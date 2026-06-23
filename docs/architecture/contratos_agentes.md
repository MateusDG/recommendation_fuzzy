# Contratos conceituais dos agentes

Este documento define os contratos conceituais dos agentes principais do projeto. Ele ainda nao descreve implementacao definitiva; serve como referencia para orientar os proximos modulos, testes e validacoes.

Cada contrato deve ser mantido simples, verificavel e alinhado ao objetivo do TCC: desenvolver e avaliar um sistema de recomendacao baseado em ontologias fuzzy para comercio eletronico, com foco em produtos premium/luxo de casa, cozinha, area gourmet e banheiro.

## 1. Agente Orquestrador de Recomendacao

**Objetivo**

Coordenar a execucao do pipeline de recomendacao e avaliacao, garantindo que os agentes sejam acionados na ordem correta e que os artefatos necessarios existam antes de cada etapa.

**Entradas**

- Configuracao de experimento.
- Caminhos para dados validados, dados curados, ontologia, perfis e regras fuzzy.
- Parametros de execucao, como `top_k`, cenario de cold start e metodo de recomendacao.

**Saidas**

- Registro da execucao.
- Status de cada etapa do pipeline.
- Referencias para rankings, explicacoes e metricas geradas.

**Criterios de qualidade**

- Nao deve executar recomendacao sem dataset curado.
- Nao deve executar inferencia fuzzy sem regras fuzzy carregadas.
- Deve registrar parametros usados em cada execucao.
- Deve falhar de forma explicita quando um artefato obrigatorio estiver ausente.

## 2. Agente de Ingestao e Validacao de Dados

**Objetivo**

Carregar e validar os dados brutos do Amazon Reviews 2023 - Home and Kitchen antes de qualquer recorte, transformacao semantica ou modelagem fuzzy.

**Entradas**

- Arquivo bruto do dataset em formato suportado.
- Configuracao de schema esperado, quando existir.
- Limite de linhas/amostras para exploracao inicial.

**Saidas**

- Relatorio de colunas disponiveis.
- Tipos observados por coluna.
- Contagem de valores ausentes por coluna.
- Lista de inconsistencias encontradas.

**Criterios de qualidade**

- Deve tratar campos esperados como hipotese ate validacao real.
- Deve separar problemas de schema de problemas de qualidade de dados.
- Deve registrar campos ausentes relevantes para o TCC, como preco, marca, categoria, descricao, rating e identificadores.
- Deve operar em amostra sem exigir carregamento completo do dataset em memoria.

## 3. Agente de Curadoria de Dominio Kouzina-Amazon

**Objetivo**

Selecionar o recorte do dataset mais aderente ao dominio da Kouzina Club e justificar metodologicamente o mapeamento entre categorias reais do e-commerce e categorias do Amazon Reviews.

**Entradas**

- Dados validados.
- Tabela de mapeamento Kouzina -> Amazon.
- Lista de termos de busca e categorias prioritarias.

**Saidas**

- Dataset filtrado por dominio.
- Relatorio de categorias incluidas e excluidas.
- Justificativa do recorte usado.

**Criterios de qualidade**

- Deve manter os filtros versionados.
- Deve evitar dependencia exclusiva de termos como `premium` ou `luxury`.
- Deve registrar a relevancia de cada categoria para o TCC.
- Deve preservar rastreabilidade entre produto original e produto filtrado.

## 4. Agente de Caracterizacao Premium

**Objetivo**

Transformar o conceito subjetivo de produto premium/luxo em indicadores observaveis e, posteriormente, em um grau de pertinencia fuzzy.

**Entradas**

- Produtos curados.
- Estatisticas por categoria.
- Campos disponiveis de preco, avaliacao, popularidade, marca, titulo, descricao e atributos.
- Dicionario de termos associados a qualidade, design, acabamento e material.

**Saidas**

- Indicadores de premium por produto.
- Grau preliminar de aderencia ao perfil premium, quando os dados permitirem.
- Alertas de baixa confianca para produtos com dados insuficientes.

**Criterios de qualidade**

- Nao deve assumir que o dataset rotula oficialmente produtos como luxo.
- Deve distinguir regra metodologica de fato observado.
- Deve registrar quais criterios foram aplicados em cada produto.
- Deve indicar quando preco, marca ou descricao estiverem ausentes.

## 5. Agente de Ontologia de Produtos

**Objetivo**

Construir a representacao semantica inicial do dominio de produtos, categorias, ambientes, atributos e relacoes relevantes para a recomendacao.

**Entradas**

- Dataset curado.
- Mapeamento Kouzina -> Amazon.
- Indicadores premium.
- Regras de dominio para categorias, ambientes, materiais, funcoes e atributos.

**Saidas**

- Ontologia inicial em formato versionavel.
- Entidades de produto, categoria, ambiente, marca, faixa de preco, avaliacao, atributo e usuario.
- Relacoes como `pertenceA`, `possuiMarca`, `indicadoParaAmbiente`, `possuiAtributo`, `possuiFaixaDePreco`, `similarA` e `compativelComPerfil`.

**Criterios de qualidade**

- Deve permitir auditoria das relacoes geradas.
- Deve registrar cobertura da ontologia por campo.
- Deve comecar simples, preferencialmente com JSON, tabelas ou grafo leve.
- Nao deve introduzir complexidade OWL/RDF antes de validar valor no prototipo.

## 6. Agente de Perfil Fuzzy do Usuario

**Objetivo**

Converter interacoes historicas de usuarios em preferencias graduais representadas por variaveis fuzzy.

**Entradas**

- Interacoes usuario-produto.
- Ratings e reviews, quando disponiveis.
- Produtos enriquecidos pela ontologia.
- Regras de interpretacao de rating.

**Saidas**

- Perfil fuzzy por usuario.
- Nivel de confianca do perfil.
- Classificacao do usuario em cenario de cold start extremo, moderado, parcial ou historico suficiente.

**Criterios de qualidade**

- Deve registrar quais interacoes foram consideradas positivas, negativas ou neutras.
- Deve tratar rating 3 conforme decisao experimental documentada.
- Deve indicar baixa confianca em usuarios com poucas interacoes.
- Nao deve criar perfil completo a partir de dados insuficientes sem sinalizar incerteza.

## 7. Agente de Inferencia Fuzzy

**Objetivo**

Aplicar funcoes de pertinencia e regras fuzzy para calcular a compatibilidade entre usuario e produto.

**Entradas**

- Perfil fuzzy do usuario.
- Produto enriquecido pela ontologia.
- Configuracao de funcoes de pertinencia.
- Configuracao de regras fuzzy.

**Saidas**

- Escore fuzzy usuario-produto.
- Regras ativadas.
- Contribuicoes parciais para explicabilidade.

**Criterios de qualidade**

- Deve manter regras e parametros fora do codigo sempre que possivel.
- Deve gerar resultados rastreaveis.
- Deve preservar interpretabilidade dos escores.
- Deve sinalizar quando uma regra nao pode ser aplicada por falta de dado.

## 8. Agente Recomendador Top-N

**Objetivo**

Gerar rankings de recomendacao Top-N com base nos escores produzidos pelo motor fuzzy ou por baselines.

**Entradas**

- Escores usuario-produto.
- Produtos candidatos.
- Historico de produtos ja avaliados ou consumidos.
- Parametros `top_k`, filtros e criterios de desempate.

**Saidas**

- Ranking Top-N por usuario.
- Metadados de ranking.
- Lista de itens removidos por ja terem sido consumidos, quando aplicavel.

**Criterios de qualidade**

- Deve evitar recomendar item ja avaliado no conjunto de treino, quando essa for a regra experimental.
- Deve aplicar criterios de desempate documentados.
- Deve preservar a ordem final do ranking.
- Deve produzir saida comparavel entre modelo fuzzy e baselines.

## 9. Agente de Explicabilidade

**Objetivo**

Gerar justificativas legiveis para as recomendacoes, conectando regras fuzzy, perfil do usuario e atributos ontologicos do produto.

**Entradas**

- Ranking Top-N.
- Regras fuzzy ativadas.
- Escores parciais.
- Dados do produto e do perfil do usuario.

**Saidas**

- Explicacao textual por produto recomendado.
- Indicador de confianca ou limitacao da explicacao.
- Exemplos qualitativos para analise no TCC.

**Criterios de qualidade**

- Deve explicar a recomendacao sem inventar atributos ausentes.
- Deve indicar quando uma recomendacao tem baixa confianca.
- Deve associar justificativas a elementos verificaveis da ontologia.
- Deve permitir medir o percentual de recomendacoes explicaveis.

## 10. Agente de Baselines

**Objetivo**

Gerar recomendacoes comparativas usando metodos simples ou tradicionais para avaliar o ganho do modelo fuzzy-ontologico.

**Entradas**

- Dataset curado.
- Interacoes usuario-produto.
- Split experimental.
- Configuracao do baseline.

**Saidas**

- Rankings Top-N dos baselines.
- Metadados dos parametros usados.
- Artefatos comparaveis aos rankings do modelo proposto.

**Criterios de qualidade**

- Deve usar o mesmo split do modelo fuzzy.
- Deve registrar a regra de cada baseline.
- Deve comecar por popularidade, categoria preferida e content-based simples.
- Deve deixar filtragem colaborativa para etapa posterior, caso o escopo permita.

## 11. Agente de Avaliacao Experimental

**Objetivo**

Avaliar quantitativamente o modelo proposto e os baselines em cenarios gerais e de cold start.

**Entradas**

- Rankings do modelo fuzzy.
- Rankings dos baselines.
- Conjunto de teste.
- Definicao de relevancia.
- Parametros de metricas.

**Saidas**

- Precision@5 e Precision@10.
- Recall@5 e Recall@10.
- NDCG@10.
- Hit Rate@10.
- Coverage.
- Tabelas comparativas por cenario.

**Criterios de qualidade**

- Deve aplicar a mesma definicao de relevancia a todos os modelos.
- Deve separar avaliacao geral de avaliacao em cold start.
- Deve registrar parametros, sementes e amostras.
- Deve produzir resultados reproduziveis.

## 12. Agente de Governanca Metodologica

**Objetivo**

Garantir coerencia entre proposta de TCC, revisao bibliografica, dataset, modelagem fuzzy, ontologia, experimentos e escrita final.

**Entradas**

- Documentacao do projeto.
- Decisoes arquiteturais.
- Resultados de validacao e experimentos.
- Requisitos academicos do TCC.

**Saidas**

- Checklist de coerencia metodologica.
- Pendencias para escrita do TCC.
- Registro de decisoes e justificativas.

**Criterios de qualidade**

- Deve identificar decisoes tecnicas sem justificativa metodologica.
- Deve apontar divergencias entre proposta, sumario e implementacao.
- Deve manter o foco no problema de cold start, preferencias graduais e conhecimento semantico.
- Deve favorecer artefatos versionados no repositorio.

## 13. Agente de Documentacao e Conhecimento do Repositorio

**Objetivo**

Manter a base de conhecimento do projeto organizada, curta, versionada e util para humanos e agentes.

**Entradas**

- Novas decisoes do projeto.
- Mudancas em contratos, configs e resultados.
- Relatorios de validacao.

**Saidas**

- Documentacao atualizada.
- Indices e referencias cruzadas.
- Registros de alteracoes relevantes.

**Criterios de qualidade**

- Deve evitar documentacao longa e redundante.
- Deve manter documentos de arquitetura e metodologia alinhados ao codigo.
- Deve registrar informacoes que nao devem ficar apenas em conversas.
- Deve preservar legibilidade do repositorio para futuras execucoes de agentes.

