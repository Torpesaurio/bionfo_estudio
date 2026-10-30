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
- Hash `sha256`

Así cualquiera puede reconstruir el análisis desde cero y comprobar que el archivo no fue alterado.

## Entorno

```bash
cd ~/projects/bionfo_estudio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependencias auditadas con `pip-audit` antes de su uso.

---

## Lección 1 — HBB y anemia falciforme (rs334)

**Pregunta biológica:** ¿cómo un solo cambio de base en el gen de la β-globina produce una enfermedad?

| Recurso | Accesión | Tamaño |
|---|---|---|
| mRNA de HBB | `NM_000518.5` | 628 nt |
| Proteína de referencia | `NP_000509.1` | 147 aa |
| Variante | `rs334` (dbSNP) | chr11:5227002 A>T |

### Resultados

| Métrica | Valor |
|---|---|
| 5' UTR | 50 nt |
| CDS (ATG→TAA) | 444 nt = 148 codones |
| 3' UTR | 134 nt |
| GC global | 51.27 % |
| GC de la CDS | 56.08 % |
| Traducción vs `NP_000509.1` | idéntica (147/147 aa) |

### Variante detectada

```
Codón 7 (HGVS)   : GAG  →  GTG     (c.20A>T)
Aminoácido       : Glu  →  Val     (p.Glu7Val)
Clasificación    : missense_variant
```

La sustitución elimina una carga negativa en la superficie de la β-globina. La hemoglobina S desoxigenada polimeriza, deforma el eritrocito (drepnocito) y obstruye la microcirculación.

> **Nota de nomenclatura:** la literatura clásica cita esta variante como **Glu6Val**, porque numera sobre la proteína madura (sin la Met iniciadora). HGVS numera sobre el precursor → **Glu7Val**. Mismo cambio, distinta referencia.

### Reproducir

```bash
source .venv/bin/activate
python 02_scripts_python/leccion01_hbb.py
# -> 04_resultados/leccion01_reporte.txt
```

---

## Progreso

El estado del curso, las dependencias instaladas y los objetivos pendientes se registran en [`PROGRESS.md`](PROGRESS.md).

## Lecciones

| # | Caso de estudio | Datos | Estado |
|---|---|---|---|
| 1 | HBB y anemia falciforme (rs334) | `NM_000518.5`, `NP_000509.1` | ✅ completada |
