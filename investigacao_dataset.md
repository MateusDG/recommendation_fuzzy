# INVESTIGAÇÃO DO DATASET PARA O TCC

> Documento de apoio para justificar a escolha, o recorte e o uso do dataset no TCC.

| Item                      | Definição                                                                       |
| ------------------------- | --------------------------------------------------------------------------------- |
| Tema                      | Sistema de Recomendação Baseado em Ontologias Fuzzy para Comércio Eletrônico  |
| Dataset principal         | Amazon Reviews 2023 — Home and Kitchen                                           |
| Domínio de aplicação   | Produtos premium/luxo para casa, cozinha, área gourmet e banheiro                |
| Próxima entrega sugerida | Justificativa do dataset, recorte Home and Kitchen e mapeamento Kouzina → Amazon |

---

## Sumário

- [10. Dataset escolhido para o TCC](#10-dataset-escolhido-para-o-tcc)
- [11. Comparação entre datasets candidatos](#11-comparação-entre-datasets-candidatos)
- [12. Como usar o Amazon Reviews 2023 no TCC](#12-como-usar-o-amazon-reviews-2023--home-and-kitchen-no-tcc)
- [13. Estratégia para simular cold start](#13-estratégia-para-simular-cold-start)
- [14. Baselines recomendados](#14-baselines-recomendados)
- [15. Métricas recomendadas](#15-métricas-recomendadas)
- [16. Plano de execução com o dataset](#16-plano-de-execução-com-o-dataset)
- [17. Estrutura sugerida para revisão](#17-estrutura-sugerida-para-a-seção-de-revisão-no-tcc)
- [18. Estrutura sugerida para metodologia](#18-estrutura-sugerida-para-a-seção-de-datasetsmetodologia)
- [19. Lacuna preliminar da pesquisa](#19-lacuna-preliminar-da-pesquisa)
- [20. Matriz de fichamento dos artigos](#20-matriz-de-fichamento-dos-artigos)
- [21. Referências preliminares](#21-referências-preliminares-para-validação)
- [22. Próximo micro-objetivo](#22-próximo-micro-objetivo)
- [23. Decisão atual](#23-decisão-atual)

---

## 10. Dataset escolhido para o TCC

### Dataset principal recomendado

**Amazon Reviews 2023 — Home and Kitchen**

### Justificativa da escolha

O dataset escolhido para o TCC será o **Amazon Reviews 2023**, com foco no subconjunto **Home and Kitchen**. Essa escolha é mais adequada ao contexto da Kouzina Club porque a empresa atua com produtos de alto padrão voltados a ambientes residenciais e gourmet, incluindo eletrodomésticos de luxo, produtos para cozinha, área gourmet e banheiro.

A proposta do TCC prevê o desenvolvimento de um sistema de recomendação para comércio eletrônico, combinando lógica fuzzy e ontologias para representar preferências graduais de usuários e conhecimento semântico sobre produtos. Nesse sentido, o domínio **Home and Kitchen** é apropriado porque permite modelar categorias, atributos, faixas de preço, marcas, avaliações e características de produtos que se aproximam do catálogo real da Kouzina.

A escolha também favorece a construção de uma ontologia de produtos mais rica do que um dataset genérico, pois o domínio de casa e cozinha permite representar relações como:

- Produto pertence a uma categoria.
- Produto é voltado a um ambiente específico.
- Produto possui faixa de preço.
- Produto possui avaliação média.
- Produto possui atributos técnicos.
- Produto possui características de acabamento, design ou funcionalidade.
- Usuário demonstra preferência por determinada categoria, marca, faixa de preço ou estilo.

A decisão metodológica fica, portanto, assim:

> O dataset Amazon Reviews 2023 — Home and Kitchen será utilizado como base pública para simular um ambiente de comércio eletrônico de produtos residenciais premium, com foco em itens associados a cozinha, área gourmet, eletrodomésticos, decoração funcional e banheiro.

---

## 12. Como usar o Amazon Reviews 2023 — Home and Kitchen no TCC

### 12.1 Objetivo do uso do dataset

O dataset será usado para simular um ambiente de recomendação em comércio eletrônico no domínio de produtos para casa, cozinha e ambientes gourmet. A partir dos dados de produtos, avaliações e interações, será possível construir perfis de usuários e recomendar itens com base em regras fuzzy e relações semânticas definidas em uma ontologia.

O foco não será apenas prever uma nota ou rating, mas gerar recomendações personalizadas considerando atributos como:

- Categoria do produto.
- Ambiente de uso.
- Faixa de preço.
- Avaliação média.
- Popularidade.
- Marca.
- Atributos textuais.
- Compatibilidade com preferências do usuário.
- Perfil premium/luxo do produto.

### 12.2 Recorte recomendado dentro de Home and Kitchen

Como o dataset pode ser grande e conter muitos tipos de produtos, recomenda-se fazer um recorte temático alinhado à Kouzina.

Categorias prioritárias para filtrar, caso estejam disponíveis nos metadados:

- Kitchen & Dining.
- Small Appliances.
- Coffee, Tea & Espresso.
- Cookware.
- Bakeware.
- Kitchen Utensils & Gadgets.
- Dining & Entertaining.
- Home Décor.
- Bath.
- Bathroom Accessories.
- Storage & Organization.
- Heating, Cooling & Air Quality, caso existam produtos residenciais premium.
- Appliances, caso o dataset apresente essa subcategoria ou relação.

Também podem ser usados termos de filtragem por título, descrição ou categoria, como:

```text
kitchen
cookware
coffee
espresso
oven
wine
gourmet
dining
bath
bathroom
faucet
shower
luxury
premium
stainless steel
designer
built-in
```

A filtragem final deve ser feita com cautela, porque termos como "luxury" e "premium" podem aparecer de forma inconsistente nos textos. Por isso, a noção de produto premium não deve depender apenas dessas palavras.

### 12.3 Definição operacional de "produto premium/luxo"

Como "luxo" é uma característica subjetiva, o TCC precisa transformá-la em critérios observáveis. Para fins experimentais, um produto pode ser tratado como mais próximo do perfil premium quando apresentar uma combinação de fatores como:

- Preço acima da média da categoria.
- Avaliação média alta.
- Número relevante de avaliações.
- Marca recorrente ou reconhecida no dataset.
- Descrição com atributos de qualidade, design, acabamento ou sofisticação.
- Materiais associados a maior valor percebido, como aço inox, vidro, madeira nobre, cerâmica, acabamento cromado, acabamento fosco, entre outros.
- Categoria associada a produtos de maior valor agregado, como cafeteiras, adegas, utensílios gourmet, equipamentos de cozinha, itens de banheiro premium ou organização sofisticada.

Essa definição não significa afirmar que o dataset classifica oficialmente os produtos como luxo. Trata-se de uma operacionalização metodológica, ou seja, uma forma de transformar um conceito abstrato em variáveis analisáveis.

### 12.4 Entidades principais da ontologia

A ontologia pode começar com as seguintes classes:

- Usuário.
- Produto.
- Categoria.
- Subcategoria.
- Ambiente.
- Marca.
- Faixa de preço.
- Avaliação.
- Review.
- Atributo do produto.
- Material.
- Estilo.
- Função.
- Preferência do usuário.
- Perfil do usuário.
- Recomendação.

No contexto da Kouzina, a classe **Ambiente** é especialmente importante, pois ajuda a diferenciar produtos voltados a:

- Cozinha.
- Área gourmet.
- Sala de jantar.
- Banheiro.
- Área externa gourmet.
- Lavanderia ou organização da casa, caso faça sentido no catálogo.

### 12.5 Relações possíveis da ontologia

Exemplos de relações ontológicas:

- Usuário avaliou Produto.
- Produto pertenceA Categoria.
- Produto possuiSubcategoria.
- Produto éIndicadoPara Ambiente.
- Produto possuiMarca.
- Produto possuiFaixaDePreço.
- Produto possuiAvaliaçãoMédia.
- Produto possuiAtributo.
- Produto possuiMaterial.
- Produto possuiEstilo.
- Produto possuiFunção.
- Usuário prefereCategoria.
- Usuário prefereAmbiente.
- Usuário prefereMarca.
- Usuário prefereFaixaDePreço.
- Usuário valorizaAvaliaçãoAlta.
- Usuário valorizaProdutoPremium.
- Produto éSimilarA Produto.
- Produto éCompatívelCom PerfilDoUsuário.

Essas relações permitem que a recomendação seja mais interpretável. Por exemplo, o sistema pode recomendar um produto não apenas porque ele é popular, mas porque ele pertence a uma categoria preferida pelo usuário, possui atributos compatíveis e se aproxima de uma faixa de preço ou estilo valorizado.

### 12.6 Variáveis fuzzy possíveis

A lógica fuzzy será usada para representar preferências graduais. Em vez de classificar um produto apenas como "adequado" ou "inadequado", o sistema pode calcular graus de compatibilidade.

| Variável fuzzy              | Conjuntos fuzzy possíveis       | Exemplo de interpretação                                        |
| ---------------------------- | -------------------------------- | ----------------------------------------------------------------- |
| Preço                       | baixo, médio, alto, premium     | Um produto pode ser parcialmente "alto" e parcialmente "premium"  |
| Avaliação média           | baixa, moderada, alta, excelente | Produtos com rating elevado recebem maior grau de pertinência    |
| Popularidade                 | baixa, média, alta              | Pode ser baseada no número de avaliações                       |
| Afinidade com categoria      | baixa, média, alta              | Mede se o usuário costuma interagir com aquela categoria         |
| Afinidade com ambiente       | baixa, média, alta              | Mede se o usuário prefere cozinha, gourmet, banheiro etc.        |
| Compatibilidade premium      | baixa, média, alta              | Mede aderência ao perfil de produto de luxo                      |
| Confiança da recomendação | baixa, média, alta              | Mede segurança da recomendação com base nos dados disponíveis |
| Compatibilidade geral        | baixa, média, alta              | Resultado final do motor fuzzy                                    |

### 12.7 Exemplos de regras fuzzy

**Exemplo 1 — produto premium para cozinha**

```text
SE o usuário possui alta afinidade com produtos de cozinha
E o produto possui preço premium
E o produto possui avaliação excelente
ENTÃO a compatibilidade do produto com o usuário é alta.
```

**Exemplo 2 — produto para área gourmet**

```text
SE o usuário possui alta preferência por área gourmet
E o produto pertence a uma categoria relacionada a dining, cookware ou coffee
E o produto possui popularidade média ou alta
ENTÃO a recomendação deve ter prioridade alta.
```

**Exemplo 3 — produto de banheiro premium**

```text
SE o usuário demonstra interesse por produtos de banheiro
E o produto possui atributos associados a acabamento premium
E o produto possui avaliação alta
ENTÃO a compatibilidade do produto com o usuário é alta.
```

**Exemplo 4 — cenário de cold start de usuário**

```text
SE o usuário possui poucas interações
E o produto pertence a uma categoria semanticamente próxima da primeira interação do usuário
E o produto possui avaliação alta
ENTÃO a recomendação deve ter prioridade moderada.
```

**Exemplo 5 — controle de risco em recomendação cara**

```text
SE o produto possui preço premium
E a confiança no perfil do usuário é baixa
ENTÃO a recomendação deve ter prioridade moderada, mesmo que a avaliação do produto seja alta.
```

Essa última regra é importante porque produtos de luxo geralmente têm maior valor financeiro. Portanto, recomendar um item caro sem confiança suficiente pode reduzir a qualidade percebida da recomendação.

---

## 13. Estratégia para simular cold start

O problema de cold start aparece quando há poucas informações sobre usuários ou produtos. A proposta do TCC considera esse desafio relevante, especialmente porque sistemas tradicionais de recomendação, como filtragem colaborativa, dependem bastante de histórico de interações.

### 13.1 Cold start de usuário

Para simular cold start de usuário, o histórico de interações pode ser reduzido artificialmente.

Exemplo de cenários:

| Cenário                           | Histórico disponível do usuário |
| ---------------------------------- | ---------------------------------- |
| Cold start extremo                 | 1 interação conhecida            |
| Cold start moderado                | 2 a 3 interações conhecidas      |
| Usuário parcialmente conhecido    | 4 a 5 interações conhecidas      |
| Usuário com histórico suficiente | Mais de 5 interações conhecidas  |

A avaliação pode comparar o desempenho do sistema fuzzy-ontológico nesses diferentes cenários.

### 13.2 Cold start de item

Para simular cold start de item, podem ser selecionados produtos com poucas avaliações ou ocultadas interações de determinados produtos.

Exemplo:

| Cenário             | Condição do produto               |
| -------------------- | ----------------------------------- |
| Item novo            | Produto com 1 a 3 avaliações      |
| Item pouco conhecido | Produto com 4 a 10 avaliações     |
| Item conhecido       | Produto com mais de 10 avaliações |

Nesse caso, a hipótese é que a ontologia ajude a recomendar produtos pouco avaliados porque considera atributos semânticos, categorias, ambiente, faixa de preço e similaridade com outros produtos.

### 13.3 Por que a ontologia fuzzy pode ajudar

A abordagem fuzzy-ontológica pode ser útil em cold start porque não depende exclusivamente da matriz usuário-item. Ela pode usar:

- Categoria do produto.
- Subcategoria.
- Ambiente de uso.
- Preço.
- Avaliação média.
- Número de avaliações.
- Atributos textuais.
- Similaridade semântica.
- Relação com produtos já avaliados.
- Preferências graduais inferidas do usuário.

Assim, mesmo com poucas interações, o sistema consegue gerar uma recomendação baseada em conhecimento de domínio.

---

## 14. Baselines recomendados

Para avaliar o sistema proposto, é necessário compará-lo com métodos simples e reconhecidos. A comparação ajuda a mostrar se a abordagem fuzzy-ontológica oferece ganho real.

### 14.1 Baseline 1 — Popularidade

Recomenda os produtos mais populares ou mais bem avaliados dentro do recorte escolhido.

Critérios possíveis:

- Maior número de avaliações.
- Maior rating médio.
- Combinação entre rating médio e quantidade de avaliações.

**Por que usar:** é um baseline simples e forte. Em e-commerce, produtos populares frequentemente têm bom desempenho inicial.

### 14.2 Baseline 2 — Content-based simples

Recomenda produtos semelhantes aos que o usuário avaliou positivamente, usando informações como:

- Categoria.
- Título.
- Descrição.
- Atributos.
- Marca.
- Palavras-chave.

**Por que usar:** é uma comparação justa, pois também utiliza dados de produto, mas sem necessariamente usar ontologia fuzzy.

### 14.3 Baseline 3 — Filtragem colaborativa

Pode ser implementada com:

- user-kNN.
- item-kNN.
- Fatoração de matriz.
- SVD ou abordagem equivalente.

**Por que usar:** a filtragem colaborativa representa uma abordagem tradicional e ajuda a testar a hipótese de que métodos baseados em conhecimento podem funcionar melhor em cenários de cold start.

### 14.4 Baseline 4 — Recomendação por categoria preferida

Recomenda produtos das categorias mais bem avaliadas pelo usuário.

Exemplo:

> Se o usuário avaliou positivamente produtos de Coffee & Espresso, o sistema recomenda outros produtos dessa categoria.

**Por que usar:** é um baseline intermediário entre popularidade e ontologia fuzzy. Ajuda a verificar se o ganho do modelo proposto vem apenas da categoria ou da combinação fuzzy-ontológica mais completa.

### 14.5 Modelo proposto — Ontologia fuzzy

O modelo proposto deve gerar recomendações com base em:

- Perfil do usuário.
- Ontologia de produtos.
- Categorias e subcategorias.
- Ambiente de uso.
- Faixa de preço.
- Atributos técnicos e textuais.
- Regras fuzzy.
- Graus de pertinência.
- Escore final de compatibilidade.

O diferencial esperado é combinar recomendação personalizada, conhecimento semântico e explicabilidade.

---

## 15. Métricas recomendadas

Como o TCC trata de recomendação em comércio eletrônico, o foco deve estar em recomendação Top-N, isto é, listas dos K produtos mais recomendados.

### 15.1 Métricas principais

| Métrica    | Função                                                                |
| ----------- | ----------------------------------------------------------------------- |
| Precision@K | Mede quantos produtos recomendados entre os K primeiros são relevantes |
| Recall@K    | Mede quantos produtos relevantes foram recuperados entre os K primeiros |
| NDCG@K      | Considera a posição dos itens relevantes no ranking                   |
| Hit Rate@K  | Verifica se pelo menos um item relevante apareceu na lista recomendada  |
| Coverage    | Mede a variedade de produtos que o sistema consegue recomendar          |

### 15.2 Métricas recomendadas para o TCC

Para manter o escopo viável, recomenda-se usar:

- Precision@5.
- Precision@10.
- Recall@5.
- Recall@10.
- NDCG@10.
- Hit Rate@10.
- Coverage.

### 15.3 Métrica complementar: explicabilidade

Como a abordagem usa ontologia e regras fuzzy, pode ser interessante registrar quantas recomendações conseguem ser acompanhadas de uma explicação.

Exemplo de explicação:

> Produto recomendado porque pertence à categoria Kitchen & Dining, possui avaliação alta, está em faixa de preço compatível com perfil premium e tem similaridade semântica com produtos avaliados positivamente pelo usuário.

Essa métrica não precisa ser estatística complexa. Pode ser apresentada como análise qualitativa ou como percentual de recomendações que possuem justificativa gerada pelo sistema.

---

## 16. Plano de execução com o dataset

### Etapa 1 — Validar a documentação do dataset

Antes de implementar, confirmar:

- Fonte oficial do Amazon Reviews 2023.
- Licença de uso.
- Estrutura dos arquivos.
- Campos disponíveis.
- Tamanho do subconjunto Home and Kitchen.
- Existência de reviews.
- Existência de metadados.
- Existência de categorias.
- Presença ou ausência de preço.
- Presença ou ausência de marca.
- Presença ou ausência de descrição e atributos.

Campos esperados devem ser tratados como hipótese até validação no arquivo real.

### Etapa 2 — Baixar apenas o recorte necessário

Não é recomendável começar com o dataset inteiro. O ideal é iniciar com uma amostra menor.

Recorte inicial sugerido:

- Categoria principal: Home and Kitchen.
- Foco em produtos relacionados a cozinha, área gourmet e banheiro.
- Remoção de categorias muito distantes, como cama, escritório ou decoração genérica, caso apareçam.
- Amostra com quantidade administrável de usuários, produtos e avaliações.

Uma estratégia viável para TCC:

> Selecionar produtos de Home and Kitchen cujo caminho de categoria, título ou descrição contenha termos ligados a cozinha, área gourmet, eletrodomésticos, café, jantar, utensílios ou banheiro.

### Etapa 3 — Limpeza dos dados

Remover ou tratar:

- Produtos sem categoria.
- Produtos sem metadados mínimos.
- Usuários sem histórico suficiente para avaliação.
- Reviews duplicadas.
- Produtos sem avaliação.
- Textos vazios.
- Categorias irrelevantes.
- Preços ausentes, caso preço seja usado como variável fuzzy.

Também será necessário definir o que conta como avaliação positiva.

Exemplo:

| Rating | Interpretação                                              |
| ------ | ------------------------------------------------------------ |
| 4 e 5  | Interação positiva                                         |
| 1 e 2  | Interação negativa                                         |
| 3      | Neutro ou descartado, dependendo da estratégia experimental |

### Etapa 4 — Criar o recorte premium

Como a Kouzina trabalha com produtos de luxo, é importante criar uma variável derivada chamada, por exemplo, `grau_premium`.

Critérios possíveis:

- Preço relativo dentro da categoria.
- Avaliação média.
- Quantidade de avaliações.
- Presença de termos associados a acabamento, design ou qualidade.
- Marca.
- Categoria de maior valor agregado.

Exemplo de regra inicial:

```text
Produto com preço acima do percentil 75 da categoria
E avaliação média maior ou igual a 4
PODE receber alto grau de pertinência ao conjunto "premium".
```

A regra deve ser ajustada após análise exploratória dos dados.

### Etapa 5 — Construir a ontologia inicial

A ontologia pode ser implementada inicialmente de forma simples, sem exigir uma ferramenta complexa.

Opções:

- Representação em RDF/OWL.
- Grafo em Python com NetworkX.
- Estrutura em JSON.
- Tabelas relacionais.
- Dicionários de classes, atributos e relações.

Para um TCC de graduação, uma versão inicial em grafo ou estrutura tabular pode ser suficiente, desde que a modelagem seja clara e justificada.

Exemplo simplificado:

| Campo           | Valor                                       |
| --------------- | ------------------------------------------- |
| Produto         | Cafeteira Espresso Premium                  |
| Categoria       | Coffee, Tea & Espresso                      |
| Ambiente        | Cozinha / Área Gourmet                     |
| Faixa de preço | Premium                                     |
| Avaliação     | Alta                                        |
| Atributos       | inox, automática, compacta, design moderno |

### Etapa 6 — Modelar o perfil fuzzy do usuário

O perfil do usuário pode ser construído a partir das interações positivas.

Exemplo de atributos do perfil:

- Preferência por categorias.
- Preferência por ambientes.
- Sensibilidade a preço.
- Preferência por produtos premium.
- Preferência por produtos populares.
- Preferência por marcas.
- Preferência por determinados atributos textuais.

Exemplo:

```text
Usuário A:
- Alta preferência por Coffee & Espresso.
- Média preferência por Cookware.
- Baixa sensibilidade a preço.
- Alta compatibilidade com produtos premium.
- Alta preferência por produtos bem avaliados.
```

### Etapa 7 — Gerar recomendações

Para cada usuário, o sistema deve calcular um escore de compatibilidade entre o perfil do usuário e cada produto candidato.

Esse escore pode combinar:

- Afinidade com categoria.
- Afinidade com ambiente.
- Adequação de preço.
- Grau premium.
- Avaliação média.
- Popularidade.
- Similaridade textual ou semântica.
- Regras fuzzy.

Exemplo de saída:

| Usuário | Produto recomendado            | Escore fuzzy | Explicação                                                             |
| -------- | ------------------------------ | -----------: | ------------------------------------------------------------------------ |
| U1       | Cafeteira Espresso Premium     |         0,87 | Alta afinidade com categoria, preço compatível e avaliação excelente |
| U1       | Conjunto de Panelas Inox       |         0,79 | Produto de cozinha premium similar a itens avaliados positivamente       |
| U1       | Acessório de Banheiro Premium |         0,63 | Compatibilidade moderada com ambiente e avaliação alta                 |

### Etapa 8 — Comparar com baselines

Comparar o modelo fuzzy-ontológico com:

- Popularidade.
- Content-based simples.
- Filtragem colaborativa.
- Categoria preferida.

A comparação deve ser feita em cenário geral e também em cenário de cold start.

### Etapa 9 — Analisar resultados

A análise final deve responder:

- O modelo fuzzy-ontológico superou os baselines?
- Em quais cenários ele teve melhor desempenho?
- O desempenho melhora em cold start?
- A ontologia aumentou a cobertura de recomendações?
- As recomendações ficaram mais explicáveis?
- Quais tipos de produto foram mais bem recomendados?
- Quais categorias tiveram baixo desempenho?
- Quais limitações apareceram no dataset?

---

## 17. Estrutura sugerida para a seção de revisão no TCC

```text
2. Fundamentação Teórica e Trabalhos Relacionados

2.1 Sistemas de recomendação em comércio eletrônico
2.2 Limitações dos sistemas tradicionais e problema de cold start
2.3 Recomendação baseada em conhecimento, ontologias e grafos
2.4 Lógica fuzzy e modelagem de preferências graduais
2.5 Ontologias fuzzy e perfis de usuário
2.6 Recomendação em e-commerce de produtos premium
2.7 Trabalhos relacionados em sistemas de recomendação para produtos de casa e cozinha
2.8 Síntese crítica e lacuna de pesquisa
```

A seção 2.6 é importante porque o domínio da Kouzina não é e-commerce genérico. A compra de produtos premium envolve fatores subjetivos como marca, design, material, ambiente de uso, percepção de qualidade e faixa de preço.

---

## 18. Estrutura sugerida para a seção de datasets/metodologia

```text
3. Metodologia

3.1 Caracterização da pesquisa
3.2 Dataset utilizado: Amazon Reviews 2023 — Home and Kitchen
3.3 Critérios de seleção e recorte dos produtos
3.4 Pré-processamento dos dados
3.5 Definição operacional de produto premium
3.6 Construção da ontologia de produtos
3.7 Modelagem fuzzy das preferências do usuário
3.8 Geração das recomendações
3.9 Baselines de comparação
3.10 Métricas de avaliação
3.11 Estratégia de avaliação em cold start
3.12 Limitações metodológicas
```

---

## 19. Lacuna preliminar da pesquisa

Uma formulação atualizada da lacuna pode ser:

> Embora a literatura apresente avanços em sistemas de recomendação baseados em ontologias, lógica fuzzy, grafos de conhecimento e estratégias para cold start, ainda há espaço para investigar abordagens híbridas aplicadas a e-commerces especializados em produtos premium para casa, cozinha, área gourmet e banheiro. Nesse domínio, a recomendação depende não apenas do histórico de interações, mas também de fatores semânticos e subjetivos, como ambiente de uso, categoria, marca, faixa de preço, avaliação, atributos técnicos, design e percepção de valor. Assim, o uso de ontologias fuzzy pode contribuir para representar preferências graduais e gerar recomendações mais interpretáveis em cenários com baixa quantidade de dados.

---

## 20. Matriz de fichamento dos artigos

Usar a seguinte tabela para cada artigo lido.

| Campo                           | Preencher                                                              |
| ------------------------------- | ---------------------------------------------------------------------- |
| Referência completa            | Autor, ano, título, periódico/evento, DOI ou URL                     |
| Tipo de estudo                  | Survey, revisão sistemática, artigo experimental, proposta de modelo |
| Problema tratado                | Cold start, fuzzy, ontologia, e-commerce, explicabilidade              |
| Objetivo                        | O que o artigo busca resolver                                          |
| Método                         | Técnica principal usada                                               |
| Dataset                         | Nome, domínio, tipo de dado                                           |
| Métricas                       | Precision, Recall, NDCG, RMSE, MAE, Coverage etc.                      |
| Resultados                      | Principais achados                                                     |
| Limitações                    | Pontos fracos ou lacunas                                               |
| Relação com o TCC             | Como ajuda no seu trabalho                                             |
| Aplicação ao domínio Kouzina | Como o artigo ajuda no contexto de produtos premium para casa/cozinha  |
| Citações úteis               | Trechos com página                                                    |
| Status                          | Baixado, lido parcialmente, fichado, descartado                        |

---

## 21. Referências preliminares para validação

Conferir todas as referências em bases acadêmicas antes de inserir na versão final do TCC. As referências abaixo são preliminares e devem ser normalizadas conforme ABNT após conferência dos dados completos.

- ADOMAVICIUS, Gediminas; TUZHILIN, Alexander. Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, v. 17, n. 6, p. 734-749, 2005.
- BOBADILLA, Jesús et al. Recommender systems survey. Knowledge-Based Systems, v. 46, p. 109-132, 2013.
- BURKE, Robin. Hybrid recommender systems: Survey and experiments. User Modeling and User-Adapted Interaction, v. 12, p. 331-370, 2002.
- FERREIRA-SATLER, M. et al. Fuzzy ontologies-based user profiles applied to enhance e-learning activities. Soft Computing, 2012.
- FERREIRA-SATLER, M. et al. Fuzzy Ontology-Based Approach for Automatic Construction of User Profiles. RSCTC, 2014.
- GUO, Qingyu et al. A Survey on Knowledge Graph-Based Recommender Systems. IEEE Transactions on Knowledge and Data Engineering, 2022.
- GUIA, Márcio; SILVA, Rodrigo Rocha; BERNARDINO, Jorge. A Hybrid Ontology-Based Recommendation System in e-Commerce. Algorithms, v. 12, n. 11, 2019.
- HOU, Y. et al. Bridging Language and Items for Retrieval and Recommendation. arXiv preprint arXiv:2403.03952, 2024.
- ISINKAYE, F. O.; FOLAJIMI, Y. O.; OJOKOH, B. A. Recommendation systems: Principles, methods and evaluation. Egyptian Informatics Journal, v. 16, n. 3, p. 261-273, 2015.
- KARTHIK, R. V.; GANAPATHY, S. A fuzzy recommendation system for predicting the customers interests using sentiment analysis and ontology in e-commerce. Applied Soft Computing, v. 108, p. 107396, 2021.
- TARUS, John K.; NIU, Zhendong; MUSTAFA, Ghazali. Knowledge-based recommendation: a review of ontology-based recommender systems for e-learning. Artificial Intelligence Review, 2018.
- WANG, Shoujin et al. A Survey on Session-based Recommender Systems. ACM Computing Surveys, 2021.
- JAIN, Amita; GUPTA, Charu. Fuzzy Logic in Recommender Systems. In: CASTILLO, O. et al. (org.). Fuzzy Logic Augmentation of Neural and Optimization Algorithms: Theoretical Aspects and Real Applications. Studies in Computational Intelligence, v. 749. Cham: Springer, 2018. DOI: 10.1007/978-3-319-71008-2_20.
- YUAN, H.; HERNANDEZ, A. A. User Cold Start Problem in Recommendation Systems: A Systematic Review. IEEE Access, v. 11, p. 136223-136238, 2023.
- ZHANG, Shuai et al. Deep Learning Based Recommender System: A Survey and New Perspectives. ACM Computing Surveys, 2019.
- ZHANG, Yongfeng; CHEN, Xu. Explainable Recommendation: A Survey and New Perspectives. Foundations and Trends in Information Retrieval, 2020.
- ZHANG, S. et al. Revisiting recommender systems: an investigative survey. Neural Computing and Applications, 2025.

---

## 22. Próximo micro-objetivo

O próximo passo concreto é validar o recorte do dataset Home and Kitchen com base no catálogo real da Kouzina.

### Tarefa prática

Criar uma tabela com 10 a 20 categorias reais da Kouzina e mapear cada uma para uma possível categoria do Amazon Reviews 2023 — Home and Kitchen.

Modelo:

| Categoria Kouzina   | Categoria equivalente no dataset   | Ambiente                | Relevância para o TCC |
| ------------------- | ---------------------------------- | ----------------------- | ---------------------- |
| Cafeteiras premium  | Coffee, Tea & Espresso             | Cozinha / Área gourmet | Alta                   |
| Fornos de embutir   | Kitchen Appliances / Appliances    | Cozinha                 | Alta                   |
| Adegas climatizadas | Wine / Kitchen Appliances          | Área gourmet           | Alta                   |
| Cooktops            | Kitchen Appliances                 | Cozinha                 | Alta                   |
| Torneiras premium   | Bath / Bathroom / Home Improvement | Banheiro / Cozinha      | Média-alta            |
| Cubas               | Bath / Bathroom                    | Banheiro / Cozinha      | Média                 |
| Panelas premium     | Cookware                           | Cozinha                 | Alta                   |
| Utensílios gourmet | Kitchen Utensils & Gadgets         | Cozinha / Área gourmet | Alta                   |

Essa tabela será importante para justificar que o dataset público escolhido representa, ainda que de forma aproximada, o domínio real da aplicação.

---

## 23. Decisão atual

**Dataset principal escolhido:** Amazon Reviews 2023 — Home and Kitchen.

**Domínio de aplicação:** produtos premium/luxo para casa, cozinha, área gourmet e banheiro.

**Justificativa resumida:** o dataset é mais compatível com a Kouzina Club porque permite representar produtos residenciais e de cozinha por meio de categorias, avaliações, reviews e metadados. Esses elementos podem ser usados para construir uma ontologia de produtos e um perfil fuzzy de usuário baseado em preferências graduais.

**Recorte recomendado:** priorizar produtos relacionados a cozinha, área gourmet, eletrodomésticos, utensílios premium, decoração funcional e banheiro.

**Atenção metodológica:** a noção de "luxo" não deve ser assumida diretamente pelo nome do dataset. Ela precisa ser modelada por critérios observáveis, como preço relativo, avaliação, marca, categoria, atributos textuais e percepção de qualidade.

**Próxima entrega sugerida ao orientador:** apresentar a escolha do dataset, justificar o recorte Home and Kitchen, mostrar a tabela de mapeamento Kouzina → Amazon e propor as primeiras variáveis fuzzy do modelo.

---

## Síntese final

O próximo micro-objetivo é montar a tabela **Categoria Kouzina → Categoria Amazon Reviews 2023**, porque ela vai sustentar a justificativa do dataset e orientar a ontologia inicial.
