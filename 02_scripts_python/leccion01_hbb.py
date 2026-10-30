#!/usr/bin/env python3
"""
Lección 1 — HBB: del transcrito maduro a la proteína.

Caso de estudio: anemia falciforme (rs334).
Entrada : 01_datos_brutos/hbb_mrna.fasta      (NM_000518.5, 628 nt)
         01_datos_brutos/hbb_protein.fasta    (NP_000509.1, 147 aa)
Salida  : 04_resultados/leccion01_reporte.txt

Uso:
    source .venv/bin/activate
    python 02_scripts_python/leccion01_hbb.py
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from Bio import SeqIO
from Bio.Data import CodonTable
from Bio.SeqUtils import gc_fraction

RAIZ = Path(__file__).resolve().parents[1]

# Tabla 1 = código genético estándar. stop_codons = TAA, TAG, TGA
STOP = set(CodonTable.unambiguous_dna_by_id[1].stop_codons)


def leer_unico(ruta: Path):
    """SeqIO.read exige EXACTAMENTE un registro en el archivo.

    SeqIO.parse devuelve un iterador (para multi-FASTA); read falla si hay
    más de uno, lo que aquí es deseable: detecta descargas corruptas o
    concatenadas por error.
    """
    return SeqIO.read(ruta, "fasta")


def localizar_cds(seq) -> tuple[int, int]:
    """Devuelve (inicio, fin) 0-based de la CDS, con el codón de parada incluido.

    Recorre en pasos de 3 desde el ATG inicial hasta el primer codón de
    parada en el mismo marco de lectura. Ese es el ORF real: el 3' UTR que
    sigue no forma parte de la proteína.
    """
    s = str(seq).upper()
    inicio = s.find("ATG")
    if inicio < 0:
        return -1, -1
    for i in range(inicio, len(s) - 2, 3):
        if s[i:i + 3] in STOP:
            return inicio, i + 3
    return inicio, len(s)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mrna", type=Path, default=RAIZ / "01_datos_brutos/hbb_mrna.fasta")
    p.add_argument("--protein", type=Path, default=RAIZ / "01_datos_brutos/hbb_protein.fasta")
    p.add_argument("--out", type=Path, default=RAIZ / "04_resultados/leccion01_reporte.txt")
    args = p.parse_args()

    mrna = leer_unico(args.mrna)
    ref = leer_unico(args.protein)
    seq = mrna.seq

    lineas: list[str] = []
    add = lineas.append

    add("=" * 62)
    add("LECCIÓN 1 — HBB / anemia falciforme")
    add("=" * 62)
    add(f"Transcrito : {mrna.id}  ({mrna.description})")
    add(f"Proteína   : {ref.id}  ({ref.description})")
    add("")

    # --- 1. Composición nucleotídica -------------------------------------
    conteo = Counter(str(seq).upper())
    total = len(seq)
    add(f"Longitud del mRNA : {total} nt")
    add(f"Composición       : A={conteo['A']} C={conteo['C']} "
        f"G={conteo['G']} T={conteo['T']}")
    add(f"GC global         : {gc_fraction(seq) * 100:.2f} %")
    add("")

    # --- 2. Localización de la CDS ---------------------------------------
    inicio, fin = localizar_cds(seq)
    if inicio < 0:
        add("ERROR: no se encontró codón de inicio ATG.")
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text("\n".join(lineas), encoding="utf-8")
        return 1

    cds = seq[inicio:fin]

    add(f"Primer ATG (0-based) : {inicio}")
    add(f"5' UTR               : {inicio} nt")
    add(f"CDS (ATG→stop)       : {len(cds)} nt  = {len(cds) // 3} codones")
    add(f"3' UTR               : {total - fin} nt")
    add(f"Codón de parada      : {cds[-3:]}")
    add("")

    # --- 3. Traducción ----------------------------------------------------
    # cds[:-3] excluye el codón de parada: no codifica aminoácido.
    proteina = cds[:-3].translate()
    add(f"Traducción           : {len(proteina)} aa")
    add(f"Referencia NCBI      : {len(ref.seq)} aa")
    add("")

    # --- 4. Comparación con la proteína de referencia --------------------
    identicas = str(proteina) == str(ref.seq)
    add(f"¿Idéntica a {ref.id}? {'SÍ' if identicas else 'NO'}")

    if not identicas:
        diferencias = [
            (i + 1, a, b)
            for i, (a, b) in enumerate(zip(str(proteina), str(ref.seq)))
            if a != b
        ]
        add(f"Discrepancias: {len(diferencias)}")
        for pos, mia, esperada in diferencias[:10]:
            add(f"  posición {pos}: {mia} != {esperada}")
    add("")

    add(f"Primeros 20 aa : {proteina[:20]}")
    add(f"Últimos 10 aa  : {proteina[-10:]}")
    add("")

    # --- 5. GC de la CDS vs global ---------------------------------------
    add(f"GC de la CDS   : {gc_fraction(cds) * 100:.2f} %")
    add("")

    # --- 6. La variante rs334 (HbS) ---------------------------------------
    add("-" * 62)
    add("Variante rs334 — anemia falciforme (HbS)")
    add("-" * 62)
    # Numeración HGVS cuenta desde la Met iniciadora -> codón 7.
    # La literatura clásica la cita como Glu6Val sobre la proteína madura,
    # que pierde esa Met. Ambas describen el MISMO cambio.
    idx = 6                      # 0-based: séptimo codón
    codon = cds[idx * 3: idx * 3 + 3]
    pos = idx * 3 + 1            # 1-based dentro de la CDS
    mutado = codon[:1] + "T" + codon[2:]

    add(f"Codón 7 (HGVS)      : {codon}  (c.{pos}-{pos + 2})")
    add(f"Aminoácido          : {codon.translate()}")
    add(f"Mutación c.20A>T    : {codon} → {mutado}")
    add(f"Aminoácido mutado   : {mutado.translate()}  (Glu → Val)")
    add("")
    add("Contexto: la sustitución elimina una carga negativa en la superficie")
    add("de la β-globina. La HbS desoxigenada agrega en polímeros que deforman")
    add("el eritrocito (drepnocito) y obstruyen la microcirculación.")

    texto = "\n".join(lineas)
    print(texto)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(texto + "\n", encoding="utf-8")
    print(f"\n[ok] Reporte guardado en {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
