# Dataset Version — rana_dataset_v003

## Identity
rana_identity_v002

## Dataset
rana_dataset_v003

## Mapping
rana_mapping_v002, finalized through Stage 2C

## Source
barunya.zip — 34 raw images

## Counts
TRAIN 24
VALIDATION 6
HOLDOUT 4

## Canonical identity token
rana_person

## Core separation
Identity is stable.
Hijab, clothing, pose, expression, environment, lighting, and camera are variables.

## Files
- datasets/manifests/source_manifest_v003.csv
- datasets/manifests/train_manifest_v003.csv
- datasets/manifests/validation_manifest_v003.csv
- datasets/manifests/holdout_manifest_v003.csv
- STAGE_2C_FINAL_VERIFICATION.md

## Freeze rule
Do not modify v003 in place after training begins. Create v004 for any dataset change.
