#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path
from types import SimpleNamespace

REPO = "https://github.com/riskean/rana_model.git"
PULID_REPO = "https://github.com/ToTheBeginning/PuLID.git"
WORK = Path("/content")
RANA = WORK / "rana_model"
PULID = WORK / "PuLID"
INPUT_DIR = WORK / "rana_private"
OUTPUT_DIR = WORK / "rana_outputs"
IDENTITY_REF = "IMG_20260901_005542.jpg"


def run(cmd, cwd=None, check=True):
    print("\n$ " + " ".join(map(str, cmd)))
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=check)


def pip_install(requirements_file=None):
    run([sys.executable, "-m", "pip", "install", "-q", "-r", str(requirements_file)])


def gpu_info():
    import torch
    if not torch.cuda.is_available():
        raise RuntimeError(
            "No CUDA GPU is attached. In Colab choose Runtime > Change runtime type > GPU."
        )
    props = torch.cuda.get_device_properties(0)
    vram_gb = props.total_memory / (1024**3)
    print(f"GPU: {props.name}")
    print(f"VRAM: {vram_gb:.1f} GB")
    print(f"PyTorch: {torch.__version__}")
    print(f"CUDA: {torch.version.cuda}")
    return props.name, vram_gb


def choose_mode(vram_gb):
    if vram_gb >= 30:
        return dict(fp8=False, offload=True, aggressive=False, onnx="gpu")
    if vram_gb >= 20:
        return dict(fp8=False, offload=True, aggressive=True, onnx="gpu")
    if vram_gb >= 16:
        return dict(fp8=True, offload=True, aggressive=False, onnx="cpu")
    if vram_gb >= 11:
        return dict(fp8=True, offload=True, aggressive=True, onnx="cpu")
    raise RuntimeError("VRAM is below the practical PuLID-FLUX target (~11 GB).")


def clone_repos():
    if not RANA.exists():
        run(["git", "clone", REPO, str(RANA)])
    if not PULID.exists():
        run(["git", "clone", PULID_REPO, str(PULID)])


def install_pulid(vram_gb):
    pip_install(PULID / "requirements.txt")
    if vram_gb < 20 and (PULID / "requirements-fp8.txt").exists():
        pip_install(PULID / "requirements-fp8.txt")


def login_huggingface():
    token = os.environ.get("HF_TOKEN")
    try:
        from google.colab import userdata
        token = token or userdata.get("HF_TOKEN")
    except Exception:
        pass

    from huggingface_hub import login
    if token:
        login(token=token, add_to_git_credential=False, skip_if_logged_in=True)
    else:
        print("No HF_TOKEN secret found; interactive Hugging Face login will appear.")
        login(add_to_git_credential=False, skip_if_logged_in=True)


def download_flux_weights():
    from huggingface_hub import hf_hub_download
    models = PULID / "models"
    models.mkdir(exist_ok=True)

    for filename in ("flux1-dev.safetensors", "ae.safetensors"):
        target = models / filename
        if not target.exists():
            print(f"Downloading {filename} ...")
            hf_hub_download(
                repo_id="black-forest-labs/FLUX.1-dev",
                filename=filename,
                local_dir=str(models),
            )


def upload_private_zip():
    if INPUT_DIR.exists() and list(INPUT_DIR.rglob("*")):
        return

    from google.colab import files
    print("Upload the private barunya.zip now. It is NOT uploaded to GitHub.")
    uploaded = files.upload()
    if not uploaded:
        raise RuntimeError("No ZIP was uploaded.")

    zip_name = next(iter(uploaded))
    zip_path = WORK / zip_name
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(INPUT_DIR)
    zip_path.unlink(missing_ok=True)


def extract_private_zip(zip_path):
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(INPUT_DIR)


def validate_private_dataset():
    image_ext = {".jpg", ".jpeg", ".png", ".webp"}
    images = sorted(p for p in INPUT_DIR.rglob("*") if p.suffix.lower() in image_ext)
    print(f"Private image count: {len(images)}")
    if len(images) != 34:
        raise RuntimeError(f"Expected 34 images, found {len(images)}.")

    refs = [p for p in images if p.name == IDENTITY_REF]
    if len(refs) != 1:
        raise RuntimeError(f"Could not locate {IDENTITY_REF}.")
    return refs[0]


def validate_repo():
    validator = RANA / "tools" / "validate_conditioning_manifest.py"
    if validator.exists():
        run([sys.executable, str(validator)], cwd=RANA)


def generate(identity_path, vram_gb, mode):
    import numpy as np
    from PIL import Image

    os.chdir(PULID)
    sys.path.insert(0, str(PULID))
    from app_flux import FluxGenerator

    cfg = choose_mode(vram_gb)
    print("Selected runtime:", cfg)

    args = SimpleNamespace(
        version="v0.9.1",
        fp8=cfg["fp8"],
        onnx_provider=cfg["onnx"],
        pretrained_model=None,
    )

    generator = FluxGenerator(
        "flux-dev",
        device="cuda",
        offload=cfg["offload"],
        aggressive_offload=cfg["aggressive"],
        args=args,
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    prompt = (
        "photorealistic adult Indonesian woman, natural skin texture, "
        "standing full body, relaxed natural pose, black square hijab, "
        "white long-sleeve top, black pants, realistic indoor photography, "
        "soft natural lighting, 3:4 portrait"
    )

    seeds = [101] if mode == "smoke" else [101, 202, 303, 404, 505, 606, 707, 808]
    id_image = np.array(Image.open(identity_path).convert("RGB"))

    for seed in seeds:
        print(f"\n=== seed {seed} ===")
        t0 = time.time()
        image, used_seed, _debug = generator.generate_image(
            width=768,
            height=1024,
            num_steps=28,
            start_step=4,
            guidance=4.0,
            seed=seed,
            prompt=prompt,
            id_image=id_image,
            id_weight=1.0,
            neg_prompt="bad quality, worst quality, text, signature, watermark, extra limbs",
            true_cfg=1.0,
            timestep_to_start_cfg=1,
            max_sequence_length=128,
        )
        out = OUTPUT_DIR / f"rana_seed_{used_seed}.png"
        image.save(out)
        print(f"Saved: {out}")
        print(f"Elapsed: {time.time() - t0:.1f}s")

    archive = shutil.make_archive(str(WORK / "rana_outputs"), "zip", OUTPUT_DIR)
    print(f"Output archive: {archive}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["smoke", "regression"], default="smoke")
    parser.add_argument("--zip", default=None)
    args = parser.parse_args()

    print("=== RANA COLAB GPU RUNNER ===")
    gpu_name, vram_gb = gpu_info()
    print(f"Using {gpu_name} / {vram_gb:.1f} GB VRAM")

    clone_repos()
    install_pulid(vram_gb)
    login_huggingface()
    download_flux_weights()

    if args.zip:
        extract_private_zip(args.zip)
    else:
        upload_private_zip()

    identity_path = validate_private_dataset()
    validate_repo()
    print(f"Identity reference: {identity_path}")
    generate(identity_path, vram_gb, args.mode)


if __name__ == "__main__":
    main()
