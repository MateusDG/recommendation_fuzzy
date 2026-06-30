# Evidencia de recorte Kouzina -> Amazon Reviews 2023

Fonte analisada: `https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz`

Amostra sequencial de metadados analisada: `50000` registros.

> Observacao: esta contagem e uma evidencia exploratoria de cobertura textual. Ela nao substitui a etapa posterior de filtragem curada nem prova que o item seja premium/luxo.

## Disponibilidade de campos na amostra

| Campo | Presentes | Nulos/vazios |
| --- | ---: | ---: |
| `parent_asin` | 50000 | 0 |
| `title` | 50000 | 1 |
| `main_category` | 50000 | 1289 |
| `categories` | 50000 | 4314 |
| `features` | 50000 | 9087 |
| `description` | 50000 | 22489 |
| `details` | 50000 | 88 |
| `price` | 50000 | 24588 |
| `store` | 50000 | 872 |
| `average_rating` | 50000 | 0 |
| `rating_number` | 50000 | 0 |

## Principais `main_category` observadas

| main_category | Ocorrencias |
| --- | ---: |
| Amazon Home | 42829 |
| Tools & Home Improvement | 2319 |
| Toys & Games | 559 |
| Industrial & Scientific | 463 |
| AMAZON FASHION | 421 |
| Health & Personal Care | 397 |
| Office Products | 330 |
| Sports & Outdoors | 223 |
| Arts, Crafts & Sewing | 190 |
| Appliances | 181 |

## Principais valores em `categories`

| categories | Ocorrencias |
| --- | ---: |
| Home & Kitchen | 45638 |
| Kitchen & Dining | 15334 |
| Home Décor Products | 11108 |
| Bedding | 6010 |
| Dining & Entertaining | 4329 |
| Storage & Organization | 3816 |
| Home Décor Accents | 3749 |
| Furniture | 3528 |
| Kitchen Utensils & Gadgets | 3189 |
| Bath | 2391 |
| Kitchen & Table Linens | 1968 |
| Wall Art | 1933 |
| Posters & Prints | 1858 |
| Window Treatments | 1700 |
| Bathroom Accessories | 1564 |
| Glassware & Drinkware | 1466 |
| Decorative Pillows, Inserts & Covers | 1445 |
| Event & Party Supplies | 1364 |
| Dinnerware & Serveware | 1337 |
| Curtains & Drapes | 1255 |

## Evidencia por grupo Kouzina

| Grupo Kouzina | Produtos com algum termo | Termos mais frequentes | Exemplo real de titulo |
| --- | ---: | --- | --- |
| Cafeteiras premium | 4580 | `coffee`:13797, `espresso`:1686, `cappuccino`:293, `barista`:107, `irish coffee`:12 | Set of 4 Irish Coffee Glass Mugs Footed 10.5 oz.Thick Wall Glass For Coffee, tea, Cappuccinos, Mulled Ciders,Hot Chocolates, Ice cream and More (`parent_asin=B07R3DYMH6`, preco=24.95, rating=4.6) |
| Fornos e preparo termico | 3135 | `baking`:4320, `oven`:4250, `bakeware`:1755, `roasting`:251, `toaster oven`:75 | Trylis Silicone Oven Mitts Heat Resistant Pot Holders Mini Cooking Gloves Insulation Finger Protector Pinch Pink 2pcs (`parent_asin=B08BPJ7XPX`, preco=None, rating=4.0) |
| Cooktops e queimadores | 734 | `induction`:726, `stovetop`:534, `burner`:525, `cooktop`:134, `hot plate`:45 | Aluminum 11inch Heat Diffuser Plate For Gas Stove Induction Electric Stovestovetop Gas stove Top Iarge (`parent_asin=B08TH5QLP5`, preco=32.8, rating=3.9) |
| Adegas e bebidas | 104 | `wine rack`:161, `wine cooler`:43, `wine cellar`:32, `beverage cooler`:12, `wine refrigerator`:4 | LAGRIMA 91 Bottle Capacity Stackable Storage Wine Rack, Standing Bottles Storage Shelf, Wobble-Free,7-Tier Black (`parent_asin=B07QQQVC14`, preco=None, rating=4.6) |
| Panelas premium | 5848 | `stainless steel`:15099, `cookware`:2407, `nonstick`:1437, `cast iron`:953, `skillet`:311 | TOP CHEF - Dynasty 9-Piece Block Knife Set - German Stainless Steel Kitchen Knives with Walnut-Stained Wood Handles (`parent_asin=B06Y3Q3VQB`, preco=None, rating=4.6) |
| Utensilios gourmet | 2157 | `knife`:3450, `chef`:1523, `spatula`:873, `utensil`:825, `tongs`:690 | TOP CHEF - Dynasty 9-Piece Block Knife Set - German Stainless Steel Kitchen Knives with Walnut-Stained Wood Handles (`parent_asin=B06Y3Q3VQB`, preco=None, rating=4.6) |
| Loucas e jantar | 5516 | `ceramic`:6421, `bowl`:3454, `dinnerware`:3055, `serveware`:2187, `plate`:2153 | Foaming Soap Dispenser Thick Ceramic Foam Hand Soap Dispenser for Bathroom or Kitchen Sink, Liquid Pump Bottles for Hand soap, Body Wash, 2 Pack Black (`parent_asin=B0BNZ8Q7YT`, preco=24.99, rating=4.4) |
| Organizacao sofisticada | 8621 | `storage`:23458, `organizer`:3857, `countertop`:1872, `pantry`:799, `drawer organizer`:219 | FESS Products 10.75"x 8" Wooden Storage Box for home with Hinged Lid - Decorative boxes with lids - Store Jewelry, Toys, and Large Premium Keepsakes in a Beautiful Decorative Crate (Black Matte) (`parent_asin=B09B2ZX2D5`, preco=34.95, rating=5.0) |
| Torneiras premium | 811 | `chrome`:1318, `matte black`:314, `faucet`:216, `sink faucet`:14, `kitchen faucet`:10 | Contigo SnapSeal Travel Mug 16 oz - Matte Black & Monaco (`parent_asin=B01N5CAJ6W`, preco=None, rating=4.8) |
| Cubas e pias | 691 | `sink`:1351, `kitchen sink`:235, `basin`:91, `bathroom sink`:61 | Foaming Soap Dispenser Thick Ceramic Foam Hand Soap Dispenser for Bathroom or Kitchen Sink, Liquid Pump Bottles for Hand soap, Body Wash, 2 Pack Black (`parent_asin=B0BNZ8Q7YT`, preco=24.99, rating=4.4) |
| Chuveiros e acessorios de banho | 2710 | `shower`:11629, `bath accessory`:16, `rain shower`:1 | Silicone Soap Dish with Drain, 2 Pcs Bar Soap Holder for Shower/Bathroom, Self Draining Waterfall Soap Tray to Keep Soap Dry Clean (`parent_asin=B08QYSNT4R`, preco=9.7, rating=2.9) |
| Decoracao funcional premium | 25470 | `decor`:18710, `modern`:17464, `decorative`:13707, `premium`:8675, `luxury`:3597 | CaliTime Throw Pillow Cases Pack of 2 Modern Solid Dyed Soft Faux Leather Decorative Cushion Covers Shells for Couch Sofa Bedroom 18 X 18 Inches Black (`parent_asin=B08C736K4M`, preco=None, rating=4.7) |

## Leitura metodologica da evidencia

- Os grupos de cozinha, jantar, utensilios, panelas, cafe, organizacao e banheiro possuem evidencia suficiente para o recorte inicial.
- Decoracao aparece com alta frequencia, mas e ampla demais; deve ser complementar e nao eixo central do prototipo.
- Adegas, cooktops, torneiras e cubas aparecem em menor volume ou com termos ambivalentes; devem ser categorias secundarias ou de validacao manual.
- Exemplos baseados em termos genericos podem conter falsos positivos. Por isso, os filtros finais devem combinar categoria, titulo, atributos, preco, avaliacao e revisao manual de amostra.
