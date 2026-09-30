# Project Completeness Audit v001

## Purpose

Before moving into inference implementation, audit the entire Rana pipeline so no identity-critical stage is silently skipped.

## Ground-truth hierarchy

1. Original pixels from `barunya.zip`
2. Explicit user-provided metadata: adult woman, 155 cm, 53 kg
3. Versioned visual observations from Stage 1A/2A/2B/2C
4. Engineering assumptions, which must be marked as assumptions and never promoted to identity facts without evidence

If a property is not supported by the source pixels or explicit user metadata, do not invent it.

## Identity-critical requirements

### A. Face identity
- frontal identity
- 3/4 identity
- side/profile support
- natural asymmetry
- stable facial proportions
- no generic beautification
- no accidental face reshaping
- expression must not redefine identity

### B. Body identity
- 155 cm user metadata
- 53 kg user metadata
- observed body silhouette and relative proportions
- stable head-to-body proportion
- stable torso/limb relationships
- no arbitrary slimming, widening, height change, or head enlargement

### C. Rendering realism
- natural skin texture
- natural micro-variation/asymmetry
- realistic lighting response
- realistic lens/perspective
- no plastic/synthetic skin by default
- no automatic beauty retouching

### D. Variable attributes
These must remain editable:
- hijab presence/style/color/tie
- clothing
- shoes/accessories
- pose
- expression
- environment
- lighting
- camera/framing

### E. Reference separation
- identity reference is face-focused
- expression reference is expression-focused
- body reference is spatial/geometry-focused
- no full-body wardrobe reference is allowed to silently become identity

## Dataset status

- source: `barunya.zip`
- total: 34
- TRAIN: 24
- VALIDATION: 6
- HOLDOUT: 4
- frozen dataset: `rana_dataset_v003`
- validation/holdout must never be used for fitting the baseline

## Completed stages

- Stage 1A — identity reanalysis
- Stage 2A — dataset reanalysis
- Stage 2B — filename-level mapping
- Stage 2C — final verification and frozen split
- Stage 3 — identity conditioning architecture
- Stage 3A — expression conditioning
- Stage 3B — reference bank engineering

## Required before claiming the character is ready

1. Conditioning asset preparation: face crops/masks, expression masks, body/depth/pose references.
2. Inference harness implementation.
3. Fixed seed and prompt matrix.
4. Identity-only tests.
5. Expression-specific tests.
6. Hijab swap tests.
7. Outfit swap tests.
8. View/pose tests.
9. Body-proportion tests.
10. Lighting/environment/camera tests.
11. Validation evaluation.
12. Holdout evaluation.
13. Failure classification and remediation.
14. Only then decide whether an auxiliary body adapter is necessary.
15. Version the resulting approved inference configuration.

## Important non-shortcut rule

Do not jump directly to a character LoRA because one generated image looks similar.

The acceptance target is **cross-condition identity consistency**: the same person must remain recognizable when expression, hijab, clothing, pose, camera, lighting, and environment change.

## Stage gate

Stage 3C is allowed to begin only with the above separation rules preserved.

The first production-capable baseline is not considered approved until validation and holdout tests are recorded.
