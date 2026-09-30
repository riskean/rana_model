# Stage 2D — Conditioning Asset Preparation v001

## Purpose

Prepare reusable conditioning assets from the frozen dataset without changing the dataset split or identity definition.

This stage is preprocessing, not identity training.

## Assets

### Identity
- face-focused crops for canonical neutral front
- face-focused crops for neutral 3/4
- optional side/profile support
- consistent crop policy
- no full-body identity embedding

### Expression
- expression-region crops/masks
- smiling prototype
- pout prototype
- wink-smile prototype
- eyes-closed prototype
- looking-up prototype
- looking-down prototype

### Body
- front body reference
- 3/4 body reference
- side body reference
- pose/depth representations when supported by the selected pipeline

## Mask policy

Identity masks should include the facial identity region while minimizing clothing, background, and hijab-specific information.

Expression masks should emphasize the eyes, eyelids, cheeks, nose-to-mouth region, and local facial context while minimizing hijab/clothing/background.

Body conditioning is spatial. Its RGB appearance must not be passed into the face identity channel.

## Split policy

- TRAIN assets may be used for baseline conditioning.
- VALIDATION assets are evaluation-only.
- HOLDOUT assets are evaluation-only.
- Do not create a validation/holdout-derived canonical identity prototype.

## Quality checks

Every asset must record:
- source filename
- dataset split
- crop type
- mask type
- source dimensions
- preprocessing version
- checksum
- manual review status

## Failure checks

Reject or revise an asset if:
- face is clipped at an identity-critical region
- expression region is obscured
- hijab dominates an identity crop
- background dominates an identity crop
- perspective is misleading
- crop changes apparent proportions
- image is too blurry to provide useful conditioning

## Status

Specification stage complete. Actual generated assets must be produced from the original `barunya.zip` before the baseline harness is declared executable.
