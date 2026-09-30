# Stage 3C — Inference Harness Implementation v002

IMPLEMENTATION FOUNDATION COMPLETE.

This version adds a deterministic prompt resolver and regression-test skeleton while keeping model execution decoupled from the public repository.

Implemented:
- canonical rana_person prompt resolver
- explicit identity/expression/wardrobe/pose/view/environment/lighting/camera separation
- subject-specific expression preset routing
- deterministic identity-reference selection by view
- regression tests
- conditioning asset manifest v002 linkage
- no raw personal images or model weights in the public repository

Model execution remains pending a compatible GPU environment. The current runtime has no CUDA device, so image-generation regression results are not marked complete.

Next execution gate: load the pinned model revision, private conditioning assets, run fixed and unseen seed matrices, evaluate validation then holdout, classify F01-F10, and only then consider auxiliary body or expression adapters.

Non-shortcut rule: do not approve a character LoRA from a single attractive output. Acceptance is cross-condition identity consistency.
