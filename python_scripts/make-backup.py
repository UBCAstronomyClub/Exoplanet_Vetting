"""Instructor script: download TESS light curves from MAST and save small backup .npz files
for the workshop repo.

Usage (on Colab or any machine that can reach MAST):

    pip install lightkurve
    python make_backup_npz.py 287196418:14 -o data

Each argument is TIC:SECTOR. Files are saved as data/tic<TIC>_s<SECTOR>.npz (about 0.4 MB each),
which is the name the workshop notebook expects. Commit the data/ folder to the (public) repo.
"""
import argparse
import os

import numpy as np


def make_backup(tic, sector, out_dir, lc=None):
    """Download (or accept) one SPOC 2-minute light curve and save the arrays the notebook needs."""
    if lc is None:
        import lightkurve as lk
        search = lk.search_lightcurve(f"TIC {tic}", author="SPOC", sector=sector, exptime=120)
        lc = search.download()
        if lc is None:
            raise RuntimeError(f"No SPOC 2-minute data found for TIC {tic}, sector {sector}")
    lc = lc.remove_nans().normalize()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"tic{tic}_s{sector}.npz")
    bkg = np.asarray(lc["sap_bkg"].value if hasattr(lc["sap_bkg"], "value") else lc["sap_bkg"], dtype=float)
    np.savez_compressed(
        path,
        time=np.asarray(lc.time.value, dtype=np.float64),     # keep full precision for the time stamps
        flux=np.asarray(lc.flux.value, dtype=np.float32),
        flux_err=np.asarray(lc.flux_err.value, dtype=np.float32),
        bkg=bkg.astype(np.float32),
    )
    print(f"saved {path}  ({os.path.getsize(path) / 1e3:.0f} KB, {len(lc)} points)")
    return path


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="+", help="TIC:SECTOR pairs, e.g. 287196418:14")
    ap.add_argument("-o", "--out", default="data", help="output folder (default: data)")
    args = ap.parse_args()
    for t in args.targets:
        tic, sector = t.split(":")
        make_backup(int(tic), int(sector), args.out)