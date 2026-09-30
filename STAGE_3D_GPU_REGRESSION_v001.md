# Stage 3D — GPU Regression & Identity Validation v001

## Status
BLOCKED ONLY BY GPU EXECUTION. The pipeline specification and preflight checks are ready; no image-generation result is claimed until an actual CUDA run is completed.

## Purpose
A real generation matrix is required to test facial identity, head/body proportions, natural rendering, expression specificity, hijab independence, clothing independence, pose/view robustness, lighting/environment robustness, and camera stability.

## Baseline
- base: FLUX.1-dev
- identity conditioner: PuLID-FLUX-v0.9.1
- dataset: rana_dataset_v003
- reference bank: rana_reference_bank_v001
- expression conditioning: rana_expression_conditioning_v001
- conditioning assets: rana_conditioning_assets_v002

## Hardware gate
Preferred: NVIDIA CUDA GPU, 48 GB VRAM if available.
Minimum target: 24 GB VRAM.
Consumer fallback: FP8/offload when supported by the pinned upstream implementation.

## Required
Access to a CUDA machine with at least 24 GB VRAM, or a private cloud CUDA environment. Personal source images and derived assets must remain private.

## Preflight
Verify CUDA, VRAM, Python, exact dependency versions, FLUX access/license acceptance, PuLID v0.9.1, source ZIP SHA-256, private asset hashes, dataset split separation, resolver tests, and isolated output storage.

## Regression
Fixed seeds: 101, 202, 303, 404, 505, 606, 707, 808.
Unseen seeds: 909, 1001, 1102, 1203.
Identity scale sweep: 0.75, 1.00, 1.15.

Families:
1. identity baseline: front / 3/4 / side
2. expression: neutral / smiling / pout / wink_smile / eyes_closed / looking_up / looking_down
3. wardrobe independence: black / white / light-gray square hijab and multiple outfits
4. body/view: front / 3/4 / side / sitting / rear evaluation
5. environment/camera: indoor / outdoor / neutral background / varied framing
6. unseen-seed generalization

## Evaluation order
Preflight → identity → expression → wardrobe → body/view → environment/camera → unseen seeds → validation → holdout → F01-F10 review.

Do not tune against holdout.

## Failure codes
F01 facial identity drift
F02 body proportion drift
F03 head-to-body proportion drift
F04 apparent-age drift
F05 skin/rendering drift
F06 hijab entanglement
F07 clothing entanglement
F08 pose drift
F09 camera/perspective drift
F10 temporal inconsistency (future video)

## Escalation
First fix references, crops, masks, scales, prompt separation, and pose/depth controls. Only systematic body drift can justify a body adapter. Only systematic expression-reference failure can justify an expression adapter. Hijab/clothing must never be fused into identity.

## Completion
A real GPU report must contain model/dependency revisions, seeds, prompts, conditioning references, scales, output hashes, validation observations, holdout observations, and F01-F10 classification. A single attractive image is not sufficient.
