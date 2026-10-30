# PROGRESS — bionfo_estudio

> Registro de estado del curso. Se actualiza **al cierre de cada lección/submódulo**, no en cada interacción.

## 0. Entorno verificado

| Elemento | Estado (2026-10-30) |
|---|---|
| SO | Ubuntu 24.04.5 LTS (WSL2) |
| Usuario | torpesaurio |
| Ruta proyecto | `~/projects/bionfo_estudio` |
| Python | 3.12.3 (venv en `.venv`) |
| R | 4.3.3 |
| Git | 2.43.0 — rama `main`, remoto `origin` (SSH) |
| Identidad Git | Sebastian Gahona / sbagahona@gmail.com |
| Autenticación GitHub | SSH ed25519 · huella `SHA256:sgmOogOpdmvBoqROP4CPzKhS8aTNd+IAFkAm4oRQgeQ` |

### Estructura del repositorio
```
bionfo_estudio/
├── 01_datos_brutos/     # descargas originales (git: solo MANIFEST.txt)
├── 02_scripts_python/   # código Python
├── 03_scripts_r/        # código R
├── 04_resultados/       # salidas generadas (no versionadas)
├── 05_notebooks/        # exploración
├── PROGRESS.md
├── README.md
└── requirements.txt
```

### Dependencias (venv, auditadas)
| Herramienta | Versión | Estado |
|---|---|---|
| biopython | 1.88 | ✅ |
| pandas | 3.1.0 | ✅ |
| numpy | 2.5.4 | ✅ (transitiva) |
| pip-audit | 2.10.1 | ✅ última auditoría: 0 vulnerabilidades |
| BLAST+ | — | ❌ pendiente |
| samtools | — | ❌ pendiente |
| ClamAV | — | ❌ pendiente (requiere sudo apt) |

## 1. Estado de lecciones

| # | Lección | Estado | Script | Fecha |
|---|---|---|---|---|
| 1 | HBB / anemia falciforme (rs334) | ✅ completada | `02_scripts_python/leccion01_hbb.py` | 2026-10-30 |

### Resultados clave — Lección 1
- `NM_000518.5`: 628 nt · 5'UTR 50 · CDS 444 (148 codones) · 3'UTR 134.
- Traducción idéntica a `NP_000509.1` (147 aa).
- Variante validada contra dbSNP: `NM_000518.5:c.20A>T`, `p.Glu7Val` (= Glu6Val clásico), `missense_variant`.

## 2. Decisiones de diseño
- Estructura numerada `01..05` (migrada con `git mv`).
- Python con `venv` local (`.venv`, ignorado). Sin conda por ahora.
- Datos crudos nunca versionados: se sustituyen por `MANIFEST.txt` con URL + fecha + `sha256`.
- Resultados en `04_resultados/`, regenerables desde los scripts.
- Accessions **nunca** se asumen: se validan por la línea de definición y por `elink`.

## 3. Objetivos pendientes
- [ ] Evaluación de la Lección 1 (tarea + cuestionario) — en curso.
- [ ] Instalar BLAST+ (alineamiento de HbS vs HbA contra UniProt P68871).
- [ ] Instalar ClamAV y establecer escaneo periódico del proyecto.
- [ ] Lección 2: expresión diferencial con datos reales de GEO.

## 4. Bitácora
- **2026-10-30** — Sesión 0: auditoría del entorno, migración a carpetas numeradas, `.gitignore` reescrito, README base, `PROGRESS.md`, remoto GitHub por SSH y primer push.
- **2026-10-30** — Lección 1: descarga E-utilities con manifiesto y sha256, script de parseo/traducción, validación de rs334 contra dbSNP, README documentado.
