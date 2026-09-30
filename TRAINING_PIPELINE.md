# Training / Conditioning Pipeline

## Baseline
The primary baseline is a decoupled conditioning system, not a monolithic character LoRA.

1. frozen dataset
2. reference-bank engineering
3. face identity conditioning
4. expression conditioning
5. body depth/pose conditioning
6. independent wardrobe conditioning
7. inference
8. regression evaluation
9. optional auxiliary body adapter only if systematic body drift is demonstrated

## Identity
Use a face-focused identity reference with PuLID-FLUX v0.9.1 on the selected FLUX base.

## Expression
Use subject-specific expression references first. Do not train an expression LoRA in the baseline.

## Body
Use depth and pose as spatial controls. Do not use identity strength to force body pose.

## Wardrobe
Hijab and clothing are generation-time conditions.

## Optional adapters
Only create rana_body_v001 after the baseline demonstrates repeatable body-proportion drift across seeds and conditions.

## Evaluation
No adapter is accepted because of one attractive sample. Acceptance requires cross-condition consistency on fixed seeds plus unseen seeds.
