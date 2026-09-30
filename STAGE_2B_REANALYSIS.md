# Stage 2B — Reference Mapping Reanalysis
Version: rana_mapping_v002

## Status
The reference registry has been rebuilt at filename level from the actual raw ZIP.

## Mapping
Each source is assigned an immutable filename, dimensions, short content hash, identity role, split, weight class, view, framing, pose, expression, hijab style/color, clothing, environment, lighting, capture type, and provisional caption.

## Weight classes
- CORE_HIGH — primary identity evidence
- CORE_MEDIUM — strong complementary identity evidence
- SUPPORT — useful variation/evidence
- VARIATION — attribute-separation evidence

## Important correction
The previous Stage 2B registry was category-level and memory-assisted. This version is filename-level and grounded in the supplied pixels. It is the authoritative working mapping for rana_dataset_v002.

## Review before training
Perform one final verification pass over the CSV, especially terminology for pose, expression, clothing and hijab. Then freeze rana_dataset_v002 and generate train/validation/holdout manifests.
