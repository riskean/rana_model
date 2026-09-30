# rana_model

Identity-consistent generative character project for `rana_person`.

## Current state
- Stage 1A: `rana_identity_v002`
- Stage 2A: `rana_dataset_v002`
- Stage 2B: `rana_mapping_v002`
- Stage 2C: **FROZEN** `rana_dataset_v003`
- Raw source analyzed: `barunya.zip`
- Raw files: 34
- Frozen split: 24 TRAIN / 6 VALIDATION / 4 HOLDOUT

## Training-ready manifests
- `datasets/manifests/source_manifest_v003.csv`
- `datasets/manifests/train_manifest_v003.csv`
- `datasets/manifests/validation_manifest_v003.csv`
- `datasets/manifests/holdout_manifest_v003.csv`

## Verification
Stage 2C includes pixel-level review, filename preservation, readability/dimension checks, hash inventory, duplicate screening, metadata correction, caption normalization, and split leakage control.

See `STAGE_2C_FINAL_VERIFICATION.md` and `DATASET_VERSION_v003.md`.

## Principle
`rana_person` is the stable person identity. Hijab, clothing, pose, expression, environment, lighting, and camera are variable attributes.

## Privacy
Raw personal photos are not committed to this public repository. The repository stores specifications, manifests, hashes, captions, and evaluation metadata only.

## Stage 3 — Identity / Expression / Reference Architecture
- Stage 3 baseline: decoupled conditioning stack
- Face identity: PuLID-FLUX v0.9.1
- Expression: reference-conditioned, separate from identity
- Stage 3A: STAGE_3A_EXPRESSION_CONDITIONING_v001.md
- Stage 3B: STAGE_3B_REFERENCE_BANK_v001.md
- Reference bank config: configs/reference_bank_v001.yaml
- Canonical behavior: rana_person resolves to a neutral identity reference; smiling resolves to a subject-specific expression reference; hijab/clothing remain independent conditions.
- Validation and holdout references are not used for baseline fitting.
