# Stage 2C — Final Verification and Frozen Training Manifests
Version: rana_dataset_v003
Source: barunya.zip
Raw files: 34

## Verification performed
1. Re-enumerated all raw files from the ZIP and preserved original filenames.
2. Verified image readability, dimensions, and file hashes.
3. Reviewed the full 34-image contact sheet at pixel level.
4. Rechecked view, framing, pose, expression, hijab style/color, clothing, environment, and lighting.
5. Checked for exact duplicate hashes and simple perceptual near-duplicate collisions; no exact duplicates and no suspicious low-distance dHash pairs were found.
6. Reduced the influence of repeated frontal portrait frames by using SUPPORT rather than CORE_HIGH for near-repeat images.
7. Kept hijab and clothing as variable attributes; they are never encoded into the identity token.
8. Separated TRAIN, VALIDATION, and HOLDOUT to test generalization rather than merely repeating the same compositions.

## Frozen split
- TRAIN: 24
- VALIDATION: 6
- HOLDOUT: 4
- Total: 34

## HOLDOUT rationale
The holdout set contains:
- sitting + outdoor variation
- same outfit with a different expression
- rear full-body
- rear 3/4 portrait

These cases are intentionally excluded from training so identity consistency can be evaluated under changed pose/view/context.

## Validation rationale
Validation emphasizes:
- sitting
- white-hijab 3/4 close-up
- white pashmina side view
- outdoor full-body
- alternate outdoor 3/4 full-body
- white-hijab full-body

This tests identity preservation while changing hijab, pose, environment, and framing.

## Caption policy
Canonical token: `rana_person`

Caption order:
identity → pose → view/framing → hijab → clothing → environment → lighting

No facial identity details are invented. Captions describe only observable attributes needed for training.

## Training recommendation
Use `train_manifest_v003.csv` as the primary training manifest.
Use `validation_manifest_v003.csv` and `holdout_manifest_v003.csv` only for evaluation.
Do not mix validation or holdout images back into training during the first baseline run.

## Dataset status
FROZEN FOR BASELINE TRAINING.
Any change requires a new dataset version rather than silently editing v003.
