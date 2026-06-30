#!/usr/bin/env python
"""Explora o schema inicial de arquivos CSV, JSONL ou JSON.

Uso:
    python scripts/data/explorar_schema.py data/raw/arquivo.jsonl --limit 1000
    python scripts/data/explorar_schema.py data/raw/arquivo.csv --limit 1000
    python scripts/data/explorar_schema.py https://exemplo/arquivo.jsonl.gz --limit 1000

O script le apenas uma amostra inicial para evitar carregar datasets grandes em
memoria. Tambem aceita arquivos compactados com gzip, como .jsonl.gz e .csv.gz,
inclusive quando informados por URL HTTP/HTTPS.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import csv
import gzip
import io
import json
from collections import Counter, defaultdict
from itertools import islice
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List
from urllib.parse import urlparse
from urllib.request import Request, urlopen


Row = Dict[str, Any]


def is_url(source: str) -> bool:
    parsed = urlparse(source)
    return parsed.scheme in {"http", "https"}


def source_suffixes(source: str) -> List[str]:
    if is_url(source):
        return [suffix.lower() for suffix in Path(urlparse(source).path).suffixes]
    return [suffix.lower() for suffix in Path(source).suffixes]


@contextmanager
def open_text(source: str):
    if is_url(source):
        request = Request(source, headers={"User-Agent": "recommendation-fuzzy-schema/1.0"})
        response = urlopen(request, timeout=60)
        try:
            binary_stream = response
            if source_suffixes(source)[-1:] == [".gz"]:
                binary_stream = gzip.GzipFile(fileobj=response)
            text_stream = io.TextIOWrapper(binary_stream, encoding="utf-8", newline="")
            try:
                yield text_stream
            finally:
                text_stream.close()
        finally:
            response.close()
        return

    path = Path(source)
    if path.suffix.lower() == ".gz":
        with gzip.open(path, mode="rt", encoding="utf-8", newline="") as file_obj:
            yield file_obj
        return

    with path.open(mode="r", encoding="utf-8", newline="") as file_obj:
        yield file_obj


def detect_format(source: str, explicit_format: str | None) -> str:
    if explicit_format:
        return explicit_format

    suffixes = source_suffixes(source)
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


def iter_csv(source: str) -> Iterator[Row]:
    with open_text(source) as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            yield dict(row)


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
            else:
                yield {"value": value}


def iter_json(source: str) -> Iterator[Row]:
    with open_text(source) as file_obj:
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


def iter_rows(source: str, file_format: str) -> Iterator[Row]:
    if file_format == "csv":
        return iter_csv(source)
    if file_format == "jsonl":
        return iter_jsonl(source)
    if file_format == "json":
        return iter_json(source)
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
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    if isinstance(value, (list, dict)):
        return len(value) == 0
    return False


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


def print_report(source: str, file_format: str, limit: int, rows: List[Row], columns: List[str], stats: dict) -> None:
    print("=== Exploracao de schema ===")
    print(f"Fonte: {source}")
    print(f"Formato: {file_format}")
    print(f"Linhas analisadas: {len(rows)}")
    print(f"Limite solicitado: {limit}")
    print(f"Total de colunas observadas: {len(columns)}")
    print()

    print("=== Colunas observadas ===")
    for column in columns:
        print(f"- {column}")
    print()

    print("=== Tipos e nulos/vazios por coluna ===")
    if not columns:
        print("Nenhuma coluna encontrada na amostra.")
        return

    header = f"{'coluna':40} {'tipos observados':35} {'presentes':>10} {'nulos/vazios':>13} {'ausentes':>10}"
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
            f"{stats['nulls'][column]:13} "
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
    parser.add_argument("path", help="Caminho ou URL para arquivo .csv, .jsonl, .json ou variantes .gz.")
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
    source = args.path

    if args.limit <= 0:
        raise ValueError("--limit deve ser maior que zero.")
    if not is_url(source):
        path = Path(source)
        if not path.exists():
            raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
        if not path.is_file():
            raise ValueError(f"O caminho informado nao e um arquivo: {path}")

    file_format = detect_format(source, args.format)
    rows_iter = iter_rows(source, file_format)
    rows, columns, stats = collect_stats(rows_iter, args.limit)
    print_report(source, file_format, args.limit, rows, columns, stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
