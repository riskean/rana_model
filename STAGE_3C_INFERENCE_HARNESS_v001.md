# Stage 3C — Inference & Consistency Harness v001

## Objective

Turn shorthand user prompts into reproducible, separated conditioning requests.

Example:

`rana_person, smiling, black square hijab`

must resolve to:

1. identity = Rana face reference
2. expression = Rana smiling prototype
3. wardrobe = black square hijab
4. pose/view = requested or default
5. environment/lighting/camera = requested or controlled defaults

## Resolver rules

### Identity
`rana_person` always activates the canonical identity reference.

### Expression
`smiling` activates the subject-specific smiling preset.

Other presets:
- pout
- wink_smile
- eyes_closed
- looking_up
- looking_down

### Wardrobe
Hijab and clothing are text/garment conditions only unless an explicit garment reference is requested.

### Pose/view
Use pose/depth conditioning when required. Never increase identity strength merely to force pose.

## Baseline test matrix

### Test A — identity
- neutral front portrait
- neutral 3/4 portrait
- side portrait

### Test B — smile
- smiling front
- smiling 3/4
- smiling with alternate hijab
- smiling with alternate outfit

### Test C — wardrobe independence
Keep identity/expression fixed while changing:
- black square hijab
- white square hijab
- light neutral square hijab
- pashmina
- different outfits

### Test D — body
- front full body
- 3/4 full body
- side full body
- sitting
- rear

### Test E — environment
- indoor
- outdoor
- soft light
- harder directional light
- different camera framing

### Test F — holdout generalization
Run against the frozen HOLDOUT conditions without using those images as fitting/reference inputs.

## Reproducibility

Every generation record must contain:
- identity version
- dataset version
- reference-bank version
- expression version
- base model and exact model revision
- adapter versions
- prompt
- negative prompt if used
- seed
- resolution
- sampler/scheduler
- inference steps
- guidance settings
- identity/reference scales
- pose/depth settings
- output filename/hash

## Acceptance dimensions

Evaluate separately:

F01 facial identity drift
F02 body proportion drift
F03 head-to-body proportion drift
F04 apparent-age drift
F05 skin/rendering drift
F06 hijab entanglement
F07 clothing entanglement
F08 pose drift
F09 camera/perspective drift
F10 temporal inconsistency for later video work

## Critical acceptance rule

A single attractive output is not sufficient.

The baseline passes only if the identity remains stable across multiple seeds and multiple independent changes to expression, hijab, clothing, pose, framing, lighting, and environment.

## Seed protocol

For each canonical test:
- use a fixed seed set for regression
- use additional unseen seeds for robustness
- do not cherry-pick the most similar image

## Escalation

If face identity is weak:
1. adjust identity reference/crop
2. sweep identity strength
3. inspect reference quality
4. only then consider an alternative identity conditioner

If body geometry is weak:
1. add depth/pose support
2. test camera/perspective
3. only then evaluate `rana_body_v001`

If expression is generic:
1. improve expression crop/mask
2. improve expression reference selection
3. test expression conditioning strength
4. only then consider a dedicated expression adapter

If hijab/clothing changes identity:
1. remove wardrobe-heavy identity references
2. strengthen face-focused conditioning
3. reduce uncontrolled image conditioning
4. do not solve the problem by permanently fusing wardrobe into identity

## Status

**NEXT IMPLEMENTATION STAGE**

The harness must be implemented before training any optional body adapter.
