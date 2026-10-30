# PROGRESS — bionfo_estudio

> Registro de estado del curso. Se actualiza **al cierre de cada lección/submódulo**, no en cada interacción.

## 0. Entorno verificado

| Elemento | Estado (2026-10-30) |
|---|---|
| SO | Ubuntu 24.04.5 LTS (WSL2) |
| Usuario | torpesaurio |
| Ruta proyecto | `~/projects/bionfo_estudio` |
| Python | 3.12.3 (sistema) — sin venv activo |
| R | 4.3.3 |
| Git | 2.43.0 — rama `main` |
| Remoto | `origin` → github.com/Torpesaurio/bionfo_estudio.git |
| Identidad Git | Sebastian Gahona / sbagahona@gmail.com |

### Estructura del repositorio
```
bionfo_estudio/
├── 01_datos_brutos/     # descargas originales (git: solo MANIFEST.txt)
├── 02_scripts_python/   # código Python
├── 03_scripts_r/        # código R
├── 04_resultados/       # salidas generadas (no versionadas)
├── 05_notebooks/        # exploración
├── PROGRESS.md
└── README.md
```

### Dependencias
| Herramienta | Estado |
|---|---|
| biopython | ❌ no instalado |
| pandas | ❌ no instalado |
| pip-audit | ❌ no instalado |
| BLAST+ | ❌ no instalado |
| samtools | ❌ no instalado |
| ClamAV | ❌ no instalado |
| sha256sum | ✅ disponible |

## 1. Estado de lecciones

| # | Lección | Estado | Script | Fecha |
|---|---|---|---|---|
| 1 | Caso HBB / anemia falciforme (rs334) | 🟡 en curso — hito 0/5 | — | — |

## 2. Decisiones de diseño
- Estructura numerada `01..05` (migrada con `git mv`).
- Python con `venv` local (`.venv`, ignorado por git). Sin conda por ahora.
- Datos crudos nunca versionados: se sustituyen por `MANIFEST.txt` con URL + fecha + `sha256`.
- Resultados en `04_resultados/`, regenerables desde los scripts.

## 3. Objetivos pendientes
- [ ] Hito 1: `.venv` + biopython/pandas + `pip-audit`.
- [ ] Hito 2: descarga RefSeq HBB + `MANIFEST.txt` con sha256.
- [ ] Hito 3: parseo, GC y traducción vs `NP_000508`.
- [ ] Hito 4: variante rs334 (GAG→GTG, E6V).
- [ ] Hito 5: cierre de lección (README, PROGRESS, clamscan, commit/push).
- [ ] Instalar BLAST+ y ClamAV (lecciones posteriores).

## 4. Bitácora
- **2026-10-30** — Sesión 0: auditoría del entorno, migración a carpetas numeradas 01–05, `.gitignore` reescrito, README base, creación de `PROGRESS.md`, remoto GitHub configurado.
