# Validacao de schema - Amazon Reviews 2023 Home_and_Kitchen

Data da validacao: 2026-06-30.

Fonte oficial consultada:

- Pagina do dataset: https://amazon-reviews-2023.github.io/
- Reviews Home_and_Kitchen: `https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Home_and_Kitchen.jsonl.gz`
- Metadados Home_and_Kitchen: `https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz`

Segundo a tabela oficial do dataset, o subconjunto `Home_and_Kitchen` possui aproximadamente 23,2 milhoes de usuarios, 3,7 milhoes de itens, 67,4 milhoes de reviews, arquivo de reviews com cerca de 3,1 GB e arquivo de metadados com cerca de 3,8 GB. Por isso, a validacao foi feita por streaming e amostragem, sem baixar os arquivos completos.

## Comandos executados

```powershell
python scripts/data/explorar_schema.py "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Home_and_Kitchen.jsonl.gz" --limit 1000
python scripts/data/explorar_schema.py "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz" --limit 1000
python scripts/data/analisar_recorte_kouzina.py "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Home_and_Kitchen.jsonl.gz" --limit 50000
```

## Schema observado em reviews

Amostra: 1.000 linhas de `Home_and_Kitchen.jsonl.gz`.

| Campo | Tipo observado | Presentes | Nulos/vazios | Ausentes | Uso metodologico |
| --- | --- | ---: | ---: | ---: | --- |
| `asin` | `str` | 1000 | 0 | 0 | Identificador do item/review no nivel de ASIN. |
| `parent_asin` | `str` | 1000 | 0 | 0 | Chave recomendada para ligar review ao produto em metadados. |
| `user_id` | `str` | 1000 | 0 | 0 | Identificador de usuario para perfil fuzzy. |
| `rating` | `float` | 1000 | 0 | 0 | Sinal de preferencia/interacao. |
| `title` | `str` | 1000 | 0 | 0 | Titulo da review, nao titulo do produto. |
| `text` | `str` | 1000 | 0 | 0 | Texto da review. |
| `timestamp` | `int` | 1000 | 0 | 0 | Ordenacao temporal e possivel split temporal. |
| `helpful_vote` | `int` | 1000 | 0 | 0 | Sinal auxiliar de qualidade da review. |
| `verified_purchase` | `bool` | 1000 | 0 | 0 | Sinal auxiliar de confiabilidade da interacao. |
| `images` | `list` | 1000 | 907 | 0 | Anexo visual da review; nao essencial para o prototipo inicial. |

Exemplo real da primeira linha:

```json
{
  "rating": 1.0,
  "title": "Received Used & scratched item! Purchased new!",
  "text": "Livid.  Once again received an obviously used item that has food on it & scratches. I purchased this new!!  Pics not loading rn. Will add them later. Disgusted.",
  "images": [],
  "asin": "B007WQ9YNO",
  "parent_asin": "B09XWYG6X1",
  "user_id": "AFKZENTNBQ7A7V7UXW5JJI6UGRYQ",
  "timestamp": 1677373409298,
  "helpful_vote": 1,
  "verified_purchase": true
}
```

## Schema observado em metadados

Amostra: 1.000 linhas de `meta_Home_and_Kitchen.jsonl.gz`.

| Campo | Tipo observado | Presentes | Nulos/vazios | Ausentes | Uso metodologico |
| --- | --- | ---: | ---: | ---: | --- |
| `parent_asin` | `str` | 1000 | 0 | 0 | Chave principal do produto enriquecido. |
| `title` | `str` | 1000 | 0 | 0 | Titulo do produto. |
| `main_category` | `str`/`null` | 1000 | 36 | 0 | Categoria principal ampla. |
| `categories` | `list` | 1000 | 77 | 0 | Campo central para recorte e ontologia. |
| `features` | `list` | 1000 | 170 | 0 | Atributos textuais do produto. |
| `description` | `list` | 1000 | 442 | 0 | Descricao textual; frequentemente vazia. |
| `details` | `dict` | 1000 | 2 | 0 | Atributos estruturados adicionais. |
| `price` | `float`/`null` | 1000 | 463 | 0 | Preco relativo; incompleto. |
| `store` | `str`/`null` | 1000 | 13 | 0 | Aproximacao inicial de marca/loja. |
| `average_rating` | `float` | 1000 | 0 | 0 | Avaliacao media agregada do produto. |
| `rating_number` | `int` | 1000 | 0 | 0 | Numero de avaliacoes do produto. |
| `images` | `list` | 1000 | 0 | 0 | Imagens do produto; nao essencial para recomendacao inicial. |
| `videos` | `list` | 1000 | 523 | 0 | Videos do produto; fora do prototipo inicial. |
| `bought_together` | `null` | 1000 | 1000 | 0 | Sem uso inicial, pois veio nulo na amostra. |

Exemplo real da primeira linha:

```json
{
  "main_category": "Amazon Home",
  "title": "Set of 4 Irish Coffee Glass Mugs Footed 10.5 oz.Thick Wall Glass For Coffee, tea, Cappuccinos, Mulled Ciders,Hot Chocolates, Ice cream and More",
  "average_rating": 4.6,
  "rating_number": 18,
  "price": 24.95,
  "parent_asin": "B07R3DYMH6"
}
```

## Evidencia de disponibilidade em 50.000 metadados

Na amostra maior usada para revisar o recorte:

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

## Implicacoes para o TCC

- O dataset tem os identificadores minimos para recomendacao personalizada: `user_id`, `rating` e `parent_asin`.
- O produto deve ser modelado preferencialmente por `parent_asin`.
- O recorte de dominio deve usar principalmente `categories`, `title`, `features`, `description` e `details`.
- O preco pode apoiar grau premium, mas nao pode ser criterio obrigatorio universal.
- A marca precisa de cuidado: `store` e util, mas deve ser tratada como metadado textual a limpar, nao como garantia de marca oficial.
- `average_rating` e `rating_number` permitem calcular qualidade percebida e popularidade sem agregar reviews manualmente na primeira etapa.
- `bought_together`, `videos` e `images` nao devem ser prioridade no prototipo inicial.
