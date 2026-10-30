# 🧬 bionfo_estudio

Portafolio académico de bioinformática: casos de estudio con **datos públicos reales** (NCBI, Ensembl, GEO), reproducibles de principio a fin.

Entorno: **WSL2 · Ubuntu 24.04 LTS** · Python 3.12 · R 4.3.3

## Estructura

| Carpeta | Contenido | ¿Se versiona? |
|---|---|---|
| `01_datos_brutos/` | Descargas originales de bases públicas (FASTA, matrices) | No — solo `MANIFEST.txt` |
| `02_scripts_python/` | Scripts y pipelines en Python | Sí |
| `03_scripts_r/` | Análisis estadístico y visualización en R | Sí |
| `04_resultados/` | Tablas, figuras e informes generados | No — se regeneran |
| `05_notebooks/` | Cuadernos de exploración | Sí |

## Política de datos y reproducibilidad

Ningún dato crudo se sube al repositorio. En su lugar se conserva `01_datos_brutos/MANIFEST.txt`, que registra para cada archivo:

- URL de descarga exacta (con versión/accesión)
- Fecha de descarga
- Tamaño en bytes
- Hash `sha256` verificado contra la fuente

Así cualquiera puede reconstruir el análisis desde cero y comprobar que el archivo no fue alterado.

## Entorno

```bash
cd ~/projects/bionfo_estudio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # cuando exista
```

## Progreso

El estado del curso, las dependencias instaladas y los objetivos pendientes se registran en [`PROGRESS.md`](PROGRESS.md).

## Lecciones

| # | Caso de estudio | Datos | Estado |
|---|---|---|---|
| 1 | HBB y anemia falciforme (rs334) | RefSeq `NM_000518`, `NP_000508` | 🟡 en curso |
