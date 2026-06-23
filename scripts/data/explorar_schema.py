#!/usr/bin/env python
"""Explora o schema inicial de arquivos CSV, JSONL ou JSON.

Uso:
    python scripts/data/explorar_schema.py data/raw/arquivo.jsonl --limit 1000
    python scripts/data/explorar_schema.py data/raw/arquivo.csv --limit 1000

O script le apenas uma amostra inicial para evitar carregar datasets grandes em
memoria. Tambem aceita arquivos compactados com gzip, como .jsonl.gz e .csv.gz.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from collections import Counter, defaultdict
from itertools import islice
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List


Row = Dict[str, Any]


def open_text(path: Path):
    if path.suffix.lower() == ".gz":
        return gzip.open(path, mode="rt", encoding="utf-8", newline="")
    return path.open(mode="r", encoding="utf-8", newline="")


def normalized_suffixes(path: Path) -> List[str]:
    return [suffix.lower() for suffix in path.suffixes]


def detect_format(path: Path, explicit_format: str | None) -> str:
    if explicit_format:
        return explicit_format

    suffixes = normalized_suffixes(path)
    suffixes_without_gz = [suffix for suffix in suffixes if suffix != ".gz"]
    last_suffix = suffixes_without_gz[-1] if suffixes_without_gz else ""

    if last_suffix == ".csv":
        return "csv"
    if last_suffix in {".jsonl", ".ndjson"}:
        return "jsonl"
    if last_suffix == ".json":
        return "json"

    raise ValueError(
        "Nao foi possivel detectar o formato. Use --format csv, jsonl ou json."
    )


def iter_csv(path: Path) -> Iterator[Row]:
    with open_text(path) as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            yield dict(row)


def iter_jsonl(path: Path) -> Iterator[Row]:
    with open_text(path) as file_obj:
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
            else:
                yield {"value": value}


def iter_json(path: Path) -> Iterator[Row]:
    with open_text(path) as file_obj:
        value = json.load(file_obj)

    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                yield item
            else:
                yield {"value": item}
        return

    if isinstance(value, dict):
        records = value.get("data") or value.get("records") or value.get("items")
        if isinstance(records, list):
            for item in records:
                if isinstance(item, dict):
                    yield item
                else:
                    yield {"value": item}
        else:
            yield value
        return

    yield {"value": value}


def iter_rows(path: Path, file_format: str) -> Iterator[Row]:
    if file_format == "csv":
        return iter_csv(path)
    if file_format == "jsonl":
        return iter_jsonl(path)
    if file_format == "json":
        return iter_json(path)
    raise ValueError(f"Formato nao suportado: {file_format}")


def type_name(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int) and not isinstance(value, bool):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "":
            return "empty_string"
        lower_value = stripped.lower()
        if lower_value in {"true", "false"}:
            return "str_bool_like"
        try:
            int(stripped)
            return "str_int_like"
        except ValueError:
            pass
        try:
            float(stripped)
            return "str_float_like"
        except ValueError:
            pass
        return "str"
    if isinstance(value, list):
        return "list"
    if isinstance(value, dict):
        return "dict"
    return type(value).__name__


def is_null_like(value: Any) -> bool:
    return value is None or (isinstance(value, str) and value.strip() == "")


def collect_stats(rows: Iterable[Row], limit: int) -> tuple[List[Row], List[str], dict]:
    sample_rows = list(islice(rows, limit))
    columns = sorted({column for row in sample_rows for column in row.keys()})

    stats = {
        "types": defaultdict(Counter),
        "nulls": Counter(),
        "present": Counter(),
        "missing": Counter(),
    }

    for row in sample_rows:
        row_keys = set(row.keys())
        for column in columns:
            if column not in row_keys:
                stats["missing"][column] += 1
                stats["nulls"][column] += 1
                stats["types"][column]["missing"] += 1
                continue

            value = row[column]
            stats["present"][column] += 1
            stats["types"][column][type_name(value)] += 1
            if is_null_like(value):
                stats["nulls"][column] += 1

    return sample_rows, columns, stats


def print_report(path: Path, file_format: str, limit: int, rows: List[Row], columns: List[str], stats: dict) -> None:
    print("=== Exploracao de schema ===")
    print(f"Arquivo: {path}")
    print(f"Formato: {file_format}")
    print(f"Linhas analisadas: {len(rows)}")
    print(f"Limite solicitado: {limit}")
    print(f"Total de colunas observadas: {len(columns)}")
    print()

    print("=== Colunas observadas ===")
    for column in columns:
        print(f"- {column}")
    print()

    print("=== Tipos e nulos por coluna ===")
    if not columns:
        print("Nenhuma coluna encontrada na amostra.")
        return

    header = f"{'coluna':40} {'tipos observados':35} {'presentes':>10} {'nulos':>10} {'ausentes':>10}"
    print(header)
    print("-" * len(header))

    for column in columns:
        type_summary = ", ".join(
            f"{type_key}:{count}" for type_key, count in stats["types"][column].most_common()
        )
        print(
            f"{column[:40]:40} "
            f"{type_summary[:35]:35} "
            f"{stats['present'][column]:10} "
            f"{stats['nulls'][column]:10} "
            f"{stats['missing'][column]:10}"
        )

    print()
    print("=== Exemplo da primeira linha ===")
    if rows:
        print(json.dumps(rows[0], ensure_ascii=False, indent=2)[:4000])
    else:
        print("Arquivo sem linhas na amostra.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Explora colunas, tipos e valores nulos de uma amostra do dataset."
    )
    parser.add_argument("path", help="Caminho para arquivo .csv, .jsonl, .json ou variantes .gz.")
    parser.add_argument(
        "--format",
        choices=["csv", "jsonl", "json"],
        default=None,
        help="Formato do arquivo. Se omitido, sera inferido pela extensao.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=1000,
        help="Quantidade maxima de linhas analisadas. Padrao: 1000.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.path)

    if args.limit <= 0:
        raise ValueError("--limit deve ser maior que zero.")
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
    if not path.is_file():
        raise ValueError(f"O caminho informado nao e um arquivo: {path}")

    file_format = detect_format(path, args.format)
    rows_iter = iter_rows(path, file_format)
    rows, columns, stats = collect_stats(rows_iter, args.limit)
    print_report(path, file_format, args.limit, rows, columns, stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
