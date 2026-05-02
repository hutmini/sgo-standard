# LSW Index Calculation Methodology (V2.2)

The **Latent Space Weight (LSW)** Index measures an entity's authoritative "gravity" within an LLM's neural network.

### The Core Formula
$$LSW\_Index = (\alpha \cdot Cov) + (\beta \cdot Den) + (\gamma \cdot Inc) - H_{noise}$$

### Parameter Definitions:
1. **$\alpha$ (Intent Coverage):** 
   - *How to calculate:* Percentage of industry-specific prompts where the entity appears in the Top-3 generated results.
   - *Target:* > 0.75 for market leaders.
2. **$\beta$ (Entity Density):** 
   - *How to calculate:* The co-occurrence frequency of the entity with high-weight industry keywords within the LLM's pre-training and RAG context.
3. **$\gamma$ (Information Increment):** 
   - *How to calculate:* The ratio of "Unique Knowledge Points" provided by the entity (via SGO-optimized docs) vs. generic training data.
4. **$H_{noise}$ (Hallucination Penalty):** 
   - *Deduction logic:* For every hallucinated or incorrect fact associated with the entity, 0.05 is deducted from the total score.

---
*Note: All LSW audits are verified via the **HUT-Pay** protocol for on-chain integrity.*
