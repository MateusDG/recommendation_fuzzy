# Revisão rigorosa da introdução e das fontes

Data: 30/06/2026

Arquivo revisado:

- `outputs/Capitulo_1_Introducao.md`
- `outputs/Capitulo_1_Introducao.docx`

## Parecer geral

A introdução está adequada ao estágio atual do projeto, desde que seja apresentada como proposta metodológica de protótipo e não como sistema já implementado. O texto está coerente com o tema do TCC, com o escopo de governança/metodologia e com a validação real do dataset. As principais fontes foram conferidas contra PDFs locais, DOI, arXiv ou página oficial do dataset.

## Correções aplicadas

| Problema encontrado | Correção feita | Motivo |
| --- | --- | --- |
| Uso de “Haw et al., 2024” para ontologia/e-commerce | Substituído por Guia, Silva e Bernardino (2019) | O PDF local disponível é `A Hybrid Ontology-Based Recommendation System in e-Commerce`, publicado em 2019. |
| Uso de “Hou et al., 2023” para Amazon Reviews 2023 | Atualizado para Hou et al. (2024) | O artigo `Bridging Language and Items for Retrieval and Recommendation` está associado ao arXiv `2403.03952`, de 2024. |
| Uso de “Yager, 2003” sem PDF local correspondente | Substituído por Jain e Gupta (2018) | O PDF local disponível é `Fuzzy Logic in Recommender Systems`, capítulo da Springer de 2018. |
| Categorias do dataset tratadas como hipotéticas | Substituídas por categorias validadas no schema | A introdução passou a citar categorias observadas em `meta_Home_and_Kitchen.jsonl.gz`. |
| Escopo sugerindo API/vitrine/captura real de comportamento | Texto suavizado para arquitetura do protótipo, ranking Top-N e extração/simulação de preferências | O projeto ainda está na fase de governança, recorte metodológico e validação de schema. |

## Matriz de fontes usadas na introdução

| Citação na introdução | Evidência verificada | Uso no texto | Status |
| --- | --- | --- | --- |
| ADOMAVICIUS; TUZHILIN, 2005 | PDF local `raw/recommender-systems-survey-2005.pdf` | Fundamentos e limitações de sistemas de recomendação | Adequada. |
| ISINKAYE; FOLAJIMI; OJOKOH, 2015 | PDF local `raw/Recommendation-systems--Principles--methods-and-_2015_Egyptian-Informatics-J.pdf`; DOI `10.1016/j.eij.2015.06.005` | Métodos, princípios e avaliação de recomendadores | Adequada. |
| BURKE, 2002 | PDF local `raw/Hybrid_Recommender_Systems_Survey_and_Experiments.pdf` | Justificativa de sistema híbrido | Adequada. |
| YUAN; HERNANDEZ, 2023 | PDF local `raw/User_Cold_Start_Problem_in_Recommendation_Systems_A_Systematic_Review.pdf` | Problema de cold start | Adequada. |
| JAIN; GUPTA, 2018 | PDF local `raw/Fuzzy Logic in Recommender Systems.pdf`; DOI `10.1007/978-3-319-71008-2_20` | Lógica fuzzy, incerteza, preferências graduais | Adequada após correção. |
| KARTHIK; GANAPATHY, 2021 | PDF local `raw/A fuzzy recommendation system for predicting the customers interests using sentiment analysis and ontology in e-commerce.pdf`; DOI `10.1016/j.asoc.2021.107396` | Fuzzy + ontologia + e-commerce | Adequada. |
| GUIA; SILVA; BERNARDINO, 2019 | PDF local `raw/A_Hybrid_Ontology-Based_Recommendation_System_in_e.pdf`; DOI `10.3390/a12110239` | Ontologia + recomendação híbrida em e-commerce | Adequada após correção. |
| GUO et al., 2022 | PDF local `raw/A Survey on Knowledge Graph-Based.pdf` | Recomendação baseada em conhecimento/grafos e apoio à semântica | Adequada para fundamentação semântica. |
| ZHANG; CHEN, 2020 | DOI `10.1561/1500000066`, Crossref: publicado em 11/03/2020, Foundations and Trends in Information Retrieval, v. 14, n. 1, p. 1-101 | Explicabilidade em sistemas de recomendação | Adequada. |
| HOU et al., 2024 | PDF local `raw/Bridging Language and Items for Retrieval and Recommendation.pdf`; arXiv `2403.03952`; página oficial `https://amazon-reviews-2023.github.io/` | Dataset Amazon Reviews 2023 | Adequada após correção. |

## Validação do dataset citada na introdução

A introdução cita o Amazon Reviews 2023 - Home and Kitchen com cautela metodológica. Isso está correto porque:

- O dataset é público e compatível com o objetivo de simular recomendação em e-commerce.
- O subconjunto Home and Kitchen contém categorias próximas ao domínio de casa, cozinha, área gourmet e banheiro.
- O dataset não possui rótulo nativo de luxo/premium.
- Campos relevantes existem, mas têm limitações de cobertura, especialmente `price` e `description`.

Documentos de apoio:

- `docs/methodology/schema_amazon_home_kitchen.md`
- `docs/methodology/recorte_kouzina_amazon.md`
- `docs/methodology/evidencias_recorte_kouzina_amazon.md`

## Pontos de atenção antes da versão final ABNT

- Normalizar todas as referências em ABNT com autores completos, título, periódico/livro, volume, número, páginas, DOI e data de acesso quando aplicável.
- Decidir se será incluída uma fonte clássica adicional sobre teoria fuzzy. A introdução ficou correta com Jain e Gupta (2018), mas uma fonte seminal pode fortalecer a fundamentação teórica.
- Não tratar `store` como marca oficial sem regra de limpeza e validação.
- Não declarar que o sistema recomenda “luxo” como rótulo real do dataset; o texto deve manter “premium/luxo” como construção operacional.
- O `raw/graphify-out/GRAPH_REPORT.md` histórico ainda possui referências antigas por ser artefato gerado em 23/06/2026. Para envio ao orientador, usar este relatório e os documentos revisados, não o Graphify histórico.

## Validação executada no DOCX

O arquivo `outputs/Capitulo_1_Introducao.docx` foi regenerado a partir de `outputs/Capitulo_1_Introducao.md`.

Checagem estrutural por leitura do `.docx`:

- Parágrafos não vazios: 35.
- Caracteres lidos: 14.381.
- Tokens antigos removidos: `HAW`, `Haw`, `YAGER`, `Yager`, `HOU et al., 2023`, `Hou et al., 2023`, `componentes de API`, `captura ou simulação`.
- Tokens corrigidos encontrados: `HOU et al., 2024` = 3; `GUIA; SILVA; BERNARDINO, 2019` = 4; `JAIN; GUPTA, 2018` = 4; `rankings Top-N` = 2.
- Caracter de substituição Unicode: 0.

Observação: a renderização visual do `.docx` para PNG/PDF não foi concluída porque o executável LibreOffice/`soffice` não está instalado neste ambiente. A validação estrutural do conteúdo foi concluída.
