from __future__ import annotations

from pathlib import Path

from tcc_docx import export_markdown_chapter


INPUT_PATH = Path("outputs") / "Capitulo_2_Fundamentacao_Teorica.md"
OUTPUT_PATH = Path("outputs") / "Capitulo_2_Fundamentacao_Teorica.docx"


if __name__ == "__main__":
    export_markdown_chapter(
        INPUT_PATH,
        OUTPUT_PATH,
        document_title="2 Fundamentação Teórica",
    )
    print(f"Arquivo gerado: {OUTPUT_PATH}")
