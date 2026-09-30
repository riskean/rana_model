# Stage 3 — Identity Conditioning Architecture v001

## Decision

For the frozen 34-photo dataset (rana_dataset_v003), the project will **not** use one monolithic character LoRA as the primary identity mechanism.

The baseline architecture is a **decoupled identity-conditioning stack**:

1. **Face identity — PuLID-FLUX v0.9.1**
   - Base: FLUX.1-dev
   - Purpose: preserve facial identity only.
   - The identity reference is face-focused, not a full-body wardrobe reference.
   - No hijab, clothing, pose, expression, lighting, or background is encoded as part of the identity token.
   - PuLID-FLUX v0.9.1 is selected because its official documentation reports improved ID fidelity over v0.9.0 while retaining editability.

2. **Body geometry — Depth + Pose conditioning**
   - Use depth to stabilize body/head-to-body geometry and silhouette when a body reference is needed.
   - Use pose conditioning for the requested pose.
   - These are spatial controls, not learned character attributes.
   - The body reference should be chosen from the training set but its RGB appearance is not used as the identity embedding.

3. **Wardrobe / hijab — text or dedicated garment conditioning**
   - Hijab remains a generation-time variable.
   - Clothing remains a generation-time variable.
   - Never create identity tokens such as rana_black_hijab, rana_white_hijab, or outfit-specific identity adapters.

4. **Expression — generation-time control**
   - Expression is controlled by prompt and, when necessary, facial/pose control.
   - Expression examples in the dataset are evidence of the subject's expression range, not separate identities.

5. **Optional body-stabilizer LoRA — only after baseline evaluation**
   - Do not train it in the first experiment.
   - If the baseline preserves face but repeatedly loses the subject's body proportions, create a separate rana_body_v001 adapter.
   - It must be low-rank, low-weight, attention-focused, and trained only from TRAIN.
   - It is never fused permanently into the base model.
   - It is an auxiliary body-shape adapter, not the canonical identity representation.

## Why this architecture

The dataset has only 34 images, with 24 training images. A single full-image identity LoRA would see the same person repeatedly alongside recurring visual attributes such as square hijabs, dark/white clothing, indoor scenes, and portrait framing. With a small dataset, those correlations can become part of the learned concept.

The chosen architecture therefore separates:

face identity -> PuLID
body geometry -> depth/pose
hijab -> wardrobe condition
clothing -> wardrobe condition
expression -> expression condition
environment/lighting -> prompt/control

This makes the identity pathway narrow and the editable pathways explicit.

## Dataset usage

- TRAIN: 24 images — used for identity reference selection and any optional body-adapter training.
- VALIDATION: 6 images — never used for fitting.
- HOLDOUT: 4 images — never used for fitting; reserved for final generalization tests.
- The first baseline must not train on validation or holdout.

## Identity reference policy

Maintain a small reference bank instead of baking all 34 images into one learned identity.

Preferred face references:
- neutral frontal portrait
- neutral/soft-smile frontal portrait
- 3/4 portrait with clear face visibility

Avoid using a reference whose primary distinguishing feature is a particular hijab or outfit when the goal is identity-only conditioning.

For each generation, select the clearest compatible face reference. Do not average arbitrary full-body images into the identity embedding.

## Generation order

1. Start from the fixed FLUX base.
2. Inject face identity with PuLID.
3. Apply requested pose/depth controls if body consistency is required.
4. Describe the requested hijab and outfit independently.
5. Describe expression independently.
6. Set environment, lighting and camera independently.
7. Generate several seeds.
8. Evaluate against the fixed consistency protocol.
9. Only if body drift is systematic, train/evaluate rana_body_v001.

## Baseline tuning policy

PuLID documentation notes a trade-off between identity fidelity and editability: stronger identity conditioning improves similarity but can reduce editability. Therefore the project will test a small grid rather than permanently choosing the strongest setting.

Initial sweep:
- identity strength: 0.75 / 1.00 / 1.15
- editability/start-step control: conservative / balanced / strong-ID
- depth control: off / medium / strong
- pose control: off / medium

The exact final values are selected by the consistency test, not by a single subjective sample.

## Failure handling

- F01/F05 facial identity drift -> adjust PuLID reference/strength.
- F02/F03 body or head proportion drift -> add depth/pose control first.
- F06 hijab entanglement -> remove full-body identity reference; use face-only identity reference.
- F07 clothing entanglement -> lower/remove any body/reference image conditioning and rely on explicit wardrobe conditioning.
- F08 pose drift -> increase pose control rather than identity strength.
- F09 camera/perspective drift -> correct camera/depth conditioning, not identity strength.

## Training rule

No full-image character LoRA is approved as the default identity architecture for rana_dataset_v003.

Any future learned adapter must receive a new versioned name and be evaluated independently. The frozen dataset version remains unchanged.

## External technical basis

- PuLID-FLUX v0.9.1 is an official PuLID release for FLUX.1-dev and reports improved ID fidelity versus v0.9.0.
- PuLID injects identity features through additional cross-attention modules while keeping the FLUX backbone usable for text-driven generation.
- ControlNet-style depth/pose conditioning is designed to control spatial structure without replacing the base model.

## Status

**APPROVED FOR STAGE 3 BASELINE**

Next implementation step: build the inference/evaluation harness and run the fixed conditioning sweep before any body LoRA training.