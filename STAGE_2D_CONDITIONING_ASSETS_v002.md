# Stage 2D — Conditioning Assets v002

## Status

COMPLETED as a preprocessing milestone; model inference remains separate.

The frozen rana_dataset_v003 was used without changing its 24/6/4 split. Conditioning assets were generated from the original barunya.zip locally. No raw photos or derived image assets are committed to this public repository.

## Generated asset set

- identity crops: 4
- expression crops: 9
- body references: 5
- facial gating masks: 13
- validation/holdout assets used for fitting: 0
- total conditioning records: 18

All 18 conditioning records originate from TRAIN images only. VALIDATION and HOLDOUT remain evaluation-only.

## Identity assets

- neutral_front → IMG_20260901_005542.jpg
- neutral_three_quarter → IMG_20260901_005744.jpg
- neutral_three_quarter_secondary → CYMERA_20260901_005132.jpg
- side_support → IMG_20260901_005731.jpg

The secondary 3/4 crop was manually verified and corrected after automated face detection produced a false positive on the clothing pattern. This correction is explicitly recorded in the public manifest rather than silently replacing the asset.

## Expression assets

- smiling: 3 references
- pout: 2 references
- wink_smile: 1 reference
- eyes_closed: 1 reference
- looking_up: 1 reference
- looking_down: 1 reference

Expression crops are conditioning references only. They do not redefine identity and do not become wardrobe references.

## Body assets

- front: 2
- 3/4: 2
- side: 1

Body assets preserve spatial composition as geometry references. They are not face-identity embeddings.

## Masks

The 13 mask files are deterministic facial gating masks for identity/expression conditioning. They are not semantic face segmentation and must not be interpreted as pixel-perfect anatomical masks. A production implementation may replace them with a higher-quality face parser/landmark mask without changing dataset identity or split.

## Integrity

The manifest records:
- source filename
- split
- asset type/role
- preprocessing status
- asset filename
- asset SHA-256
- dimensions
- mask filename/SHA-256 where applicable

Public manifest: CONDITIONING_ASSET_MANIFEST_v002.csv

## Privacy boundary

Derived image assets remain local/private. The public repository stores only reproducibility metadata and specifications. Do not commit raw photos, face crops, masks, depth maps, pose maps, or generated personal images.

## Remaining Stage 2D work

If a production pipeline supports a stronger face parser, landmark mask, depth estimator, or pose estimator, those can be generated as new conditioning-asset versions. They must preserve the frozen dataset and must not be promoted to identity facts.
