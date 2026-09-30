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
## Completeness audit
- PROJECT_COMPLETENESS_AUDIT_v001.md
- Stage 2D conditioning asset preparation: STAGE_2D_CONDITIONING_ASSETS_v001.md
- Stage 3C inference harness: STAGE_3C_INFERENCE_HARNESS_v001.md
- Harness config: configs/inference_harness_v001.yaml
- Core specifications restored: CHARACTER_BIBLE.md, DATASET_SPEC.md, TRAINING_PIPELINE.md, PROMPT_SCHEMA.md


## Stage 2D — Conditioning assets
- Stage 2D v001 specification retained for provenance.
- Stage 2D v002 completed the private preprocessing milestone.
- Public manifest: CONDITIONING_ASSET_MANIFEST_v002.csv
- Config: configs/conditioning_assets_v002.yaml
- 18 TRAIN-only conditioning records: 4 identity, 9 expression, 5 body; 13 facial gating masks.
- Derived personal image assets remain private and are not committed.

## Stage 3C — Inference implementation
- Stage 3C v001 specification retained for provenance.
- Stage 3C v002 implementation foundation added.
- Resolver: src/rana_harness/resolver.py
- Tests: tests/test_resolver.py
- Harness config: configs/inference_harness_v002.yaml
- Local resolver tests: 4/4 passed.
- Full FLUX/PuLID image-generation regression is still pending a compatible GPU environment; it is not falsely marked complete.


## Stage 3D — GPU regression gate
- Stage 3D specification: STAGE_3D_GPU_REGRESSION_v001.md
- Config: configs/gpu_regression_v001.yaml
- Preflight: tools/gpu_preflight.py
- Hardware request: GPU_RUN_REQUEST.md
- Current runtime is CPU-only; no generation results are claimed.
- The next gate requires a real CUDA run before any body adapter, expression adapter, or character LoRA decision.
