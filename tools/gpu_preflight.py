"""Local preflight for Stage 3D."""
import platform
import sys

def main():
    print("python:", sys.version.split()[0])
    print("platform:", platform.platform())
    try:
        import torch
        print("torch:", torch.__version__)
        print("cuda_available:", torch.cuda.is_available())
        print("cuda_version:", torch.version.cuda)
        if torch.cuda.is_available():
            print("gpu:", torch.cuda.get_device_name(0))
            print("vram_gb:", round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2))
    except Exception as exc:
        print("torch_check_error:", repr(exc))
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
