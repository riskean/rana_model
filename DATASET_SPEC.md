# Dataset Specification — rana_dataset_v003

## Source
- source archive: barunya.zip
- raw files: 34
- TRAIN: 24
- VALIDATION: 6
- HOLDOUT: 4

## Objective
Preserve stable identity while preventing hijab, clothing, pose, expression, environment, lighting, and camera from becoming identity attributes.

## Pipeline
RAW → CURATED → TRAIN / VALIDATION / HOLDOUT → CONDITIONING ASSETS → EVALUATION

## Caption order
identity → pose → view/framing → hijab → clothing → environment → lighting → camera/look

Canonical identity token: rana_person.

## Split rules
Validation and holdout are never used for baseline fitting. Holdout is reserved for final generalization testing.

## Metadata
Preserve source filename, split, weight class, view/framing, pose, expression, hijab style/color, clothing, environment, lighting, quality/visibility notes, and caption.

## Freeze rule
Any change creates a new dataset version. Do not silently edit v003.
