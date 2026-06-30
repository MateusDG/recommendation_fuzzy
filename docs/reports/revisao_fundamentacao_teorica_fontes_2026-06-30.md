# Revisão da fundamentação teórica e das fontes

> Relatório histórico da primeira versão. A formatação atual foi revisada posteriormente conforme o `GUIA_TCC_2026.pdf`. Para a situação vigente, consulte `docs/reports/revisao_abnt_capitulos_1_2_2026-06-30.md`.

Data: 30/06/2026

Arquivos revisados:

- `outputs/Capitulo_2_Fundamentacao_Teorica.md`
- `outputs/Capitulo_2_Fundamentacao_Teorica.docx`

## Escopo da entrega

O texto corresponde à abertura do Capítulo 2 prevista em `arquivos_tcc/Sumario Mateus Diniz.docx`. O sumário solicita uma apresentação dos conceitos fundamentais em 1 a 2 páginas; as subseções 2.1 a 2.5 possuem estimativas próprias e não foram antecipadas integralmente nesta entrega.

## Auditoria das afirmações

| Conceito empregado | Fonte local conferida | Evidência usada | Situação |
| --- | --- | --- | --- |
| Finalidade dos sistemas de recomendação e redução da sobrecarga de informação | `raw/Recommendation-systems--Principles--methods-and-_2015_Egyptian-Informatics-J.pdf` | Resumo e introdução, página 1 do PDF | Adequada. |
| Recomendação baseada em conteúdo, colaborativa e híbrida | `raw/recommender-systems-survey-2005.pdf` | Classificação dos métodos, página 5 do PDF | Adequada. |
| Combinação de técnicas em sistemas híbridos | `raw/Hybrid_Recommender_Systems_Survey_and_Experiments.pdf` | Definição e finalidade da hibridização, páginas 1 e 6 do PDF | Adequada. |
| Limitações de conteúdo, filtragem colaborativa e cold start | `raw/Recommendation-systems--Principles--methods-and-_2015_Egyptian-Informatics-J.pdf` | Discussão de limitações, páginas 3 e 7 do PDF | Adequada. |
| Cold start de usuário e de item | `raw/User_Cold_Start_Problem_in_Recommendation_Systems_A_Systematic_Review.pdf` | Resumo e definições, páginas 1 e 2 do PDF | Adequada. |
| Grau de pertinência no intervalo de 0 a 1, preferência gradual e variáveis linguísticas | `raw/Fuzzy Logic in Recommender Systems.pdf` | Discussão de regras linguísticas e função de pertinência, páginas 3 e 14 do PDF | Adequada. |
| Ontologia como representação de usuários, itens e relações | `raw/A_Hybrid_Ontology-Based_Recommendation_System_in_e.pdf` | Fundamentação de recomendadores baseados em ontologia, página 2 do PDF | Adequada. |
| Conhecimento estruturado como apoio a recomendação e explicabilidade | `raw/A Survey on Knowledge Graph-Based.pdf` | Resumo e fundamentação, páginas 1 e 2 do PDF | Adequada, sem equiparar ontologia e grafo de conhecimento. |
| Integração de fuzzy, ontologia e recomendação em e-commerce | `raw/A fuzzy recommendation system for predicting the customers interests using sentiment analysis and ontology in e-commerce.pdf` | Resumo e contribuições, páginas 1 e 2 do PDF | Adequada. |

## Limites adotados

- O texto apresenta fundamentos e uma hipótese de solução; não declara que o protótipo já foi implementado ou validado.
- A hibridização é descrita como combinação de técnicas, sem prometer ganho automático de desempenho.
- Ontologias são tratadas como estrutura adicional de conhecimento, não como solução garantida para cold start.
- A lógica fuzzy é apresentada como forma de representar gradualidade e incerteza, sem definir funções de pertinência ou regras definitivas antes da etapa metodológica.
- O acervo local não contém uma fonte específica sobre APIs REST e arquiteturas SaaS. Por isso, a abertura apenas reconhece a dimensão arquitetural; afirmações técnicas detalhadas devem aguardar bibliografia própria para a subseção 2.5.
- O Amazon Reviews 2023 não é discutido nesta abertura porque pertence à metodologia e não aos conceitos gerais solicitados para esta seção.

## Validação do DOCX

- Paginação calculada pelo Microsoft Word: 2 páginas.
- Estrutura: 1 título e 7 parágrafos de corpo; 642 palavras no corpo pela auditoria textual.
- Distribuição: título e quatro parágrafos na página 1; três parágrafos na página 2.
- Página: A4, com margens superior/esquerda de 3 cm e inferior/direita de 2 cm.
- Tipografia: Times New Roman 12 em todos os parágrafos; título em negrito e centralizado; corpo justificado, com espaçamento 1,5 e recuo inicial de 1,25 cm.
- Correspondência: o texto extraído do DOCX coincide integralmente com o Markdown de origem.
- Citações: todas as oito combinações autor-data usadas possuem PDF correspondente no diretório `raw/`.
- Integridade: nenhum caractere de substituição, referência antiga, comentário ou alteração controlada foi encontrado.

## Limitação da revisão visual

O renderizador canônico `render_docx.py` foi executado no arquivo final, mas não gerou PNGs porque o executável LibreOffice/`soffice` não está disponível no ambiente. A abertura e a paginação pelo Microsoft Word foram concluídas, mas a inspeção visual por imagens não pôde ser realizada. Essa limitação não altera a auditoria estrutural e textual descrita acima.
