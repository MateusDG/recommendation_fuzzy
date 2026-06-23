# Recorte Kouzina -> Amazon Reviews 2023

Este documento registra a estrutura inicial do mapeamento entre categorias do e-commerce Kouzina Club e categorias ou termos equivalentes no Amazon Reviews 2023 - Home and Kitchen.

O objetivo e justificar o recorte do dataset para um dominio proximo ao TCC: produtos premium/luxo para casa, cozinha, area gourmet e banheiro. A tabela abaixo e preliminar e deve ser revisada apos a validacao do schema real do dataset.

## Criterios iniciais de recorte

- Priorizar produtos de cozinha, area gourmet, eletrodomesticos, cafe, jantar, utensilios, organizacao sofisticada e banheiro.
- Usar categorias e textos do dataset como evidencia, nao apenas palavras como `premium` ou `luxury`.
- Tratar "produto premium" como uma variavel derivada por criterios observaveis.
- Registrar termos de busca para que o filtro seja reproduzivel.
- Classificar a relevancia de cada categoria para o TCC.

## Tabela de mapeamento inicial

| Categoria Kouzina | Categoria Amazon candidata | Ambiente | Relevancia | Termos de Busca | Observacoes |
| --- | --- | --- | --- | --- | --- |
| Cafeteiras premium | Coffee, Tea & Espresso; Small Appliances | Cozinha / Area gourmet | Alta | `coffee`, `espresso`, `coffee maker`, `espresso machine`, `barista` | Categoria forte para perfil premium e area gourmet. |
| Fornos de embutir | Appliances; Kitchen Appliances; Small Appliances | Cozinha | Alta | `oven`, `built-in oven`, `convection oven`, `electric oven` | Confirmar se Home and Kitchen contem metadados suficientes para esse tipo de produto. |
| Cooktops | Appliances; Kitchen Appliances | Cozinha | Alta | `cooktop`, `stovetop`, `burner`, `induction`, `gas cooktop` | Pode exigir busca textual se a categoria nao existir explicitamente. |
| Adegas climatizadas | Kitchen Appliances; Wine Accessories; Dining & Entertaining | Area gourmet | Alta | `wine cooler`, `wine cellar`, `wine refrigerator`, `beverage cooler` | Categoria relevante para produtos de alto valor agregado. |
| Panelas premium | Cookware; Kitchen & Dining | Cozinha | Alta | `cookware`, `stainless steel`, `ceramic`, `cast iron`, `nonstick` | Boa candidata para regras de material e avaliacao. |
| Utensilios gourmet | Kitchen Utensils & Gadgets; Kitchen & Dining | Cozinha / Area gourmet | Alta | `gourmet`, `kitchen utensils`, `chef`, `knife`, `gadget` | Pode misturar produtos simples e premium; exige caracterizacao posterior. |
| Loucas e jantar | Dining & Entertaining; Dinnerware | Sala de jantar / Area gourmet | Media-alta | `dinnerware`, `serveware`, `porcelain`, `ceramic`, `tableware` | Relevante para experiencia premium, mas pode ter variacao grande de preco. |
| Organizacao sofisticada | Storage & Organization; Kitchen Storage | Cozinha / Casa | Media | `storage`, `organizer`, `pantry`, `countertop`, `drawer organizer` | Manter se o recorte nao ficar amplo demais. |
| Torneiras premium | Bath; Bathroom Accessories; Kitchen Fixtures | Banheiro / Cozinha | Media-alta | `faucet`, `sink faucet`, `bathroom faucet`, `kitchen faucet`, `chrome`, `matte black` | Validar se o dataset Home and Kitchen cobre esse tipo de item. |
| Cubas e pias | Bath; Bathroom Accessories; Kitchen Fixtures | Banheiro / Cozinha | Media | `sink`, `basin`, `bathroom sink`, `kitchen sink`, `vessel sink` | Pode depender de categorias de Home Improvement fora de Home and Kitchen. |
| Chuveiros e acessorios de banho | Bath; Bathroom Accessories | Banheiro | Media | `shower`, `shower head`, `bath accessory`, `rain shower` | Usar apenas se houver cobertura consistente no dataset. |
| Decoracao funcional premium | Home Decor; Kitchen & Dining | Casa / Area gourmet | Media | `decor`, `designer`, `modern`, `premium`, `luxury` | Cuidado para nao abrir demais o escopo. |

## Campos esperados para validar no dataset

| Campo desejado | Uso no projeto | Observacao |
| --- | --- | --- |
| Identificador do produto | Relacionar produto, review e recomendacao | Obrigatorio para qualquer avaliacao. |
| Identificador do usuario | Construir perfil fuzzy | Obrigatorio para recomendacao personalizada. |
| Rating | Definir interacao positiva, negativa ou neutra | Ratings 4 e 5 tendem a ser positivos. |
| Categoria | Mapear produto para ontologia | Pode vir como lista, caminho hierarquico ou texto. |
| Titulo | Filtragem textual e extracao de atributos | Importante quando categoria for insuficiente. |
| Descricao | Extracao de material, estilo e funcao | Nem sempre esta presente. |
| Preco | Variavel fuzzy e criterio premium | Campo critico, mas pode estar ausente. |
| Marca | Preferencia de usuario e criterio premium | Pode estar ausente ou inconsistente. |
| Numero de reviews | Popularidade e confianca | Pode precisar ser calculado. |
| Avaliacao media | Qualidade percebida | Pode precisar ser agregada. |

## Pendencias

- Validar o schema real do Amazon Reviews 2023 - Home and Kitchen.
- Confirmar os nomes exatos das colunas de produtos e reviews.
- Verificar se categorias de banheiro e eletrodomesticos aparecem no recorte Home and Kitchen.
- Revisar a tabela com categorias reais da Kouzina, quando estiverem disponiveis.
- Transformar este mapeamento em configuracao versionada apos aprovacao.

