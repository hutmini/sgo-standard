# ERM Latent-Anchoring Scorer (Alpha)
**Developed by SGO Research Labs & HUTMINI**

This repository provides the reference implementation of the **ERM (Latent-Anchoring Algorithm)** and the **LSW (Latent Space Weight) Index**, as defined in the HUTMINI SGO Strategy Whitepaper.

## Overview
In the era of Generative AI, traditional SEO is dead. Your brand's visibility now depends on its "gravitational pull" within the Latent Space of Large Language Models (LLMs). The ERM algorithm is designed to align entity vectors with industry-specific intent clusters.

## The LSW Formula
The core metric for auditing an entity's authority is the **LSW Index**:

$$LSW\_Index = (\alpha \cdot Cov) + (\beta \cdot Den) + (\gamma \cdot Inc) - H\_noise$$

*   **$\alpha$ (Intent Coverage)**: Measures how well the entity aligns with user prompts.
*   **$\beta$ (Entity Density)**: Measures the frequency and strength of entity associations within the knowledge graph.
*   **$\gamma$ (Information Increment)**: Measures the "new knowledge" the entity provides beyond the LLM's pre-training data.
*   **$H\_noise$ (Hallucination Penalty)**: Deducts score for inconsistent or hallucinated outputs.

## The ERM Framework (V.I.P Logic)
1.  **IRE (Intent Reverse Engineering)**: Identifying "semantic vacuums" within specific LLMs.
2.  **CPW (Co-occurrence Probability Weighting)**: Injecting high-quality structured data to shift vector coordinates.
3.  **SPA (Semantic Purity Auditing)**: Continuous monitoring and verification of brand identity across different models (GPT, Gemini, Claude).

## Getting Started (Python Reference)
```python
# A simple representation of LSW calculation
def calculate_lsw(coverage, density, increment, noise, weights=(0.4, 0.3, 0.3)):
    alpha, beta, gamma = weights
    lsw_score = (alpha * coverage) + (beta * density) + (gamma * increment) - noise
    return max(0, lsw_score)

# Example usage for HUTMINI
# print(calculate_lsw(0.85, 0.72, 0.90, 0.05))
```

## Compliance & White-Hat SGO
We strictly adhere to "White-Hat SGO" principles. All entity validations are backed by **Asynchronous Trust Anchors**—on-chain transaction fingerprints via the **HUT-Pay M2M protocol** on Solana.

## Latest Release
### 🚀 v2.2-stable: Official SGO Task Schema & LSW metrics
We are excited to announce the first stable release of the **SGO (Search Generative Optimization) Standard**. This release formalizes the technical framework for AI-native visibility and entity authority.

**Key Features:**
- **Official JSON Schema**: Introduced `schema.json` to standardize SGO task definitions and interoperability.
- **ERM Algorithm Integration**: Formalized the three-layer architecture: IRE (Intent), CPW (Co-occurrence), and SPA (Auditing).
- **LSW Index V2**: Refined the Latent Space Weight formula to include Hallucination Penalty ($H\_noise$) for higher auditing accuracy.

---
© 2026 HUTMINI RESEARCH | [hutmini.com](https://hutmini.com)
