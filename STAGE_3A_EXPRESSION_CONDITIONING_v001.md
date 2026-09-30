# Stage 3A — Expression Reference Conditioning v001

## Goal

`rana_person + smiling` must not mean a generic smile. It should reproduce the subject's own observed smile characteristics, while leaving identity and wardrobe independently controllable.

Observed smile references in the frozen dataset include:
- `1790605624951.jpg` — frontal soft smile, close portrait
- `CYMERA_20260901_001623.jpg` — smile while looking upward
- `CYMERA_20260901_005029.jpg` — frontal smile, close portrait
- `IMG_20260901_005629.jpg` — frontal smile
- `IMG_20260901_005650.jpg` — wink + smile
- `IMG_20260901_005921.jpg` — 3/4 smile
- `IMG_20260928_213440.jpg` — full-body smile
- `IMG_20260929_175636.jpg` — full-body smile

## Critical design decision

Expression is a **condition**, not part of the identity embedding.

The system therefore has two separate concepts:

`rana_person` = who the person is
`smile` = how that person expresses

A smile reference may be supplied to define the subject-specific smile geometry, but its clothing, hijab, background, camera, and body pose must not become identity attributes.

## Smile prototype

Create a canonical expression prototype from the clearest TRAIN smile references. Prefer:
1. frontal close-up with natural smile
2. second frontal smile with different capture
3. 3/4 smile for view robustness

The prototype should preserve the observed subject-specific expression pattern: eye narrowing/squinting, mouth shape and scale, cheek movement, and the overall natural smile geometry visible in the source images.

Do not hard-code a textual claim about exact facial anatomy when it is not independently verified. The reference image is the authoritative expression evidence.

## Generation behavior

When the user asks only:
`rana_person + smiling`

the inference harness should automatically attach the canonical smile prototype in the **expression/reference channel**, while PuLID receives a separate face-identity reference.

When the user asks:
`rana_person + smiling + black square hijab`

the smile reference still controls expression, while black square hijab is supplied independently as wardrobe conditioning.

When the user asks for another expression, the harness swaps only the expression prototype.

## Reference separation

Identity reference:
- face crop
- neutral or minimally expressive
- no dependence on a specific hijab/outfit

Expression reference:
- expression is clearly visible
- can contain hijab/outfit because the reference is masked/cropped for expression extraction
- never reused as the sole identity reference

## Recommended implementation

Phase 1: reference-conditioned expression, no expression LoRA.

Use an expression reference image or expression-region conditioning together with the separate PuLID identity reference. IP-Adapter-style systems explicitly separate image and text conditioning and support combining face/image references with structural controls; masking can restrict image conditioning to selected regions. This is preferable for a 34-image dataset because it avoids training a tiny expression-specific adapter that could accidentally memorize identity or wardrobe.

Phase 2: only if reference-conditioned expression is insufficient, evaluate a dedicated expression adapter. It must be trained and evaluated as a separate module and must never be fused into `rana_person`.

## Fixed smile test

Generate the same prompt across at least 8 seeds:
- `rana_person, smiling, neutral wardrobe, front portrait`
- `rana_person, smiling, alternate hijab, front portrait`
- `rana_person, smiling, alternate outfit, 3/4 portrait`

Check:
- identity remains stable
- smile geometry remains subject-specific
- eyes/eyelids follow the observed smile pattern
- mouth shape remains consistent with the reference
- hijab can change without changing identity
- outfit can change without changing identity
- expression changes do not alter head/body proportions

## Status

**APPROVED**: subject-specific expression reference conditioning is part of the Stage 3 baseline.

Do not train an expression LoRA yet.