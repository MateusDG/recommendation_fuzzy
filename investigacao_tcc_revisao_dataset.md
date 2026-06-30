# Investigação inicial — Revisão bibliográfica e levantamento de datasets

**TCC:** Sistema de Recomendação Baseado em Ontologias Fuzzy para Comércio Eletrônico
**Aluno:** Mateus Diniz Gottardi
**Foco desta etapa:** Revisão bibliográfica, trabalhos relacionados e escolha inicial de dataset público.
**Data da organização:** 2026-06-23

---

## 1. Observação de transparência

Esta investigação foi organizada com base na proposta de TCC já anexada e em conhecimento acadêmico prévio. Não houve navegação web em tempo real nesta etapa. Portanto, antes de inserir qualquer nova referência no texto final do TCC, é necessário confirmar os metadados em bases acadêmicas como Google Scholar, IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, Scopus, Web of Science, Portal CAPES ou no site oficial do periódico/evento.

A lista abaixo evita fontes inventadas, mas alguns detalhes bibliográficos, como volume, número, páginas e DOI, devem ser conferidos antes da versão final.

---

## 2. Recorte do TCC para orientar a busca

O TCC propõe desenvolver e avaliar um sistema de recomendação híbrido para comércio eletrônico, baseado em:

- sistemas de recomendação;
- lógica fuzzy;
- ontologias;
- modelagem semântica de produtos;
- perfis de usuário;
- preferências graduais;
- cold start;
- datasets públicos;
- avaliação por métricas de recomendação.

A pergunta norteadora da revisão pode ser formulada assim:

> Como ontologias fuzzy podem ser usadas para modelar preferências graduais de usuários e melhorar recomendações em comércio eletrônico, especialmente em cenários de cold start e baixa quantidade de interações?

---

## 3. Objetivos desta etapa da investigação

### Objetivo geral da investigação bibliográfica

Mapear estudos, revisões e datasets públicos relevantes para fundamentar o desenvolvimento de um sistema de recomendação baseado em ontologias fuzzy aplicado a comércio eletrônico.

### Objetivos específicos

1. Identificar revisões bibliográficas e surveys recentes sobre sistemas de recomendação.
2. Levantar trabalhos sobre recomendação baseada em ontologias, grafos de conhecimento e semântica.
3. Levantar trabalhos sobre lógica fuzzy aplicada à modelagem de preferências.
4. Identificar trabalhos relacionados especificamente a e-commerce.
5. Selecionar um dataset público adequado ao contexto da Kouzina Club.
6. Definir critérios iniciais de avaliação experimental.

---

## 4. Núcleo de referências já presente na proposta

Estas referências já aparecem na proposta do TCC e devem ser tratadas como leitura obrigatória inicial.

| Prioridade | Referência                  | Papel no TCC                                                                                                                        |
| ---------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1          | KARTHIK; GANAPATHY, 2021     | Trabalho diretamente relacionado: sistema fuzzy com ontologia e análise de sentimento em e-commerce.                               |
| 2          | GUIA; SILVA; BERNARDINO, 2019 | Trabalho diretamente relacionado: sistema híbrido de recomendação baseado em ontologia para e-commerce. |
| 3          | YUAN; HERNANDEZ, 2023        | Revisão sistemática sobre cold start em sistemas de recomendação.                                                               |
| 4          | ZHANG et al., 2025           | Survey recente sobre sistemas de recomendação.                                                                                    |
| 5          | FERREIRA-SATLER et al., 2012 | Base conceitual para perfis de usuário baseados em ontologias fuzzy.                                                               |
| 6          | FERREIRA-SATLER et al., 2014 | Construção automática de perfis de usuário com ontologias fuzzy.                                                                |
| 7          | HOU et al., 2024             | Relação com itens, linguagem e recomendação; associado ao Amazon Reviews 2023 dataset.                                          |

---

## 5. Novas revisões, surveys e fontes relevantes para acrescentar

As fontes abaixo são candidatas fortes para ampliar a revisão bibliográfica. A recomendação é priorizar as mais recentes e as mais próximas do tema.

### 5.1 Recomendação baseada em conhecimento, ontologias e grafos

#### 1. Guo et al. — Survey on Knowledge Graph-Based Recommender Systems

**Referência preliminar:**
GUO, Qingyu et al. *A Survey on Knowledge Graph-Based Recommender Systems*. IEEE Transactions on Knowledge and Data Engineering, 2022.

**Por que acrescentar:**
É uma fonte muito relevante para conectar ontologias, conhecimento estruturado, relações semânticas e sistemas de recomendação. Embora o seu TCC fale em ontologias fuzzy, muitos trabalhos recentes migraram a discussão para grafos de conhecimento. Essa referência ajuda a posicionar sua proposta dentro de uma linha atual: sistemas de recomendação enriquecidos por conhecimento.

**Como usar no TCC:**
Pode fundamentar a seção sobre recomendação semântica e explicar por que relações entre produtos, categorias, atributos e usuários podem melhorar recomendações em comparação com métodos puramente colaborativos.

**Relação com o TCC:**
Alta. Serve para justificar o uso de conhecimento de domínio.

---

#### 2. Tarus, Niu e Mustafa — Ontology-based recommender systems

**Referência preliminar:**
TARUS, John K.; NIU, Zhendong; MUSTAFA, Ghazali. *Knowledge-based recommendation: a review of ontology-based recommender systems for e-learning*. Artificial Intelligence Review, 2018.

**Por que acrescentar:**
Apesar do domínio ser e-learning, a referência é útil porque discute recomendação baseada em ontologias e modelagem de perfis. Ela pode dialogar diretamente com os trabalhos de Ferreira-Satler et al. sobre perfis de usuário baseados em ontologias fuzzy.

**Como usar no TCC:**
Pode ser usada para explicar como ontologias apoiam sistemas de recomendação baseados em conhecimento, mesmo que o domínio de aplicação seja diferente.

**Relação com o TCC:**
Média-alta. A contribuição é conceitual, não diretamente e-commerce.

---

### 5.2 Sistemas de recomendação: surveys gerais e fundamentos

#### 3. Zhang et al. — Deep Learning Based Recommender System

**Referência preliminar:**
ZHANG, Shuai; YAO, Lina; SUN, Aixin; TAY, Yi. *Deep Learning Based Recommender System: A Survey and New Perspectives*. ACM Computing Surveys, 2019.

**Por que acrescentar:**
Ajuda a contextualizar os sistemas de recomendação modernos, especialmente aqueles baseados em aprendizado profundo. Mesmo que o TCC não use deep learning como técnica principal, essa referência ajuda a comparar a abordagem fuzzy-ontológica com modelos mais comuns na literatura recente.

**Como usar no TCC:**
Pode aparecer na fundamentação sobre evolução dos sistemas de recomendação e na justificativa de escolha por uma abordagem semântica e interpretável.

**Relação com o TCC:**
Média. Serve mais como contextualização e comparação.

---

#### 4. Isinkaye, Folajimi e Ojokoh — Principles, methods and evaluation

**Referência preliminar:**
ISINKAYE, F. O.; FOLAJIMI, Y. O.; OJOKOH, B. A. *Recommendation systems: Principles, methods and evaluation*. Egyptian Informatics Journal, 2015.

**Por que acrescentar:**
É uma referência introdutória e didática sobre métodos e avaliação de sistemas de recomendação. Útil para explicar filtragem colaborativa, baseada em conteúdo, híbrida e métricas de avaliação.

**Como usar no TCC:**
Pode apoiar a seção inicial sobre conceitos de sistemas de recomendação.

**Relação com o TCC:**
Média. É menos recente, mas boa para conceitos básicos.

---

#### 5. Bobadilla et al. — Recommender systems survey

**Referência preliminar:**
BOBADILLA, Jesús et al. *Recommender systems survey*. Knowledge-Based Systems, 2013.

**Por que acrescentar:**
Survey clássico sobre sistemas de recomendação. Embora mais antigo, é útil para apresentar fundamentos, limitações e classificações tradicionais.

**Como usar no TCC:**
Como base histórica e conceitual, sem depender dele como principal referência de estado da arte.

**Relação com o TCC:**
Média. Usar com moderação por ser anterior a muitos métodos atuais.

---

#### 6. Adomavicius e Tuzhilin — Next generation of recommender systems

**Referência preliminar:**
ADOMAVICIUS, Gediminas; TUZHILIN, Alexander. *Toward the Next Generation of Recommender Systems: A Survey of the State-of-the-Art and Possible Extensions*. IEEE Transactions on Knowledge and Data Engineering, 2005.

**Por que acrescentar:**
É uma referência seminal. Ajuda a explicar os fundamentos e as limitações dos sistemas tradicionais, além de contextualizar abordagens híbridas e contextuais.

**Como usar no TCC:**
Apenas como referência histórica/fundacional.

**Relação com o TCC:**
Média. Importante, mas não deve ser usada como evidência de estado da arte atual.

---

### 5.3 Cold start, sessões e baixa quantidade de dados

#### 7. Yuan e Hernandez — User cold start problem

**Referência já presente na proposta:**
YUAN, H.; HERNANDEZ, A. A. *User Cold Start Problem in Recommendation Systems: A Systematic Review*. IEEE Access, 2023.

**Por que manter como central:**
O problema de cold start aparece explicitamente na proposta. Essa referência deve fundamentar a justificativa de que métodos tradicionais, especialmente os baseados apenas em histórico de interações, têm limitações quando há poucos dados de usuários ou itens.

**Como usar no TCC:**
Na seção “Desafios em sistemas de recomendação”, especialmente para explicar cold start de usuário, cold start de item e estratégias de mitigação.

**Relação com o TCC:**
Muito alta.

---

#### 8. Wang et al. — Session-based recommender systems

**Referência preliminar:**
WANG, Shoujin et al. *A Survey on Session-based Recommender Systems*. ACM Computing Surveys, 2021.

**Por que acrescentar:**
Se a Kouzina Club tiver navegação por sessão, cliques, carrinho ou histórico recente de navegação, sistemas baseados em sessão podem ser relevantes. Mesmo que o TCC não implemente esse tipo de recomendação, a referência ajuda a diferenciar sua proposta de abordagens baseadas apenas em comportamento recente.

**Como usar no TCC:**
Pode aparecer como comparação: sistemas session-based dependem de sequências de comportamento, enquanto a ontologia fuzzy pode recomendar com base em atributos semânticos mesmo com pouco histórico.

**Relação com o TCC:**
Média. Alta apenas se houver dados de sessão no sistema real.

---

### 5.4 Explicabilidade e recomendação interpretável

#### 9. Zhang e Chen — Explainable recommendation

**Referência preliminar:**
ZHANG, Yongfeng; CHEN, Xu. *Explainable Recommendation: A Survey and New Perspectives*. Foundations and Trends in Information Retrieval, 2020.

**Por que acrescentar:**
Ontologias e regras fuzzy podem tornar o sistema mais explicável. Em vez de apenas recomendar “porque o modelo calculou”, o sistema pode justificar: “produto recomendado porque pertence à categoria preferida, tem avaliação alta e preço compatível com o perfil do usuário”.

**Como usar no TCC:**
Na justificativa de que sistemas baseados em conhecimento e fuzzy podem oferecer maior interpretabilidade do que modelos puramente colaborativos ou modelos de caixa-preta.

**Relação com o TCC:**
Alta.

---

### 5.5 Lógica fuzzy em recomendação

#### 10. Jain e Gupta — Fuzzy Logic in Recommender Systems

**Referência preliminar:**
JAIN, Amita; GUPTA, Charu. *Fuzzy Logic in Recommender Systems*. In: CASTILLO, O. et al. (org.). *Fuzzy Logic Augmentation of Neural and Optimization Algorithms: Theoretical Aspects and Real Applications*. Studies in Computational Intelligence, v. 749. Cham: Springer, 2018. DOI: 10.1007/978-3-319-71008-2_20.

**Por que acrescentar:**
É a fonte disponível no repositório para embasar a aplicação de lógica fuzzy em sistemas de recomendação. Ajuda a justificar a modelagem de preferências graduais, imprecisão e incerteza em perfis de usuário e atributos de itens.

**Como usar no TCC:**
Na seção sobre lógica fuzzy aplicada a recomendação, especialmente para explicar que preferências não precisam ser tratadas apenas como valores binários.

**Relação com o TCC:**
Alta como base conceitual.

---

### 5.6 Sistemas híbridos

#### 11. Burke — Hybrid recommender systems

**Referência preliminar:**
BURKE, Robin. *Hybrid Recommender Systems: Survey and Experiments*. User Modeling and User-Adapted Interaction, 2002.

**Por que acrescentar:**
A proposta fala em sistema de recomendação híbrido. Essa referência é clássica para explicar tipos de hibridização: weighted, switching, mixed, feature combination, cascade, feature augmentation e meta-level.

**Como usar no TCC:**
Na seção sobre sistemas híbridos, mostrando que a combinação de ontologia, regras fuzzy e eventualmente técnicas de recomendação baseadas em conteúdo ou popularidade se encaixa na tradição de sistemas híbridos.

**Relação com o TCC:**
Média-alta.

---

## 6. Referências adicionais que devem ser priorizadas no primeiro ciclo de leitura

A leitura inicial deve ser concentrada. A recomendação é não tentar ler 40 artigos de uma vez. O primeiro ciclo deve ter entre 8 e 12 fontes.

### Primeiro ciclo — leitura obrigatória

1. KARTHIK; GANAPATHY, 2021.
2. GUIA; SILVA; BERNARDINO, 2019.
3. YUAN; HERNANDEZ, 2023.
4. ZHANG et al., 2025.
5. FERREIRA-SATLER et al., 2012.
6. FERREIRA-SATLER et al., 2014.
7. GUO et al., 2022.
8. ZHANG; CHEN, 2020.
9. JAIN; GUPTA, 2018.
10. HOU et al., 2024.

### Segundo ciclo — leitura complementar

1. WANG et al., 2021.
2. TARUS; NIU; MUSTAFA, 2018.
3. ZHANG et al., 2019.
4. ISINKAYE; FOLAJIMI; OJOKOH, 2015.
5. BOBADILLA et al., 2013.
6. BURKE, 2002.
7. ADOMAVICIUS; TUZHILIN, 2005.

---

## 7. Estrutura recomendada da revisão bibliográfica

A revisão não deve ser organizada como “autor 1 disse isso, autor 2 disse aquilo”. O ideal é estruturar por temas, comparando abordagens.

### 7.1 Sistemas de recomendação em comércio eletrônico

Conteúdo esperado:

- conceito de sistemas de recomendação;
- recomendação baseada em conteúdo;
- filtragem colaborativa;
- recomendação baseada em conhecimento;
- sistemas híbridos;
- relevância em e-commerce.

Fontes principais:

- Isinkaye et al. (2015);
- Bobadilla et al. (2013);
- Zhang et al. (2025);
- Burke (2002).

---

### 7.2 Limitações dos sistemas tradicionais

Conteúdo esperado:

- esparsidade de dados;
- cold start de usuário;
- cold start de item;
- dependência de histórico;
- dificuldade em representar preferências graduais;
- limitação semântica de modelos puramente numéricos.

Fontes principais:

- Yuan e Hernandez (2023);
- Adomavicius e Tuzhilin (2005);
- Zhang et al. (2025).

---

### 7.3 Recomendação baseada em ontologias e conhecimento semântico

Conteúdo esperado:

- conceito de ontologia;
- representação de classes, relações e atributos;
- modelagem de domínio de produtos;
- semântica de categorias e atributos;
- relação com grafos de conhecimento;
- recomendação explicável.

Fontes principais:

- Guo et al. (2022);
- Guia, Silva e Bernardino (2019);
- Tarus, Niu e Mustafa (2018);
- Zhang e Chen (2020).

---

### 7.4 Lógica fuzzy e modelagem de preferências graduais

Conteúdo esperado:

- diferença entre lógica clássica e lógica fuzzy;
- graus de pertinência;
- variáveis linguísticas;
- regras fuzzy;
- preferências graduais de usuários;
- exemplos no contexto de e-commerce: preço baixo, avaliação alta, categoria preferida, produto muito compatível.

Fontes principais:

- Jain e Gupta (2018);
- Ferreira-Satler et al. (2012);
- Ferreira-Satler et al. (2014);
- Karthik e Ganapathy (2021).

---

### 7.5 Ontologias fuzzy e perfis de usuário

Conteúdo esperado:

- construção de perfis semânticos;
- associação entre usuário, preferências e atributos;
- atualização do perfil;
- integração entre ontologia e graus fuzzy;
- transferência conceitual de e-learning para e-commerce.

Fontes principais:

- Ferreira-Satler et al. (2012);
- Ferreira-Satler et al. (2014);
- Karthik e Ganapathy (2021).

---

### 7.6 Trabalhos relacionados em e-commerce

Conteúdo esperado:

- comparação direta entre trabalhos que usam ontologia, fuzzy, semântica e e-commerce;
- quais datasets foram usados;
- quais métricas foram aplicadas;
- quais lacunas permanecem.

Fontes principais:

- Karthik e Ganapathy (2021);
- Guia, Silva e Bernardino (2019);
- Guo et al. (2022);
- Zhang et al. (2025).

---

### 7.7 Síntese da lacuna

Síntese preliminar possível:

> A literatura apresenta avanços em recomendação baseada em conhecimento, ontologias, grafos de conhecimento e lógica fuzzy. Entretanto, ainda há espaço para investigar modelos híbridos que combinem ontologias fuzzy e preferências graduais em comércio eletrônico, especialmente quando o histórico de interações é limitado e o domínio possui alta complexidade semântica. Essa lacuna é relevante para contextos como e-commerces especializados, nos quais atributos de produtos, categorias, preço, avaliações e preferências subjetivas podem influenciar fortemente a recomendação.

---

## 8. Strings de busca para validação e ampliação da revisão

As buscas devem ser executadas em Google Scholar, IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, Scopus, Web of Science e Portal CAPES.

<pre class="overflow-visible! px-0!" data-start="1001" data-end="17586"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>### 8.1 Busca principal</span><br/><br/><span>```text</span><br/><span>("fuzzy ontology" OR "fuzzy ontologies") AND ("recommender system" OR "recommendation system") AND ("e-commerce" OR ecommerce OR retail)</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="17588" data-end="17721"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("ontology-based recommender system" OR "semantic recommender system") AND ("e-commerce" OR ecommerce OR "online retail")</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="17723" data-end="17823"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("fuzzy logic" AND "recommender system" AND "user profile") AND ("e-commerce" OR retail)</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="17825" data-end="17928"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("cold start" AND "recommender system") AND ("ontology" OR "semantic" OR "knowledge-based")</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="17930" data-end="17998"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("knowledge graph-based recommender systems" AND survey)</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18000" data-end="18053"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("explainable recommendation" AND survey)</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18055" data-end="18108"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("hybrid recommender systems" AND survey)</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

### 8.2 Busca focada em trabalhos recentes

Usar filtros de ano entre 2021 e 2026.

<pre class="overflow-visible! px-0!" data-start="18199" data-end="18272"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("ontology-based recommendation" AND "e-commerce") after:2021</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18274" data-end="18342"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("fuzzy recommender system" AND "e-commerce") after:2021</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18344" data-end="18428"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("knowledge graph" AND "recommender system" AND "e-commerce") after:2021</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18430" data-end="18503"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("cold start" AND "recommendation" AND "semantic") after:2021</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18505" data-end="18596"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>("product ontology" AND "recommender system" AND "user preferences") after:2021</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

### 8.3 Busca em português

<pre class="overflow-visible! px-0!" data-start="18631" data-end="18686"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>"ontologia fuzzy" "sistema de recomendação"</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18688" data-end="18757"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>"sistema de recomendação" "comércio eletrônico" ontologia</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18759" data-end="18831"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>"lógica fuzzy" "sistema de recomendação" "perfil de usuário"</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18833" data-end="18891"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>"recomendação semântica" "comércio eletrônico"</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="18893" data-end="18953"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>"cold start" "sistema de recomendação" ontologia</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

## 9. Critérios de inclusão e exclusão

### 9.1 Incluir artigos que:

* tratem de sistemas de recomendação;
* usem ontologias, grafos de conhecimento ou conhecimento semântico;
* usem lógica fuzzy ou modelagem gradual de preferências;
* abordem e-commerce, varejo digital, produtos, catálogos ou recomendação personalizada;
* discutam cold start, esparsidade ou baixa quantidade de interações;
* apresentem avaliação com métricas claras;
* usem dataset público ou descrevam bem os dados utilizados;
* sejam surveys, revisões sistemáticas ou trabalhos experimentais relevantes.

### 9.2 Excluir artigos que:

* mencionem “fuzzy” ou “ontology” apenas superficialmente;
* não tenham relação com recomendação;
* não apresentem método claro;
* não possuam texto completo acessível;
* não tenham avaliação ou comparação minimamente compreensível;
* sejam antigos sem valor seminal;
* não contribuam para o problema do TCC.
