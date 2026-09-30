# GPU Run Request

The next project gate requires actual CUDA inference.

## What I need from the user

### Option A — Your own PC/workstation
Provide:
- GPU model
- VRAM
- Windows/Linux
- available disk space
- whether Python/Conda can run

### Option B — Cloud GPU
Provide access to a CUDA instance with at least 24 GB VRAM target, preferably 48 GB, sufficient system RAM and disk, and private file handling.

## Do not provide
- passwords
- API keys
- public uploads of the original photos
- validation/holdout files mixed into training

## Preflight
Run:
python tools/gpu_preflight.py

Send the output. The execution configuration will be finalized from the actual hardware rather than guessed.

## Current limitation
The current runtime is CPU-only: no NVIDIA GPU and no CUDA-enabled PyTorch. Therefore no generation result is claimed yet.
