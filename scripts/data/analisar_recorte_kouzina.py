#!/usr/bin/env python
"""Analisa evidencias textuais do recorte Kouzina em metadados Amazon.

Uso:
    python scripts/data/analisar_recorte_kouzina.py URL_META_HOME_KITCHEN --limit 50000

Este script e exploratorio. Ele nao define regras fuzzy nem classifica produto
premium; apenas conta sinais textuais em uma amostra real de metadados para
apoiar a decisao metodologica do recorte.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from itertools import islice
from typing import Any, Dict, Iterable, Iterator, List

from explorar_schema import open_text


Row = Dict[str, Any]


TERM_GROUPS: dict[str, list[str]] = {
    "Cafeteiras premium": [
        "coffee",
        "espresso",
        "cappuccino",
        "coffee maker",
        "irish coffee",
        "barista",
    ],
    "Fornos e preparo termico": [
        "oven",
        "convection oven",
        "toaster oven",
        "bakeware",
        "baking",
        "roasting",
    ],
    "Cooktops e queimadores": [
        "cooktop",
        "stovetop",
        "burner",
        "induction",
        "hot plate",
    ],
    "Adegas e bebidas": [
        "wine cooler",
        "wine cellar",
        "wine refrigerator",
        "beverage cooler",
        "wine rack",
    ],
    "Panelas premium": [
        "cookware",
        "skillet",
        "saucepan",
        "cast iron",
        "stainless steel",
        "nonstick",
    ],
    "Utensilios gourmet": [
        "kitchen utensil",
        "utensil",
        "kitchen tool",
        "gadget",
        "chef",
        "knife",
        "spatula",
        "whisk",
        "tongs",
    ],
    "Loucas e jantar": [
        "dinnerware",
        "tableware",
        "serveware",
        "plate",
        "bowl",
        "porcelain",
        "ceramic",
    ],
    "Organizacao sofisticada": [
        "storage",
        "organizer",
        "pantry",
        "drawer organizer",
        "countertop",
        "cabinet organizer",
    ],
    "Torneiras premium": [
        "faucet",
        "sink faucet",
        "bathroom faucet",
        "kitchen faucet",
        "matte black",
        "chrome",
    ],
    "Cubas e pias": [
        "sink",
        "basin",
        "vessel sink",
        "bathroom sink",
        "kitchen sink",
    ],
    "Chuveiros e acessorios de banho": [
        "shower",
        "shower head",
        "rain shower",
        "bath accessory",
    ],
    "Decoracao funcional premium": [
        "decor",
        "decorative",
        "designer",
        "modern",
        "premium",
        "luxury",
    ],
}


FIELDS_OF_INTEREST = [
    "parent_asin",
    "title",
    "main_category",
    "categories",
    "features",
    "description",
    "details",
    "price",
    "store",
    "average_rating",
    "rating_number",
]


def iter_jsonl(source: str) -> Iterator[Row]:
    with open_text(source) as file_obj:
        for line_number, line in enumerate(file_obj, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"JSON invalido na linha {line_number}: {exc}") from exc
            if isinstance(value, dict):
                yield value


def flatten(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(flatten(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{key} {flatten(item)}" for key, item in value.items())
    return str(value)


def row_text(row: Row) -> str:
    parts = [
        row.get("title"),
        row.get("main_category"),
        row.get("categories"),
        row.get("features"),
        row.get("description"),
        row.get("details"),
        row.get("store"),
    ]
    return " ".join(flatten(part) for part in parts).lower()


def compile_terms(terms: Iterable[str]) -> re.Pattern[str]:
    escaped = [re.escape(term.lower()) for term in terms]
    return re.compile(r"(?<![a-z0-9])(" + "|".join(escaped) + r")(?![a-z0-9])")


def is_null_like(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False


def summarize(source: str, limit: int) -> str:
    patterns = {group: compile_terms(terms) for group, terms in TERM_GROUPS.items()}
    counts = Counter()
    term_hits: dict[str, Counter[str]] = {group: Counter() for group in TERM_GROUPS}
    examples: dict[str, Row] = {}
    example_quality: dict[str, int] = {}
    field_present = Counter()
    field_null = Counter()
    main_categories = Counter()
    category_terms = Counter()

    rows = list(islice(iter_jsonl(source), limit))

    for row in rows:
        for field in FIELDS_OF_INTEREST:
            if field in row:
                field_present[field] += 1
                if is_null_like(row[field]):
                    field_null[field] += 1
            else:
                field_null[field] += 1

        main_category = row.get("main_category")
        if main_category:
            main_categories[str(main_category)] += 1

        categories = row.get("categories")
        if isinstance(categories, list):
            for category in categories:
                if category:
                    category_terms[str(category)] += 1

        text = row_text(row)
        title_category_text = " ".join(
            [
                flatten(row.get("title")),
                flatten(row.get("categories")),
                flatten(row.get("main_category")),
            ]
        ).lower()
        for group, pattern in patterns.items():
            matches = pattern.findall(text)
            if matches:
                counts[group] += 1
                term_hits[group].update(matches)
                quality = 2 if pattern.search(title_category_text) else 1
                if quality > example_quality.get(group, 0):
                    examples[group] = row
                    example_quality[group] = quality

    lines = [
        "# Evidencia de recorte Kouzina -> Amazon Reviews 2023",
        "",
        f"Fonte analisada: `{source}`",
        f"Amostra sequencial de metadados analisada: `{len(rows)}` registros.",
        "",
        "> Observacao: esta contagem e uma evidencia exploratoria de cobertura textual. Ela nao substitui a etapa posterior de filtragem curada nem prova que o item seja premium/luxo.",
        "",
        "## Disponibilidade de campos na amostra",
        "",
        "| Campo | Presentes | Nulos/vazios |",
        "| --- | ---: | ---: |",
    ]

    for field in FIELDS_OF_INTEREST:
        lines.append(f"| `{field}` | {field_present[field]} | {field_null[field]} |")

    lines.extend(
        [
            "",
            "## Principais `main_category` observadas",
            "",
            "| main_category | Ocorrencias |",
            "| --- | ---: |",
        ]
    )
    for category, count in main_categories.most_common(10):
        lines.append(f"| {category} | {count} |")

    lines.extend(
        [
            "",
            "## Principais valores em `categories`",
            "",
            "| categories | Ocorrencias |",
            "| --- | ---: |",
        ]
    )
    for category, count in category_terms.most_common(20):
        lines.append(f"| {category} | {count} |")

    lines.extend(
        [
            "",
            "## Evidencia por grupo Kouzina",
            "",
            "| Grupo Kouzina | Produtos com algum termo | Termos mais frequentes | Exemplo real de titulo |",
            "| --- | ---: | --- | --- |",
        ]
    )

    for group in TERM_GROUPS:
        top_terms = ", ".join(f"`{term}`:{count}" for term, count in term_hits[group].most_common(5))
        example = examples.get(group, {})
        title = str(example.get("title", "")).replace("|", "\\|")
        parent_asin = example.get("parent_asin", "")
        price = example.get("price", "")
        rating = example.get("average_rating", "")
        example_text = title
        if parent_asin:
            example_text += f" (`parent_asin={parent_asin}`, preco={price}, rating={rating})"
        lines.append(f"| {group} | {counts[group]} | {top_terms or '-'} | {example_text or '-'} |")

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Conta evidencias textuais do recorte Kouzina em metadados Amazon."
    )
    parser.add_argument("source", help="Caminho ou URL para meta_Home_and_Kitchen.jsonl.gz.")
    parser.add_argument("--limit", type=int, default=50000, help="Quantidade maxima de registros analisados.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.limit <= 0:
        raise ValueError("--limit deve ser maior que zero.")
    print(summarize(args.source, args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
