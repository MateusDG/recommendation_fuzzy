# Relatório para orientação - TCC1

Data: 30/06/2026

Tema: Sistema de Recomendação Baseado em Ontologias Fuzzy para Comércio Eletrônico

## Síntese executiva

Foram concluídas três frentes de preparação do TCC: revisão bibliográfica e levantamento de datasets, levantamento/leitura de trabalhos relacionados e revisão rigorosa da introdução. O principal avanço metodológico foi deixar de tratar o recorte Kouzina -> Amazon como hipótese genérica e passar a sustentá-lo com validação real do schema e evidências extraídas do Amazon Reviews 2023 - Home and Kitchen.

Também foram corrigidas inconsistências de citação que poderiam gerar problema na orientação: a referência “Haw et al., 2024” foi substituída por Guia, Silva e Bernardino (2019), que é o artigo local efetivamente disponível sobre recomendação baseada em ontologia em e-commerce; “Hou et al., 2023” foi atualizado para Hou et al. (2024); e “Yager, 2003” foi substituído por Jain e Gupta (2018), que é o PDF disponível no repositório para lógica fuzzy em sistemas de recomendação.

## Revisão bibliográfica e levantamento de datasets

### O que foi feito

- Seleção do dataset público principal: Amazon Reviews 2023, subconjunto Home and Kitchen.
- Consulta à página oficial do dataset: https://amazon-reviews-2023.github.io/
- Validação prática dos arquivos oficiais de reviews e metadados:
  - Reviews: `https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Home_and_Kitchen.jsonl.gz`
  - Metadados: `https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz`
- Validação do schema real com `scripts/data/explorar_schema.py`, sem assumir previamente campos como preço, marca, descrição, categoria ou rating.
- Atualização do recorte metodológico Kouzina -> Amazon com evidência real do dataset.
- Criação/atualização de filtros versionados em `configs/dataset/kouzina_mapping.yaml`.

### Achados principais do dataset

- Reviews possuem campos como `user_id`, `asin`, `parent_asin`, `rating`, `title`, `text`, `timestamp`, `helpful_vote`, `verified_purchase` e `images`.
- Metadados possuem `parent_asin`, `title`, `main_category`, `categories`, `features`, `description`, `details`, `price`, `store`, `average_rating`, `rating_number`, `images` e `videos`.
- `parent_asin` deve ser tratado como elo principal entre reviews e metadados.
- `price` existe, mas é incompleto; na amostra de 50.000 metadados, 24.588 registros estavam sem preço ou com valor vazio.
- `description` também é incompleto; na mesma amostra, 22.489 registros estavam vazios.
- `store` pode ser usado como aproximação inicial de marca/loja, mas não deve ser tratado automaticamente como marca oficial.
- O dataset não possui rótulo oficial de produto premium/luxo. Esse conceito deve ser operacionalizado por critérios observáveis, como preço relativo, avaliação, popularidade, categoria, materiais e termos textuais.

Revalidação curta em 30/06/2026:

- Reviews, limite 1.000 linhas: 10 colunas observadas, sem ausência nos campos principais.
- Metadados, limite 1.000 linhas: 14 colunas observadas; `price` ausente/vazio em 463 registros; `description` vazia em 442 registros; `categories` vazia em 77 registros.

### Evidência de aderência ao domínio Kouzina

Foram encontradas categorias e sinais textuais compatíveis com cozinha, área gourmet, jantar, organização, banheiro e parte de eletrodomésticos. Exemplos de categorias validadas:

- `Kitchen & Dining`
- `Dining & Entertaining`
- `Kitchen Utensils & Gadgets`
- `Storage & Organization`
- `Bath`
- `Bathroom Accessories`
- `Dinnerware & Serveware`
- `Glassware & Drinkware`

Artefatos principais:

- `docs/methodology/schema_amazon_home_kitchen.md`
- `docs/methodology/recorte_kouzina_amazon.md`
- `docs/methodology/evidencias_recorte_kouzina_amazon.md`
- `configs/dataset/kouzina_mapping.yaml`
- `scripts/data/explorar_schema.py`
- `scripts/data/analisar_recorte_kouzina.py`

## Levantamento e leitura de trabalhos relacionados

### Eixos revisados

| Eixo | Fontes principais | Uso no TCC |
| --- | --- | --- |
| Fundamentos de recomendação | Adomavicius e Tuzhilin (2005); Isinkaye, Folajimi e Ojokoh (2015); Bobadilla et al. (2013) | Explicar tipos de recomendadores, limitações de filtragem colaborativa/conteúdo e avaliação. |
| Sistemas híbridos | Burke (2002) | Justificar a combinação entre conhecimento de domínio, fuzzy, ranking e possíveis baselines. |
| Cold start | Yuan e Hernandez (2023) | Sustentar a motivação sobre usuários/produtos com poucas interações. |
| Lógica fuzzy | Jain e Gupta (2018); Karthik e Ganapathy (2021) | Justificar preferências graduais, incerteza e graus de pertinência. |
| Ontologias e conhecimento semântico | Guia, Silva e Bernardino (2019); Guo et al. (2022); Tarus, Niu e Mustafa (2018) | Justificar o uso de relações semânticas entre produto, categoria, ambiente e atributos. |
| Explicabilidade | Zhang e Chen (2020) | Sustentar a necessidade de recomendações explicáveis. |
| Dataset Amazon Reviews 2023 | Hou et al. (2024) | Justificar a base pública e a relação entre linguagem, itens, reviews e recomendação. |

### Correções bibliográficas realizadas

- Substituição de “Haw et al., 2024” por Guia, Silva e Bernardino (2019), pois o PDF local é `A Hybrid Ontology-Based Recommendation System in e-Commerce`.
- Substituição de “Yager, 2003” por Jain e Gupta (2018), pois o PDF local disponível é `Fuzzy Logic in Recommender Systems`.
- Atualização de “Hou et al., 2023” para Hou et al. (2024), conforme arXiv `2403.03952` e página oficial do Amazon Reviews 2023.
- Manutenção de Zhang e Chen (2020), validado por Crossref/DOI `10.1561/1500000066`, publicado em 11/03/2020 em Foundations and Trends in Information Retrieval.

Arquivos revisados:

- `investigacao_tcc_revisao_dataset.md`
- `investigacao_dataset.md`
- `outputs/Capitulo_1_Introducao.md`
- `outputs/Capitulo_1_Introducao.docx`

## Revisão da introdução

### Resultado

A introdução foi revisada e alinhada ao estado metodológico atual do projeto. O texto agora:

- Trata o Amazon Reviews 2023 - Home and Kitchen como base pública, sem afirmar que ele representa oficialmente produtos de luxo.
- Explica que o conceito de produto premium/luxo será uma construção operacional derivada de atributos observáveis.
- Cita categorias reais observadas no schema validado, evitando listas hipotéticas não comprovadas.
- Remove promessas fortes de API, vitrine ou captura real de comportamento como se já fossem escopo implementado.
- Mantém a proposta de protótipo avaliável, ranking Top-N, explicabilidade e comparação com baselines.
- Usa citações compatíveis com os PDFs e metadados conferidos.

O Word foi regenerado em:

- `outputs/Capitulo_1_Introducao.docx`

## Pontos para validação do orientador

- Confirmar se o recorte Home and Kitchen é aceito como base pública para simular o domínio de casa, cozinha, área gourmet e banheiro.
- Confirmar se `store` poderá ser usado como aproximação de marca/loja ou se deve ser tratado apenas como metadado auxiliar.
- Confirmar a regra metodológica para produtos sem `price`, já que quase metade da amostra analisada não possui preço.
- Confirmar se o orientador deseja incluir uma fonte seminal específica de lógica fuzzy, além de Jain e Gupta (2018), caso prefira uma base teórica mais clássica.
- Confirmar se algum artigo de “Haw et al., 2024” deve permanecer no referencial; no repositório atual, o PDF correspondente não está presente, então ele foi removido das citações principais.

## Mensagem pronta para envio ao orientador

Prezado(a) professor(a),

Encaminho uma atualização das atividades de TCC realizadas até o momento.

Concluí a revisão bibliográfica inicial e o levantamento de datasets, com escolha do Amazon Reviews 2023 - Home and Kitchen como base pública principal. A escolha foi acompanhada de validação do schema real dos arquivos oficiais de reviews e metadados, evitando assumir previamente campos como preço, marca, descrição, categoria ou rating. Também foi revisado o mapeamento entre o domínio da Kouzina Club e categorias observadas no dataset, com evidências reais extraídas de uma amostra dos metadados.

Também avancei no levantamento e leitura dos trabalhos relacionados, organizando as fontes por eixos: fundamentos de sistemas de recomendação, cold start, lógica fuzzy, ontologias, recomendação baseada em conhecimento, explicabilidade e Amazon Reviews 2023. Durante a revisão, corrigi inconsistências bibliográficas: substituí uma referência que não estava presente no repositório pelo artigo efetivamente disponível de Guia, Silva e Bernardino (2019), atualizei Hou et al. para 2024 e alinhei a base de lógica fuzzy ao capítulo de Jain e Gupta (2018).

Por fim, revisei a introdução do TCC. O texto foi ajustado para não afirmar que o dataset possui rótulo oficial de luxo/premium, para citar apenas categorias validadas no schema e para evitar promessas de implementação fora do escopo atual. A introdução agora está alinhada à proposta de um protótipo avaliável baseado em ontologias fuzzy, ranking Top-N, explicabilidade e comparação com baselines.

Ficam como pontos para validação: a aprovação do recorte Home and Kitchen, o uso de `store` como possível aproximação de marca/loja, a estratégia para produtos sem preço e a decisão sobre incluir uma fonte clássica adicional de lógica fuzzy.
