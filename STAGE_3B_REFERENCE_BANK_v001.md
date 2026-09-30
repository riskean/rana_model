# Stage 3B — Reference Bank Engineering v001

## Objective

Build a small, explicit reference bank for `rana_person` so identity, expression, and body geometry can be conditioned independently.

The reference bank is an inference asset map, not a new training dataset. The frozen dataset `rana_dataset_v003` remains unchanged.

## Hard separation

`rana_person` = identity

`expression preset` = subject-specific expression behavior

`body reference` = geometry / pose support

`hijab` = wardrobe variable

`clothing` = wardrobe variable

No reference in the bank is allowed to silently become a permanent identity attribute.

## Identity reference bank

Use TRAIN images only for the canonical baseline identity bank.

### Canonical neutral front

- `IMG_20260901_005542.jpg`
- Role: primary identity face reference
- View: frontal portrait
- Expression: neutral
- Reason: clear frontal face with minimal expression and no full-body wardrobe dependence
- Conditioning: face-focused crop/mask only

### Canonical neutral 3/4

- `IMG_20260901_005744.jpg`
- Role: primary 3/4 identity support
- View: 3/4 portrait
- Expression: neutral
- Reason: adds non-frontal identity geometry without using a full-body appearance
- Conditioning: face-focused crop/mask only

### Secondary neutral 3/4

- `CYMERA_20260901_005132.jpg`
- Role: identity cross-check/reference alternative
- View: 3/4 close-up
- Expression: neutral
- Reason: different capture and hijab tone reduce overfitting to one image
- Conditioning: face-focused crop/mask only

### Optional side identity support

- `IMG_20260901_005731.jpg`
- Role: side-view identity evaluation/support
- View: side portrait
- Expression: neutral
- Reason: profile geometry is useful for identity checks
- Conditioning: face-focused crop/mask only
- Do not use as the sole identity reference.

## Expression reference bank

Expression references are never used as the sole identity reference.

### Smiling

Primary TRAIN references:
- `1790605624951.jpg`
- `CYMERA_20260901_001623.jpg`
- `CYMERA_20260901_005029.jpg`
- `IMG_20260901_005629.jpg`
- `IMG_20260901_005650.jpg`

Preferred prototype order:
1. `CYMERA_20260901_005029.jpg` — clear frontal smile
2. `IMG_20260901_005629.jpg` — second frontal smile
3. `1790605624951.jpg` — additional capture
4. `IMG_20260901_005921.jpg` — 3/4 smile, VALIDATION only; evaluation reference, not baseline fitting/reference bank

The harness should normally use a frontal smile prototype first, with 3/4 smile reserved for view-robustness tests.

### Pout

- `CYMERA_20260901_005335.jpg`
- `IMG_20260901_005815.jpg`

Use expression-region conditioning. Do not infer identity from these references.

### Wink + smile

- `IMG_20260901_005650.jpg`

Treat as a distinct expression preset rather than merging it into ordinary smiling.

### Eyes closed

- `CYMERA_20260824_230551.jpg`

### Looking up

- `CYMERA_20260901_001623.jpg`

### Looking down

- `CYMERA_20260901_001324.jpg`

## Body geometry reference bank

Body references are used for spatial geometry and pose support, not face identity.

### Front full-body

- `CYMERA_20260901_002601.jpg`
- `file_000000001d6c81f5a63d04b00dd863a4.png`

### 3/4 full-body

- `CYMERA_20260901_004624.jpg`
- `1790678683041.jpg`

### Side full-body

- `1790592352294.jpg`

### Rear

No TRAIN rear reference is designated for the baseline.

The rear full-body image `CYMERA_20260928_174838.jpg` is HOLDOUT and must remain evaluation-only. This is intentional: the baseline should be tested on rear-view generalization without using that exact reference to fit the system.

## Reference masking rules

### Identity channel

Use a face-focused crop/mask that contains the facial region and only the minimum surrounding context needed by the identity extractor.

Do not use the full image when the purpose is identity.

### Expression channel

Use an expression-region crop/mask covering the eyes, eyelids, nose-to-mouth area, cheeks, and the visible local facial context needed to preserve the subject-specific expression.

The expression reference may contain hijab pixels around the face, but those pixels must be excluded or minimized by the mask.

### Body channel

Use full-body or upper-body spatial references only when depth/pose/body geometry is required.

The RGB appearance of the body reference must not become the face identity embedding.

## Selection policy

1. Prefer TRAIN references for baseline fitting/conditioning.
2. Prefer clear face visibility over image resolution alone.
3. Prefer neutral expression for identity.
4. Prefer frontal + 3/4 diversity over many near-identical frontal frames.
5. Do not use validation or holdout references in baseline fitting.
6. Validation and holdout references remain reserved for evaluation.
7. Never create identity names tied to hijab or outfit.
8. Never average unrelated full-body images into a single identity embedding.

## Canonical inference mapping

The intended user-facing behavior is:

`rana_person`
→ primary neutral identity reference

`rana_person + smiling`
→ primary neutral identity reference + smiling expression prototype

`rana_person + smiling + black square hijab`
→ primary neutral identity reference + smiling expression prototype + independent black square hijab condition

`rana_person + 3/4 + smiling`
→ identity reference + 3/4 pose/view control + smiling expression prototype

Changing hijab or outfit must not require rebuilding the identity reference.

## Evaluation leakage rule

For the first benchmark:

- TRAIN references may be used by the conditioning harness.
- VALIDATION images are comparison targets only.
- HOLDOUT images are final generalization targets only.
- A validation/holdout source image must never be selected as the canonical identity reference for the same benchmark run.

## Status

**APPROVED FOR STAGE 3 BASELINE**

Next step: implement the inference/evaluation harness that resolves user shorthand such as `rana_person + smiling` into these separated conditioning channels and records every reference, strength, seed, prompt, and result for reproducible comparison.
