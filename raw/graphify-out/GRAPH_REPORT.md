# Graph Report - C:\Users\mateu\Desktop\recommendation_fuzzy\raw  (2026-06-23)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 35 nodes · 25 edges · 12 communities (5 shown, 7 thin omitted)
- Extraction: 56% EXTRACTED · 44% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fc23ee6c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]

## God Nodes (most connected - your core abstractions)
1. `Sistema de Recomendação Baseado em Ontologias Fuzzy` - 8 edges
2. `Recommender Systems` - 5 edges
3. `Cold Start Problem` - 2 edges
4. `Karthik & Ganapathy (2021)` - 2 edges
5. `Knowledge Graph-Based Recommender Systems` - 2 edges
6. `Fuzzy Recommendation System with Sentiment Analysis and Ontology` - 2 edges
7. `Ontology Modeling` - 2 edges
8. `Collaborative Filtering` - 2 edges
9. `Collaborative Filtering` - 2 edges
10. `Content-based Filtering` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Guo et al. (2022)` --cites--> `Sistema de Recomendação Baseado em Ontologias Fuzzy`  [INFERRED]
  investigacao_tcc_revisao_dataset.md → investigacao_dataset.md
- `Yager (2003)` --cites--> `Sistema de Recomendação Baseado em Ontologias Fuzzy`  [INFERRED]
  investigacao_tcc_revisao_dataset.md → investigacao_dataset.md
- `Recommender Systems Survey (2005)` --references--> `Recommender Systems`  [INFERRED]
  recommender-systems-survey-2005.pdf → Recommender systems survey.pdf
- `Investigative Survey of Recommender Systems` --references--> `Recommender Systems`  [INFERRED]
  Revisiting recommender systems an investigative survey.pdf → Recommender systems survey.pdf
- `Cold Start Problem` --conceptually_related_to--> `Recommender Systems`  [INFERRED]
  User_Cold_Start_Problem_in_Recommendation_Systems_A_Systematic_Review.pdf → Recommender systems survey.pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Semantic and Knowledge-Aware Recommendation** — a_survey_on_knowledge_graph_based_kg_rec, knowledge_basedrecommendation_kb_rec, a_hybrid_ontology_based_recommendation_system_hybrid_ontology, a_fuzzy_recommendation_system_fuzzy_sentiment_ontology [INFERRED 0.85]
- **Hybrid Recommendation Frameworks** — hybrid_recommender_systems_survey_hybrid_survey, a_hybrid_ontology_based_recommendation_system_hybrid_ontology, recommendation_systems_principles_methods_principles_methods [INFERRED 0.80]
- **Core Recommendation Methodologies** — recommender_systems_survey_collaborative_filtering, recommender_systems_survey_content_based_filtering, recommender_systems_survey_hybrid_methods [EXTRACTED 0.95]

## Communities (12 total, 7 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.22
Nodes (9): Revisão bibliográfica e levantamento de Datasets, Amazon Reviews 2023 — Home and Kitchen, Sistema de Recomendação Baseado em Ontologias Fuzzy, Kouzina Club, Produto Premium/Luxo, Guo et al. (2022), Haw et al. (2024), Karthik & Ganapathy (2021) (+1 more)

### Community 1 - "Community 1"
Cohesion: 0.29
Nodes (8): Recommender Systems Survey (2005), Collaborative Filtering, Content-based Filtering, Hybrid Recommendation Methods, Recommender Systems, Investigative Survey of Recommender Systems, Cold Start Problem, User Cold Start Problem Systematic Review

### Community 2 - "Community 2"
Cohesion: 0.50
Nodes (4): Fuzzy Recommendation System with Sentiment Analysis and Ontology, Hybrid Ontology-Based Recommendation System, Ontology Modeling, Sentiment Analysis

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (3): Knowledge Graph-Based Recommender Systems, Explainable Recommendation Survey, Knowledge-Based Recommendation

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (3): Collaborative Filtering, Deep Learning Based Recommender System Survey, Hybrid Recommender Systems Survey

## Knowledge Gaps
- **21 isolated node(s):** `recommendation_fuzzy`, `Amazon Reviews 2023 — Home and Kitchen`, `Kouzina Club`, `Produto Premium/Luxo`, `Haw et al. (2024)` (+16 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Sistema de Recomendação Baseado em Ontologias Fuzzy` connect `Community 0` to `Community 5`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Why does `Cold Start Problem` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Sistema de Recomendação Baseado em Ontologias Fuzzy` (e.g. with `Kouzina Club` and `Guo et al. (2022)`) actually correct?**
  _`Sistema de Recomendação Baseado em Ontologias Fuzzy` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Recommender Systems` (e.g. with `Recommender Systems Survey (2005)` and `Investigative Survey of Recommender Systems`) actually correct?**
  _`Recommender Systems` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Knowledge Graph-Based Recommender Systems` (e.g. with `Knowledge-Based Recommendation` and `Explainable Recommendation Survey`) actually correct?**
  _`Knowledge Graph-Based Recommender Systems` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `recommendation_fuzzy`, `Amazon Reviews 2023 — Home and Kitchen`, `Kouzina Club` to the rest of the system?**
  _23 weakly-connected nodes found - possible documentation gaps or missing edges._