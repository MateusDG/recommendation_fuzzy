# 1 INTRODUÇÃO

## 1.1 CONTEXTUALIZAÇÃO DO PROBLEMA DE PESQUISA

Sistemas de recomendação ocupam posição estratégica em plataformas de comércio eletrônico porque reduzem a sobrecarga de informação e auxiliam o usuário a localizar itens compatíveis com seus interesses. O problema técnico não se limita a apresentar produtos populares: é necessário representar preferências, utilizar as informações disponíveis sobre usuários e itens e ordenar alternativas relevantes. A literatura classifica as abordagens tradicionais principalmente em recomendação baseada em conteúdo, filtragem colaborativa e métodos híbridos (Adomavicius; Tuzhilin, 2005; Isinkaye; Folajimi; Ojokoh, 2015).

Modelos baseados em filtragem colaborativa exploram padrões de avaliações ou interações, mas sua capacidade de estimar preferências diminui quando a matriz usuário-item é esparsa. Essa limitação afeta usuários e produtos com poucos registros e exige que a avaliação do sistema considere diferentes níveis de disponibilidade de dados. No recorte deste trabalho, depender exclusivamente de sinais colaborativos poderia deixar de aproveitar informações descritivas e semânticas presentes no catálogo (Adomavicius; Tuzhilin, 2005; Isinkaye; Folajimi; Ojokoh, 2015).

Uma manifestação específica da insuficiência de dados é o *cold start*. Usuários novos não possuem histórico suficiente para a construção de um perfil confiável, enquanto itens novos ainda não acumularam avaliações ou interações. Nesses casos, métodos que dependem apenas do histórico encontram dificuldade para estimar a relevância das recomendações, o que justifica investigar fontes adicionais de conhecimento sobre usuários e produtos (Yuan; Hernandez, 2023).

Outra questão está na natureza gradual das preferências. Um usuário pode apresentar alta afinidade por cozinha gourmet, preferência moderada por determinada faixa de preço e interesse parcial por materiais ou funcionalidades específicas. Essas dimensões não são adequadamente descritas apenas por classificações binárias. A lógica *fuzzy* permite atribuir graus de pertinência a conceitos linguísticos, como preço alto, avaliação excelente, popularidade média ou compatibilidade elevada, e oferece recursos para representar incerteza e imprecisão em sistemas de recomendação (Jain; Gupta, 2018).

Ontologias de domínio complementam essa representação ao explicitar conceitos e relações entre usuários, produtos, categorias, ambientes, materiais, marcas e funções. Em vez de utilizar somente a matriz de interações, um recomendador baseado em conhecimento pode explorar a estrutura semântica do catálogo como informação adicional. Essa organização não elimina o problema de escassez de dados, mas amplia os elementos disponíveis para comparar itens e justificar recomendações (Guia; Silva; Bernardino, 2019; Guo *et al.*, 2022).

O presente trabalho investiga a integração entre recomendação personalizada, lógica *fuzzy* e ontologias no comércio eletrônico. O recorte empírico utiliza o *dataset* Amazon Reviews 2023, no subconjunto *Home and Kitchen*, por sua proximidade com produtos residenciais, cozinha, área gourmet e banheiro (Hou *et al.*, 2024). A base não classifica oficialmente itens como luxo ou *premium*; por isso, esse conceito será tratado como uma construção operacional baseada em atributos observáveis e em critérios que deverão ser documentados e avaliados. Diante desse contexto, formula-se a seguinte questão de pesquisa: em que medida a integração entre conhecimento ontológico e representação *fuzzy* de preferências pode apoiar recomendações personalizadas e explicáveis em cenários com diferentes níveis de informação sobre usuários e produtos?

## 1.2 JUSTIFICATIVA E MOTIVAÇÃO

A justificativa deste trabalho está nas limitações dos recomendadores tradicionais quando as interações disponíveis são insuficientes ou quando atributos relevantes do domínio não estão representados na matriz usuário-item. A filtragem colaborativa utiliza relações observadas entre usuários e produtos, enquanto abordagens baseadas em conteúdo e conhecimento podem incorporar características dos itens. A combinação dessas fontes em um sistema híbrido permite investigar se informações complementares produzem recomendações mais adequadas ao problema estudado, sem pressupor ganho automático de desempenho (Adomavicius; Tuzhilin, 2005; Burke, 2002).

No domínio de produtos residenciais *premium*, a proposta considera que a recomendação deve ser acompanhada por fatores compreensíveis, como categoria, ambiente de uso, faixa de preço, avaliação e atributos do produto. A explicabilidade é relevante porque permite apresentar ao usuário e ao pesquisador os elementos que contribuíram para uma sugestão, favorecendo a análise da transparência e da aceitação das recomendações (Zhang; Chen, 2020).

A lógica *fuzzy* contribui para esse objetivo ao representar gradualidade sem impor fronteiras rígidas. Um produto pode possuir diferentes graus de pertinência ao conceito *premium*, e um usuário pode apresentar níveis distintos de afinidade por categorias, ambientes ou faixas de preço. Regras linguísticas podem combinar esses graus e produzir escores rastreáveis, desde que as funções de pertinência e os critérios de inferência sejam definidos e documentados de forma explícita (Jain; Gupta, 2018; Karthik; Ganapathy, 2021).

A ontologia acrescenta uma estrutura semântica para organizar o domínio e relacionar produtos, categorias, atributos e preferências. Em cenários de *cold start*, essa estrutura pode fornecer informação adicional ao histórico de interações, sem ser tratada como solução garantida para o problema. A combinação entre ontologia, filtragem colaborativa e regras *fuzzy* possui precedentes em estudos de recomendação para comércio eletrônico e constitui a hipótese técnica que será examinada neste trabalho (Guia; Silva; Bernardino, 2019; Karthik; Ganapathy, 2021).

A escolha do Amazon Reviews 2023 - *Home and Kitchen* se justifica por oferecer dados públicos de avaliações e metadados de produtos próximos ao domínio investigado. A validação inicial do esquema confirmou campos como título, descrição, características, preço, avaliação média e número de avaliações, além de categorias relacionadas a cozinha, organização e banheiro. Esses campos apresentam limitações de cobertura e deverão ser tratados durante a preparação dos dados. O uso de uma base pública favorece a reprodutibilidade, desde que versão, filtros, parâmetros e critérios de recorte sejam registrados (Hou *et al.*, 2024).

A motivação acadêmica consiste em avaliar, de forma controlada, como conhecimento semântico e preferências graduais podem ser combinados em um protótipo de recomendação. A literatura registra desafios associados a *cold start*, esparsidade e explicabilidade, enquanto trabalhos aplicados mostram diferentes formas de integrar ontologias e lógica *fuzzy* (Yuan; Hernandez, 2023; Zhang; Chen, 2020; Guia; Silva; Bernardino, 2019; Karthik; Ganapathy, 2021). Assim, o trabalho delimita como espaço de investigação a aplicação dessa integração a produtos residenciais *premium*, com comparação experimental frente a métodos de referência.

## 1.3 OBJETIVOS GERAL E ESPECÍFICOS

O objetivo geral deste trabalho é desenvolver e avaliar um sistema de recomendação híbrido baseado na integração entre ontologias e lógica *fuzzy*, capaz de modelar preferências graduais de usuários e gerar recomendações personalizadas e explicáveis para produtos residenciais *premium* em comércio eletrônico.

Para alcançar esse objetivo geral, são definidos quatro objetivos específicos:

a) analisar os fundamentos de sistemas de recomendação, lógica *fuzzy*, ontologias, explicabilidade e estratégias relacionadas ao problema de *cold start*;

b) selecionar, validar e preparar um recorte do Amazon Reviews 2023 - *Home and Kitchen*, incluindo a definição operacional e rastreável do conceito de produto *premium*;

c) modelar a representação ontológica do domínio, os perfis graduais de usuário e as regras *fuzzy*, integrando esses elementos em um protótipo que gere listas de recomendação e justificativas associadas;

d) avaliar o modelo proposto com o mesmo protocolo experimental aplicado aos métodos de referência, utilizando métricas de recomendação Top-N e cenários gerais e de *cold start*.

## 1.4 SÍNTESE DA METODOLOGIA

A investigação será desenvolvida em quatro etapas. A primeira corresponde à revisão bibliográfica dos conceitos e trabalhos relacionados. A segunda abrange a validação do esquema, a limpeza e o recorte do Amazon Reviews 2023 - *Home and Kitchen*, sem assumir a existência de um rótulo nativo de produto *premium*. A terceira compreende a modelagem da ontologia, das variáveis linguísticas, das funções de pertinência e das regras *fuzzy*, seguida pelo desenvolvimento do protótipo. A quarta etapa consiste na avaliação experimental do modelo e dos métodos de referência sob os mesmos conjuntos de treino e teste.

Os experimentos deverão registrar versão dos dados, filtros, parâmetros, métricas e sementes. A avaliação considerará listas Top-N, cenários de *cold start*, cobertura e análise das justificativas produzidas. As decisões metodológicas serão documentadas antes ou junto da implementação para manter a rastreabilidade entre os objetivos, os dados, as regras de inferência e os resultados.

## 1.5 ORGANIZAÇÃO DA MONOGRAFIA

Esta monografia está organizada em sete capítulos. O primeiro apresenta a contextualização do problema, a justificativa, os objetivos, a síntese metodológica e a estrutura geral do trabalho.

O segundo capítulo aborda a fundamentação teórica sobre sistemas de recomendação, filtragem colaborativa, recomendação baseada em conteúdo, lógica *fuzzy*, ontologias, representação semântica e conceitos arquiteturais necessários ao protótipo.

O terceiro capítulo apresenta os trabalhos relacionados e compara estudos sobre recomendação *fuzzy*, ontologias, sistemas semânticos, *cold start*, explicabilidade e aplicações em comércio eletrônico.

O quarto capítulo descreve a metodologia, incluindo a preparação do Amazon Reviews 2023 - *Home and Kitchen*, os critérios de recorte, a definição operacional de produto *premium*, a modelagem ontológica e *fuzzy* e o protocolo experimental.

O quinto capítulo trata do desenvolvimento do protótipo e descreve a integração entre ontologia, regras *fuzzy*, geração de listas Top-N e justificativas das recomendações.

O sexto capítulo apresenta os testes, as métricas, os métodos de referência, os cenários de *cold start* e a análise dos resultados que forem obtidos.

O sétimo capítulo reúne as conclusões, as limitações do estudo e as possibilidades de continuidade da pesquisa.
