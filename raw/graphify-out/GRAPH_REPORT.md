# Graph Report - C:\Users\mateu\Desktop\recommendation_fuzzy\raw  (2026-06-23)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 13 nodes · 10 edges · 5 communities (1 shown, 4 thin omitted)
- Extraction: 60% EXTRACTED · 40% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bf83c5cb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]

## God Nodes (most connected - your core abstractions)
1. `Sistema de Recomendação Baseado em Ontologias Fuzzy` - 8 edges
2. `Cold Start Problem` - 2 edges
3. `Karthik & Ganapathy (2021)` - 2 edges
4. `Amazon Reviews 2023 — Home and Kitchen` - 1 edges
5. `Kouzina Club` - 1 edges
6. `Produto Premium/Luxo` - 1 edges
7. `Haw et al. (2024)` - 1 edges
8. `Yuan & Hernandez (2023)` - 1 edges
9. `Guo et al. (2022)` - 1 edges
10. `Yager (2003)` - 1 edges

## Surprising Connections (you probably didn't know these)
- `Guo et al. (2022)` --cites--> `Sistema de Recomendação Baseado em Ontologias Fuzzy`  [INFERRED]
  investigacao_tcc_revisao_dataset.md → investigacao_dataset.md
- `Karthik & Ganapathy (2021)` --cites--> `Sistema de Recomendação Baseado em Ontologias Fuzzy`  [EXTRACTED]
  investigacao_tcc_revisao_dataset.md → investigacao_dataset.md
- `Yager (2003)` --cites--> `Sistema de Recomendação Baseado em Ontologias Fuzzy`  [INFERRED]
  investigacao_tcc_revisao_dataset.md → investigacao_dataset.md
- `Haw et al. (2024)` --cites--> `Sistema de Recomendação Baseado em Ontologias Fuzzy`  [EXTRACTED]
  investigacao_tcc_revisao_dataset.md → investigacao_dataset.md
- `Revisão bibliográfica e levantamento de Datasets` --references--> `Karthik & Ganapathy (2021)`  [INFERRED]
  arquivos_tcc/Cronograma de Tarefas TCC_d1ea91f9.md → investigacao_tcc_revisao_dataset.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **TCC Methodology and Dataset Selection** — investigacao_dataset_amazon_reviews_2023, investigacao_dataset_kouzina_club, investigacao_dataset_premium_product [EXTRACTED 0.95]
- **Fuzzy Ontology Recommendation Research Core** — investigacao_tcc_revisao_dataset_karthik_2021, investigacao_tcc_revisao_dataset_haw_2024, investigacao_dataset_fuzzy_ontology_system [EXTRACTED 1.00]

## Communities (5 total, 4 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (7): Amazon Reviews 2023 — Home and Kitchen, Sistema de Recomendação Baseado em Ontologias Fuzzy, Kouzina Club, Produto Premium/Luxo, Guo et al. (2022), Haw et al. (2024), Yager (2003)

## Knowledge Gaps
- **8 isolated node(s):** `recommendation_fuzzy`, `Amazon Reviews 2023 — Home and Kitchen`, `Kouzina Club`, `Produto Premium/Luxo`, `Haw et al. (2024)` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Sistema de Recomendação Baseado em Ontologias Fuzzy` connect `Community 0` to `Community 1`, `Community 2`?**
  _High betweenness centrality (0.652) - this node is a cross-community bridge._
- **Why does `Cold Start Problem` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Why does `Karthik & Ganapathy (2021)` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Sistema de Recomendação Baseado em Ontologias Fuzzy` (e.g. with `Kouzina Club` and `Guo et al. (2022)`) actually correct?**
  _`Sistema de Recomendação Baseado em Ontologias Fuzzy` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `recommendation_fuzzy`, `Amazon Reviews 2023 — Home and Kitchen`, `Kouzina Club` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._