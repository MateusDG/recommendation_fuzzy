# Arquitetura inicial de agentes para recomendacao fuzzy

## 1. Objetivo do documento

Este documento define a arquitetura inicial, ainda sem implementacao de codigo definitivo, para o projeto de TCC **Sistema de Recomendacao Baseado em Ontologias Fuzzy para Comercio Eletronico**.

A proposta considera os arquivos de investigacao do projeto, a proposta de orientacao, o sumario preliminar, o mapa semantico gerado pelo Graphify e as diretrizes tecnicas da OpenAI sobre engenharia orientada a agentes. A intencao e criar uma base de projeto legivel, verificavel e evolutiva antes de programar o motor de recomendacao.

## 2. Principios de arquitetura

1. **Repositorio como fonte de verdade**

   Toda decisao metodologica, regra fuzzy, criterio de recorte do dataset, contrato de entrada e saida dos modulos e resultado experimental deve ser documentado no proprio repositorio. Isso evita depender de conhecimento externo disperso e torna o projeto legivel para humanos e agentes.

2. **Agentes com fronteiras pequenas e verificaveis**

   Cada agente deve ter uma responsabilidade clara, entradas e saidas declaradas e criterios de validacao. O sistema nao deve comecar como um unico bloco que "faz recomendacao"; ele deve ser dividido em etapas auditaveis.

3. **Dados validados nas bordas**

   Os campos do Amazon Reviews 2023 devem ser tratados como hipotese ate a validacao no arquivo real. Nenhum agente deve assumir que campos como preco, marca, descricao ou categoria existem sem checagem anterior.

4. **Ontologia e fuzzy como nucleo interpretavel**

   O diferencial do TCC nao e apenas obter ranking Top-N. O sistema deve explicar por que um item foi recomendado, ligando perfil do usuario, atributos do produto, relacoes ontologicas e graus de pertinencia fuzzy.

5. **Prototipo primeiro, escalabilidade depois**

   O primeiro prototipo deve usar um recorte controlado de Home and Kitchen, com foco em cozinha, area gourmet, eletrodomesticos, cafe, utensilios premium e banheiro. A estrutura deve permitir crescimento, mas a validacao inicial precisa ser pequena o bastante para ser compreendida e medida.

6. **Reprodutibilidade experimental**

   Toda etapa experimental deve ser reproduzivel: versao do dataset, filtros aplicados, amostras, parametros fuzzy, baselines, metricas e sementes aleatorias devem ser registrados.

## 3. Visao geral da arquitetura

O sistema sera organizado como um pipeline de agentes especializados. Cada agente executa uma parte do processo e gera artefatos intermediarios que podem ser inspecionados.

```text
Dataset bruto
  -> Agente de Ingestao e Validacao
  -> Agente de Curadoria de Dominio
  -> Agente de Ontologia de Produtos
  -> Agente de Perfil Fuzzy do Usuario
  -> Agente de Inferencia Fuzzy
  -> Agente Recomendador Top-N
  -> Agente de Explicabilidade
  -> Agente de Avaliacao Experimental
```

Havera tambem agentes de suporte para governanca metodologica, experimentos, documentacao e comparacao com baselines.

## 4. Definicao dos agentes

### 4.1 Agente Orquestrador de Recomendacao

**Funcao:** coordenar a execucao dos demais agentes em uma ordem controlada.

**Responsabilidades:**

- Receber uma solicitacao de experimento ou recomendacao.
- Verificar se os artefatos necessarios ja existem: dataset curado, ontologia, perfis de usuario, regras fuzzy e configuracao experimental.
- Acionar os agentes na ordem correta.
- Registrar metadados de execucao.
- Impedir que recomendacoes sejam geradas com dados incompletos ou inconsistentes.

**Entradas principais:**

- Configuracao do experimento.
- Caminhos dos dados preparados.
- Parametros de recomendacao, como `top_k`, cenario de cold start e baseline desejado.

**Saidas principais:**

- Execucao coordenada.
- Relatorio tecnico da execucao.
- Ponte entre pipeline de dados, motor fuzzy e avaliacao.

### 4.2 Agente de Ingestao e Validacao de Dados

**Funcao:** carregar e validar os dados brutos do Amazon Reviews 2023 - Home and Kitchen.

**Responsabilidades:**

- Confirmar a estrutura real dos arquivos do dataset.
- Validar presenca, tipo e qualidade minima dos campos.
- Separar dados de produtos, reviews, usuarios e interacoes.
- Detectar campos ausentes relevantes para o TCC, como preco, marca, categorias, descricao, rating e numero de reviews.
- Gerar um relatorio de qualidade dos dados antes de qualquer transformacao semantica.

**Entradas principais:**

- Arquivos brutos do Amazon Reviews 2023.
- Documentacao local do dataset.
- Configuracao de schema esperado.

**Saidas principais:**

- Dados validados em formato intermediario.
- Relatorio de campos disponiveis e ausentes.
- Lista de problemas: duplicatas, valores nulos, categorias vazias, ratings invalidos, produtos sem metadados e usuarios sem historico minimo.

**Relacao com os datasets investigados:**

Este agente materializa a primeira decisao metodologica do projeto: usar Amazon Reviews 2023 - Home and Kitchen como dataset principal, mas sem assumir que ele representa diretamente luxo/premium. Essa caracteristica sera derivada posteriormente.

### 4.3 Agente de Curadoria de Dominio Kouzina-Amazon

**Funcao:** criar o recorte tematico alinhado ao dominio da Kouzina Club.

**Responsabilidades:**

- Filtrar produtos de Home and Kitchen associados a cozinha, area gourmet, eletrodomesticos, cafe, jantar, utensilios premium, decoracao funcional e banheiro.
- Mapear categorias reais ou esperadas da Kouzina para categorias do Amazon Reviews.
- Classificar categorias por relevancia para o TCC: alta, media-alta, media ou baixa.
- Registrar os termos usados para filtragem, como `kitchen`, `coffee`, `espresso`, `cookware`, `gourmet`, `bath`, `bathroom`, `premium`, `luxury`, `stainless steel` e equivalentes.
- Evitar que "premium" dependa apenas da presenca literal de palavras como `luxury` ou `premium`.

**Entradas principais:**

- Dados validados.
- Tabela Kouzina -> Amazon a ser criada.
- Lista de termos e categorias prioritarias.

**Saidas principais:**

- Dataset curado do dominio.
- Tabela de mapeamento de categorias.
- Justificativa metodologica do recorte.

**Interacao com outros agentes:**

- Fornece produtos candidatos ao Agente de Ontologia.
- Fornece criterios de dominio ao Agente de Compatibilidade Premium.
- Fornece evidencias para a escrita da metodologia.

### 4.4 Agente de Caracterizacao Premium

**Funcao:** calcular uma representacao operacional de produto premium/luxo.

**Responsabilidades:**

- Transformar o conceito subjetivo de produto premium em variaveis observaveis.
- Calcular indicadores como preco relativo dentro da categoria, avaliacao media, popularidade, marca, categoria de maior valor agregado e termos de qualidade/acabamento.
- Produzir um `grau_premium` ou conjunto fuzzy equivalente.
- Registrar a justificativa de cada criterio.

**Entradas principais:**

- Produtos curados.
- Estatisticas por categoria.
- Dicionario inicial de termos associados a design, acabamento, material e sofisticacao.

**Saidas principais:**

- Produto enriquecido com grau de pertinencia premium.
- Relatorio dos criterios utilizados.
- Alertas de baixa confianca quando dados como preco ou marca estiverem ausentes.

**Observacao metodologica:**

Este agente e central para o TCC porque evita afirmar que o dataset rotula oficialmente produtos como luxo. O sistema apenas aproxima esse conceito por criterios mensuraveis.

### 4.5 Agente de Ontologia de Produtos

**Funcao:** construir a representacao semantica do dominio.

**Responsabilidades:**

- Representar classes como Usuario, Produto, Categoria, Subcategoria, Ambiente, Marca, Faixa de Preco, Avaliacao, Review, Atributo, Material, Estilo, Funcao, Preferencia, Perfil e Recomendacao.
- Representar relacoes como `pertenceA`, `possuiMarca`, `indicadoParaAmbiente`, `possuiMaterial`, `possuiFuncao`, `similarA`, `compativelComPerfil` e `avaliadoPor`.
- Mapear categorias para ambientes: cozinha, area gourmet, sala de jantar, banheiro, area externa gourmet e organizacao da casa.
- Expor uma estrutura consultavel pelo motor de recomendacao.

**Entradas principais:**

- Dataset curado.
- Mapeamento Kouzina-Amazon.
- Regras de dominio.
- Atributos extraidos de titulo, descricao, categorias e metadados.

**Saidas principais:**

- Ontologia inicial em formato simples e versionavel.
- Grafo ou estrutura tabular de entidades e relacoes.
- Relatorio de cobertura: quantos produtos possuem categoria, ambiente, marca, atributos e grau premium.

**Decisao inicial recomendada:**

Comecar com uma ontologia serializada em JSON ou tabelas relacionais simples. RDF/OWL pode ser avaliado depois, caso agregue valor para a monografia. Para o primeiro prototipo, clareza e auditabilidade sao mais importantes que complexidade semantica.

### 4.6 Agente de Perfil Fuzzy do Usuario

**Funcao:** transformar interacoes historicas em preferencias graduais.

**Responsabilidades:**

- Identificar interacoes positivas, negativas e neutras.
- Inferir preferencias por categoria, ambiente, marca, faixa de preco, popularidade e perfil premium.
- Criar variaveis fuzzy de usuario, como afinidade com categoria, afinidade com ambiente, sensibilidade a preco e valorizacao de produto premium.
- Tratar cenarios de cold start com historico reduzido.

**Entradas principais:**

- Reviews e ratings.
- Produtos enriquecidos pela ontologia.
- Regras de interpretacao de rating.

**Saidas principais:**

- Perfil fuzzy por usuario.
- Nivel de confianca do perfil.
- Classificacao de cenario: cold start extremo, cold start moderado, usuario parcialmente conhecido ou usuario com historico suficiente.

**Regra inicial sugerida para rating:**

- Ratings 4 e 5: interacao positiva.
- Ratings 1 e 2: interacao negativa.
- Rating 3: neutro ou descartado, dependendo do desenho experimental.

### 4.7 Agente de Inferencia Fuzzy

**Funcao:** aplicar regras fuzzy para calcular compatibilidade entre usuario e produto.

**Responsabilidades:**

- Definir funcoes de pertinencia para preco, avaliacao, popularidade, afinidade de categoria, afinidade de ambiente, compatibilidade premium, confianca e compatibilidade geral.
- Aplicar regras fuzzy interpretaveis.
- Gerar escores intermediarios e escore final.
- Preservar rastreabilidade das regras que influenciaram cada recomendacao.

**Entradas principais:**

- Perfil fuzzy do usuario.
- Produto enriquecido pela ontologia.
- Grau premium.
- Configuracao das regras fuzzy.

**Saidas principais:**

- Escore fuzzy usuario-produto.
- Regras ativadas.
- Contribuicoes parciais para explicabilidade.

**Exemplos de regras candidatas:**

- Se o usuario tem alta afinidade com cozinha, o produto e de cozinha e possui avaliacao excelente, entao a compatibilidade e alta.
- Se o produto e premium e a confianca no perfil do usuario e baixa, entao a prioridade deve ser moderada.
- Se o usuario esta em cold start e o produto e semanticamente proximo da primeira interacao positiva, entao a recomendacao pode ter prioridade moderada.

### 4.8 Agente Recomendador Top-N

**Funcao:** gerar rankings finais de recomendacao.

**Responsabilidades:**

- Receber escores fuzzy e produzir listas Top-N.
- Remover produtos ja consumidos ou avaliados pelo usuario, quando apropriado.
- Aplicar criterios de desempate, como avaliacao media, popularidade, diversidade de categorias ou cobertura.
- Permitir recomendacoes por cenario: geral, cold start de usuario e cold start de item.

**Entradas principais:**

- Escores usuario-produto.
- Lista de produtos elegiveis.
- Parametros `top_k`, filtros de categoria e cenario experimental.

**Saidas principais:**

- Ranking Top-N.
- Lista de produtos recomendados por usuario.
- Metadados para avaliacao e explicacao.

### 4.9 Agente de Explicabilidade

**Funcao:** gerar justificativas compreensiveis para as recomendacoes.

**Responsabilidades:**

- Traduzir regras fuzzy ativadas em explicacoes textuais.
- Associar recomendacoes aos elementos da ontologia: categoria, ambiente, marca, preco, avaliacao, popularidade, premium e similaridade.
- Indicar quando a recomendacao tem baixa confianca.
- Registrar explicacoes para analise qualitativa no TCC.

**Entradas principais:**

- Ranking Top-N.
- Escores parciais.
- Regras ativadas.
- Dados ontologicos dos produtos.

**Saidas principais:**

- Explicacao por item recomendado.
- Percentual de recomendacoes com explicacao.
- Exemplos qualitativos para a secao de resultados.

### 4.10 Agente de Baselines

**Funcao:** gerar recomendacoes comparativas com metodos tradicionais ou simples.

**Responsabilidades:**

- Implementar baseline por popularidade.
- Implementar baseline content-based simples.
- Implementar baseline por categoria preferida.
- Preparar, em etapa posterior, filtragem colaborativa simples como user-kNN, item-kNN ou SVD, se o tempo do projeto permitir.
- Garantir que todos os baselines usem o mesmo split experimental do modelo fuzzy.

**Entradas principais:**

- Dataset curado.
- Interacoes usuario-produto.
- Configuracao de experimento.

**Saidas principais:**

- Rankings Top-N dos baselines.
- Artefatos comparaveis com o modelo proposto.

### 4.11 Agente de Avaliacao Experimental

**Funcao:** medir o desempenho do modelo fuzzy e dos baselines.

**Responsabilidades:**

- Criar splits de treino/teste.
- Simular cold start de usuario e de item.
- Calcular Precision@5, Precision@10, Recall@5, Recall@10, NDCG@10, Hit Rate@10 e Coverage.
- Gerar tabelas de resultados.
- Comparar modelo fuzzy, popularidade, content-based, categoria preferida e filtragem colaborativa quando disponivel.

**Entradas principais:**

- Recomendacoes do modelo fuzzy.
- Recomendacoes dos baselines.
- Conjunto de teste.
- Definicao de relevancia.

**Saidas principais:**

- Resultados quantitativos.
- Comparacao por cenario.
- Indicadores de cobertura e explicabilidade.

### 4.12 Agente de Governanca Metodologica

**Funcao:** proteger a coerencia academica e tecnica do projeto.

**Responsabilidades:**

- Verificar se cada decisao tecnica esta associada a uma justificativa metodologica.
- Manter uma matriz de decisoes: dataset, recorte, variaveis fuzzy, regras, baselines e metricas.
- Sinalizar lacunas entre a proposta, o sumario, a revisao bibliografica e a implementacao.
- Garantir que o prototipo responda ao problema central: recomendacao em e-commerce com baixa quantidade de dados e preferencias graduais.

**Entradas principais:**

- Documentacao do projeto.
- Resultados de experimentos.
- Decisoes tecnicas.

**Saidas principais:**

- Relatorio de coerencia.
- Checklist de metodologia.
- Itens pendentes para escrita do TCC.

### 4.13 Agente de Documentacao e Conhecimento do Repositorio

**Funcao:** manter o projeto legivel para humanos e agentes.

**Responsabilidades:**

- Atualizar documentos de arquitetura, metodologia, experimentos e decisoes.
- Manter um indice de documentos relevantes.
- Registrar mudancas no pipeline e nos contratos dos agentes.
- Evitar que regras importantes fiquem apenas em prompts, conversas ou memoria externa.

**Entradas principais:**

- Alteracoes de arquitetura.
- Resultados de validacao.
- Novas decisoes do orientador ou do aluno.

**Saidas principais:**

- Documentacao versionada.
- Registro de decisoes.
- Checklist de revisao para novas alteracoes.

## 5. Interacao entre os agentes

### 5.1 Fluxo principal de preparacao dos dados

1. O Agente de Ingestao valida os arquivos brutos.
2. O Agente de Curadoria aplica o recorte Kouzina-Amazon.
3. O Agente de Caracterizacao Premium calcula indicadores de produto premium.
4. O Agente de Ontologia transforma produtos e atributos em entidades e relacoes.
5. O Agente de Governanca verifica se o recorte e as regras estao documentados.

### 5.2 Fluxo principal de recomendacao

1. O Agente Orquestrador recebe o usuario ou experimento.
2. O Agente de Perfil Fuzzy constroi ou recupera o perfil do usuario.
3. O Agente de Inferencia Fuzzy calcula compatibilidade usuario-produto.
4. O Agente Recomendador Top-N monta o ranking.
5. O Agente de Explicabilidade gera justificativas por recomendacao.

### 5.3 Fluxo principal de avaliacao

1. O Agente de Avaliacao define splits e cenarios.
2. O Agente Orquestrador executa o modelo fuzzy.
3. O Agente de Baselines executa metodos comparativos.
4. O Agente de Avaliacao calcula metricas.
5. O Agente de Governanca verifica se os resultados respondem aos objetivos do TCC.
6. O Agente de Documentacao registra tabelas, parametros e conclusoes.

## 6. Artefatos principais

| Artefato | Responsavel | Objetivo |
| --- | --- | --- |
| Relatorio de validacao do dataset | Agente de Ingestao | Confirmar campos, qualidade e limitacoes dos dados |
| Tabela Kouzina -> Amazon | Agente de Curadoria | Justificar o recorte do dataset |
| Dataset curado | Agente de Curadoria | Base limpa para ontologia e recomendacao |
| Indicadores premium | Agente de Caracterizacao Premium | Operacionalizar produto premium/luxo |
| Ontologia inicial | Agente de Ontologia | Representar dominio, classes e relacoes |
| Perfis fuzzy de usuario | Agente de Perfil Fuzzy | Representar preferencias graduais |
| Regras fuzzy versionadas | Agente de Inferencia Fuzzy | Manter inferencia interpretavel |
| Rankings Top-N | Agente Recomendador | Gerar recomendacoes |
| Explicacoes de recomendacao | Agente de Explicabilidade | Apoiar interpretabilidade e analise qualitativa |
| Resultados experimentais | Agente de Avaliacao | Comparar modelo proposto e baselines |
| Registro de decisoes | Agente de Governanca | Preservar coerencia academica |

## 7. Estrutura de diretorios proposta

A estrutura abaixo e uma proposta inicial. Ela organiza o projeto para crescer sem misturar dados brutos, codigo, experimentos, documentacao e artefatos academicos.

```text
recommendation_fuzzy/
  README.md
  arquitetura_agentes.md
  AGENTS.md

  docs/
    architecture/
      sistema.md
      agentes.md
      fluxo_dados.md
    methodology/
      dataset.md
      recorte_kouzina_amazon.md
      variaveis_fuzzy.md
      regras_fuzzy.md
      avaliacao.md
    decisions/
      ADR-0001-dataset-amazon-home-kitchen.md
      ADR-0002-ontologia-inicial.md
      ADR-0003-metricas-top-n.md
    literature/
      matriz_fichamento.md
      referencias_preliminares.md

  data/
    raw/
      amazon_reviews_2023/
    interim/
      validated/
      filtered/
    processed/
      products_curated/
      interactions/
      ontology/
      user_profiles/
    samples/
      prototype/

  configs/
    dataset/
      schema_expected.yaml
      filters_home_kitchen.yaml
      kouzina_mapping.yaml
    fuzzy/
      membership_functions.yaml
      rules.yaml
    experiments/
      prototype.yaml
      cold_start_user.yaml
      cold_start_item.yaml

  src/
    agents/
      orchestrator/
      data_ingestion/
      domain_curator/
      premium_characterizer/
      ontology_builder/
      user_profile/
      fuzzy_inference/
      recommender/
      explainer/
      baselines/
      evaluator/
      governance/
    domain/
      entities/
      schemas/
      value_objects/
    services/
      recommendation/
      evaluation/
    repositories/
      datasets/
      artifacts/
    utils/

  tests/
    unit/
      agents/
      domain/
    integration/
      pipeline/
    fixtures/
      small_catalog/
      small_interactions/

  experiments/
    notebooks/
    runs/
    reports/
    figures/

  scripts/
    data/
    experiments/

  outputs/
    recommendations/
    explanations/
    metrics/
    logs/

  raw/
    graphify-out/

  arquivos_tcc/
```

### 7.1 Observacoes sobre a estrutura

- `data/raw/` deve conter dados brutos imutaveis.
- `data/interim/` deve conter transformacoes intermediarias ainda nao finais.
- `data/processed/` deve conter artefatos prontos para recomendacao e avaliacao.
- `configs/` deve concentrar parametros que mudam entre experimentos.
- `src/agents/` deve manter cada agente isolado por responsabilidade.
- `docs/decisions/` deve registrar decisoes arquiteturais e metodologicas.
- `tests/fixtures/` deve conter pequenos dados artificiais para validar regras sem depender do dataset completo.
- `outputs/` deve conter resultados gerados, preferencialmente ignorados pelo Git quando forem grandes ou reproduziveis.
- `AGENTS.md` deve ser curto e pratico, servindo como mapa para agentes de desenvolvimento, nao como manual gigante.

## 8. Contratos iniciais entre agentes

Antes de programar, cada agente deve ter um contrato documentado com:

- Objetivo.
- Entradas obrigatorias.
- Entradas opcionais.
- Saidas.
- Erros esperados.
- Criterios de qualidade.
- Exemplos minimos.

### 8.1 Exemplo de contrato conceitual

```text
Agente: Perfil Fuzzy do Usuario
Entrada:
  - interacoes_usuario
  - produtos_enriquecidos
  - configuracao_fuzzy
Saida:
  - perfil_usuario
  - nivel_confianca
  - cenario_cold_start
Criterios de qualidade:
  - nao criar perfil sem ao menos uma interacao valida
  - registrar quando rating 3 for descartado
  - explicar como cada preferencia foi calculada
```

Este formato deve ser repetido para todos os agentes antes da implementacao.

## 9. Prioridades para o primeiro prototipo funcional

### Prioridade 1 - Validacao real do dataset

O primeiro modulo a focar deve ser a validacao do Amazon Reviews 2023 - Home and Kitchen. Sem isso, toda regra sobre preco, marca, categoria e descricao fica especulativa.

**Resultado esperado:**

- Relatorio dos campos reais.
- Quantidade de produtos, usuarios e reviews disponiveis.
- Percentual de valores ausentes por campo.
- Confirmacao do que pode ou nao ser usado como variavel fuzzy.

### Prioridade 2 - Recorte Kouzina-Amazon

Depois da validacao, o foco deve ser construir a tabela de mapeamento entre categorias da Kouzina e categorias do Amazon Reviews.

**Resultado esperado:**

- 10 a 20 categorias mapeadas.
- Ambientes associados.
- Relevancia para o TCC.
- Termos de filtragem versionados.

### Prioridade 3 - Dataset pequeno de prototipo

Criar uma amostra controlada para desenvolvimento inicial.

**Resultado esperado:**

- Conjunto pequeno de produtos e interacoes.
- Dados suficientes para testar usuario conhecido, cold start de usuario e cold start de item.
- Fixture pequena para testes automatizados.

### Prioridade 4 - Ontologia inicial simples

Modelar classes e relacoes essenciais sem ainda buscar complexidade OWL/RDF.

**Resultado esperado:**

- Produto, Categoria, Ambiente, Marca, Faixa de Preco, Avaliacao, Atributo e Usuario.
- Relacoes basicas entre produto, categoria, ambiente e perfil.
- Cobertura medida por produto.

### Prioridade 5 - Variaveis e regras fuzzy minimas

Definir um conjunto inicial pequeno e interpretavel.

**Resultado esperado:**

- Variaveis: preco, avaliacao, popularidade, afinidade de categoria, afinidade de ambiente, grau premium, confianca e compatibilidade geral.
- Regras suficientes para gerar recomendacoes explicaveis.
- Registro de parametros.

### Prioridade 6 - Recomendador Top-N e explicabilidade

Gerar recomendacoes com explicacoes antes de ampliar baselines.

**Resultado esperado:**

- Ranking Top-5 e Top-10 por usuario.
- Justificativa textual por recomendacao.
- Escores parciais rastreaveis.

### Prioridade 7 - Baselines e avaliacao

Somente depois do fluxo fuzzy minimo funcionar, implementar comparacoes.

**Resultado esperado:**

- Popularidade.
- Categoria preferida.
- Content-based simples.
- Precision@K, Recall@K, NDCG@10, Hit Rate@10 e Coverage.

## 10. O que nao deve ser feito agora

- Nao implementar motor fuzzy definitivo antes de validar o dataset.
- Nao assumir que todo produto tem preco, marca ou descricao.
- Nao modelar OWL/RDF complexo antes de provar que a ontologia simples resolve o prototipo.
- Nao misturar notebook exploratorio com codigo de producao.
- Nao avaliar o modelo sem baselines comparaveis.
- Nao usar "premium/luxo" como rotulo direto sem uma definicao operacional.
- Nao criar agentes genericos demais sem contrato claro de entrada e saida.

## 11. Proxima decisao recomendada

A proxima aprovacao deve ser sobre a seguinte sequencia:

1. Criar a documentacao de contratos dos agentes.
2. Criar `AGENTS.md` curto com orientacoes do repositorio.
3. Validar o schema real do Amazon Reviews 2023 - Home and Kitchen.
4. Montar a tabela Kouzina -> Amazon.
5. So entao iniciar os primeiros modulos de codigo.

## 12. Referencias consideradas

### Documentos locais

- `raw/graphify-out/GRAPH_REPORT.md`
- `investigacao_dataset.md`
- `investigacao_tcc_revisao_dataset.md`
- `arquivos_tcc/Sumario Mateus Diniz.docx`
- `arquivos_tcc/26-1 - Proposta de Orientacao de TCC - SI.pdf`
- `raw/graphify-out/converted/Cronograma de Tarefas TCC_d1ea91f9.md`

### Referencias tecnicas oficiais

- OpenAI. **Alavancando o Codex em um mundo centrado no agente**. Disponivel em: https://openai.com/pt-BR/index/harness-engineering/
- OpenAI Developers. **Best practices - Codex**. Disponivel em: https://developers.openai.com/codex/learn/best-practices
