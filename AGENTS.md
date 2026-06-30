# AGENTS.md

Guia curto para agentes que trabalharem neste repositorio.

## Contexto do projeto

Este repositorio apoia o TCC **Sistema de Recomendacao Baseado em Ontologias Fuzzy para Comercio Eletronico**. O foco e construir um prototipo de recomendacao para produtos premium/luxo de casa, cozinha, area gourmet e banheiro, usando o dataset Amazon Reviews 2023 - Home and Kitchen como base publica.

## Fontes de verdade

- Leia `arquitetura_agentes.md` antes de propor mudancas estruturais.
- Use `docs/architecture/contratos_agentes.md` como referencia para fronteiras dos agentes.
- Use `docs/methodology/recorte_kouzina_amazon.md` para decisoes de recorte de dominio.
- Consulte `investigacao_dataset.md` e `investigacao_tcc_revisao_dataset.md` para justificativas academicas.
- Consulte @raw/graphify-out/GRAPH_REPORT.md para acessar o mapa semântico, embasamento teórico e citações da literatura, evitando a leitura direta dos PDFs brutos.

## Regras de desenvolvimento

- Nao implemente logica definitiva de agentes sem aprovacao explicita.
- Não invente dados, sempre busca informações nos artigos que coloquei na pasta raw
- Valide o schema real do dataset antes de assumir campos como preco, marca, descricao, categoria ou rating.
- Mantenha dados brutos em `data/raw/` e nao altere arquivos originais.
- Separe scripts exploratorios de codigo de producao.
- Prefira configuracoes versionadas em `configs/` para filtros, regras fuzzy e parametros experimentais.
- Documente decisoes metodologicas em `docs/` antes ou junto da implementacao.

## Qualidade esperada

- Cada modulo deve ter entrada, saida e erro esperado bem definidos.
- Cada regra fuzzy deve ser rastreavel e explicavel.
- Cada experimento deve registrar dataset, filtros, parametros, metricas e sementes.
- Baselines devem usar o mesmo split do modelo fuzzy.
- Resultados devem ser reproduziveis.

## Comandos uteis

Explorar schema de um dataset:

```powershell
python scripts/data/explorar_schema.py caminho/para/arquivo.jsonl --limit 1000
python scripts/data/explorar_schema.py caminho/para/arquivo.csv --limit 1000
```

## Escopo atual

O projeto esta na fase de governanca, recorte metodologico e validacao de schema. Ainda nao avance para implementacao do motor fuzzy, ontologia definitiva, baselines ou API sem aprovacao do responsavel pelo TCC.