# Recorte Kouzina -> Amazon Reviews 2023

Este documento registra o mapeamento entre categorias do e-commerce Kouzina Club e evidencias reais encontradas no Amazon Reviews 2023 - Home_and_Kitchen.

A revisao abaixo foi feita apos validacao por amostragem dos arquivos oficiais:

- Reviews: `https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Home_and_Kitchen.jsonl.gz`
- Metadados: `https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz`

Comandos utilizados:

```powershell
python scripts/data/explorar_schema.py "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Home_and_Kitchen.jsonl.gz" --limit 1000
python scripts/data/explorar_schema.py "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz" --limit 1000
python scripts/data/analisar_recorte_kouzina.py "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz" --limit 50000
```

## Achados de schema que afetam o recorte

- O arquivo de reviews possui `user_id`, `asin`, `parent_asin`, `rating`, `title`, `text`, `timestamp`, `helpful_vote`, `verified_purchase` e `images`.
- O arquivo de metadados possui `parent_asin`, `title`, `main_category`, `categories`, `features`, `description`, `details`, `price`, `store`, `average_rating`, `rating_number`, `images` e `videos`.
- `parent_asin` aparece nos dois arquivos e deve ser o elo principal entre review/interacao e produto.
- `asin` aparece nas reviews, mas o metadado de produto usa `parent_asin`; nao assumir que `asin` e a chave principal do produto enriquecido.
- `price` existe, mas e incompleto: na amostra de 50.000 metadados, 24.588 registros estavam sem preco ou com valor vazio.
- `store` existe e pode ser usado como aproximacao de marca/loja, mas nao deve ser tratado automaticamente como marca oficial sem limpeza.
- `categories`, `title`, `features`, `description` e `details` sao os campos principais para o recorte textual e para extracao inicial de atributos.
- `average_rating` e `rating_number` aparecem nos metadados e podem apoiar qualidade percebida e popularidade do produto.

## Criterios revisados de recorte

- Priorizar categorias com evidencia direta em `categories`, como `Kitchen & Dining`, `Dining & Entertaining`, `Kitchen Utensils & Gadgets`, `Storage & Organization`, `Bath`, `Bathroom Accessories`, `Dinnerware & Serveware` e `Glassware & Drinkware`.
- Usar termos de `title`, `features`, `description`, `details`, `categories`, `main_category` e `store` como apoio, mas registrar que busca textual pode gerar falsos positivos.
- Tratar "produto premium/luxo" como variavel derivada. O dataset nao oferece esse rotulo diretamente.
- Nao depender apenas de `price`, porque quase metade da amostra de metadados nao possui preco.
- Usar `average_rating` e `rating_number` para qualidade/popularidade, mas nao confundir esses campos com avaliacao personalizada do usuario.

## Tabela Kouzina -> Amazon revisada com evidencia real

Evidencia baseada em amostra sequencial de 50.000 metadados de `meta_Home_and_Kitchen.jsonl.gz`.

| Categoria Kouzina | Evidencia real no dataset | Ambiente | Relevancia revisada | Termos/categorias para filtro | Decisao metodologica |
| --- | --- | --- | --- | --- | --- |
| Cafeteiras premium | 4.580 produtos com termos associados; exemplo real com `coffee`, `cappuccino` e `Irish Coffee`; `Glassware & Drinkware` apareceu 1.466 vezes. | Cozinha / Area gourmet | Alta | `coffee`, `espresso`, `cappuccino`, `coffee maker`, `barista`, `Glassware & Drinkware`, `Kitchen & Dining` | Manter. Categoria forte para demonstrar produto de maior valor percebido, mas filtrar itens simples por preco/avaliacao/atributos. |
| Fornos e preparo termico | 3.135 produtos com termos de preparo termico; `Appliances` apareceu como `main_category` 181 vezes na amostra. | Cozinha | Media | `oven`, `convection oven`, `toaster oven`, `bakeware`, `baking`, `roasting`, `Appliances` | Manter com cautela. Nao afirmar cobertura de "forno de embutir" sem filtro mais especifico. |
| Cooktops e queimadores | 734 produtos com termos; houve sinais para `induction`, `stovetop`, `burner`, `cooktop` e `hot plate`. | Cozinha | Media-alta | `cooktop`, `stovetop`, `burner`, `induction`, `hot plate` | Manter como categoria candidata, mas exigir validacao textual forte para evitar acessorios soltos. |
| Adegas climatizadas e bebidas | 104 produtos com termos; maior evidencia foi `wine rack`, com menor presenca de `wine cooler`, `wine cellar` e `wine refrigerator`. | Area gourmet | Media | `wine cooler`, `wine cellar`, `wine refrigerator`, `beverage cooler`, `wine rack`, `Dining & Entertaining` | Manter como nicho de area gourmet, mas nao tratar como categoria abundante. |
| Panelas premium | 5.848 produtos com termos; sinais fortes para `stainless steel`, `cookware`, `nonstick` e `cast iron`. | Cozinha | Alta | `cookware`, `stainless steel`, `ceramic`, `cast iron`, `nonstick`, `skillet`, `saucepan`, `Kitchen & Dining` | Manter. Boa categoria para operacionalizar material, preco relativo e avaliacao. |
| Utensilios gourmet | 2.157 produtos com termos; `Kitchen Utensils & Gadgets` apareceu 3.189 vezes em `categories`. | Cozinha / Area gourmet | Alta | `Kitchen Utensils & Gadgets`, `utensil`, `kitchen tool`, `gadget`, `chef`, `knife`, `spatula`, `whisk`, `tongs` | Manter. Exigir criterios premium adicionais porque a categoria mistura itens simples e sofisticados. |
| Loucas e jantar | 5.516 produtos com termos; `Dining & Entertaining` apareceu 4.329 vezes e `Dinnerware & Serveware` 1.337 vezes. | Sala de jantar / Area gourmet | Alta | `Dining & Entertaining`, `Dinnerware & Serveware`, `dinnerware`, `tableware`, `serveware`, `plate`, `bowl`, `porcelain`, `ceramic` | Manter. Categoria bem alinhada a experiencia premium de mesa e area gourmet. |
| Organizacao sofisticada | 8.621 produtos com termos; `Storage & Organization` apareceu 3.816 vezes. | Cozinha / Casa | Media-alta | `Storage & Organization`, `storage`, `organizer`, `pantry`, `drawer organizer`, `countertop`, `cabinet organizer` | Manter, mas controlar amplitude para nao deslocar o foco de cozinha/banheiro/gourmet. |
| Torneiras premium | 811 produtos com termos, mas parte da evidencia veio de termos genericos como `chrome` e `matte black`; `Tools & Home Improvement` apareceu 2.319 vezes como `main_category`. | Banheiro / Cozinha | Media | `faucet`, `sink faucet`, `bathroom faucet`, `kitchen faucet`, `chrome`, `matte black`, `Tools & Home Improvement` | Manter como categoria secundaria. Exigir termos especificos de `faucet` para reduzir falsos positivos. |
| Cubas e pias | 691 produtos com termos; houve sinais para `sink`, `kitchen sink`, `bathroom sink` e `basin`, mas com risco de acessorios de pia. | Banheiro / Cozinha | Media | `sink`, `basin`, `vessel sink`, `bathroom sink`, `kitchen sink` | Manter como secundaria e dependente de filtro textual especifico. |
| Chuveiros e acessorios de banho | 2.710 produtos com termos; `Bath` apareceu 2.391 vezes e `Bathroom Accessories` 1.564 vezes. | Banheiro | Media-alta | `Bath`, `Bathroom Accessories`, `shower`, `shower head`, `rain shower`, `bath accessory` | Manter para o eixo banheiro, separando acessorios simples de itens premium por preco, avaliacao e atributos. |
| Decoracao funcional premium | 25.470 produtos com termos; `Home Décor Products` apareceu 11.108 vezes, mas a categoria e muito ampla. | Casa / Area gourmet | Media | `Home Décor Products`, `Home Décor Accents`, `decor`, `decorative`, `designer`, `modern`, `premium`, `luxury` | Manter apenas como recorte complementar. Nao deixar decoracao dominar o dataset curado. |

## Campos validados para uso metodologico

| Campo validado | Origem | Uso no projeto | Restricao |
| --- | --- | --- | --- |
| `parent_asin` | reviews e metadados | Relacionar interacoes e produto enriquecido | Chave principal recomendada para produto. |
| `user_id` | reviews | Construir perfil fuzzy do usuario | Disponivel nas reviews, nao nos metadados. |
| `rating` | reviews | Definir interacao positiva, negativa ou neutra | Rating da review do usuario. |
| `title` | reviews e metadados | Review title nas reviews; produto title nos metadados | Nao misturar os dois significados. |
| `text` | reviews | Texto da review | Pode apoiar analise futura, mas nao e necessario para o primeiro recorte. |
| `categories` | metadados | Mapear produto para dominio/ontologia | Lista presente, mas pode vir vazia. |
| `features` | metadados | Extrair atributos e termos de qualidade/material | Lista pode vir vazia. |
| `description` | metadados | Extrair atributos textuais | Na amostra de 50.000, 22.489 estavam vazios. |
| `details` | metadados | Buscar atributos estruturados adicionais | Presente na maior parte da amostra. |
| `price` | metadados | Preco relativo e criterio premium | Ausente/vazio em 24.588 de 50.000 metadados analisados. |
| `store` | metadados | Aproximacao inicial de marca/loja | Precisa limpeza; nao assumir marca oficial. |
| `average_rating` | metadados | Qualidade percebida do produto | Agregado por produto. |
| `rating_number` | metadados | Popularidade/confianca do produto | Agregado por produto. |

## Decisoes apos validacao

- O recorte Home_and_Kitchen e metodologicamente defensavel para cozinha, area gourmet, jantar, organizacao, banheiro e parte de eletrodomesticos.
- A variavel premium deve combinar evidencias, nao depender de palavra `premium`, `luxury` ou de preco isolado.
- Categorias de banheiro existem no recorte, mas precisam filtro cuidadoso porque muitos itens sao acessorios simples.
- Categorias de eletrodomesticos existem em menor proporcao; nao prometer cobertura forte de fornos de embutir, cooktops ou adegas sem filtros especificos.
- A proxima etapa deve transformar este mapeamento em filtros reproduziveis, com amostra curada e revisao manual de falsos positivos.

## Pendencias atualizadas

- Criar amostra curada de produtos usando os filtros versionados em `configs/dataset/kouzina_mapping.yaml`.
- Medir falsos positivos por categoria em uma amostra manual revisada.
- Definir regra de uso de `price` para produtos sem preco.
- Definir se `store` sera tratado como marca, loja ou apenas metadado auxiliar.
- Registrar a versao final dos filtros antes de implementar ontologia, motor fuzzy ou baselines.
