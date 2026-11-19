# 🪐 Planet or Impostor? Vetting TESS Transit Signals

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UBCAstronomyClub/Exoplanet_Vetting/blob/main/planet_or_impostor_workshop.ipynb)

A hands-on, 60-minute Python workshop for astronomy students and enthusiasts. You will find a transit signal in real TESS data, then learn how astronomers tell **real planets from impostors** such as eclipsing binaries, variable stars and instrumental glitches. The notebook uses [LEO-Vetter](https://pypi.org/project/leo-vetter/), a professional automated vetting tool.

**No installation needed.** Click the button above and the notebook opens in Google Colab. You'll need a Google account.

---

## What you'll do

| Time | Section | What happens |
|------|---------|--------------|
| 0-5 min | Background and setup | Learn the transit method and why vetting matters |
| 5-20 min | **Part 1: A real TESS light curve** | *Run only.* Download real data, flatten it, search for a period with Box Least Squares (BLS), and fold the light curve |
| 20-45 min | **Part 2a: Vetting by hand** | Four short fill-in exercises (size, odd/even, secondary eclipse, background) on five simulated stars: four impostors and one planet |
| 45-60 min | **Part 2b: LEO-Vetter** | Run the professional tool on the same five stars, compare its verdicts with yours, and discuss when a signal *could* be a planet |
| Take-home | **Part 3: Vet the real star** | Apply the same vetting to the real star from Part 1 |

## What you need

- A Google account (for Colab)
- Comfort reading short Python snippets and filling in a few lines
- No astronomy background required. The notebook explains the concepts as it goes.

## How to run it

1. Click the **Open in Colab** button at the top of this page.
2. Run the cells in order with **Shift + Enter**. The first code cell installs the libraries and takes about a minute.
3. Fill in the `None` placeholders in the exercise cells. Each exercise has collapsible hints, then a solution, and a test cell to check your work.

> The install cell may print warnings (for example about `fsspec` or `tpfmodel`). These are harmless.

## If the data download fails

The notebook downloads TESS data from [MAST](https://mast.stsci.edu), NASA's archive. If MAST is slow or down, the notebook has two backups. Both are controlled by the settings cell near the top:

1. **`USE_BACKUP = True`** (try this first): fetches a small copy of the data from this repository. Re-run the settings cell and the download cell.
2. **`USE_DRIVE = True`** (last resort, if the first backup also fails): download `data/tic287196418_s14.npz` from this repository, put it in your Google Drive in the folder named by `DRIVE_FOLDER` in the settings cell, set `USE_DRIVE = True`, re-run, and allow Colab to access your Drive when it asks.

## Repository contents

| File | Purpose |
|------|---------|
| `planet_or_impostor_workshop.ipynb` | The workshop notebook |
| `data/tic287196418_s14.npz` | Backup copy of the Part 1 light curve (TIC 287196418, TESS Sector 14), about 0.3 MB |
| `make_backup_npz.py` | Instructor script that creates the backup data files from MAST |

## For instructors

- **Before the session:** run the whole notebook once on Colab and check the timing. If it runs long, the easiest sections to trim are Exercise 4, the Lomb-Scargle demo and the optional extensions.
- **Making backup data for a different star:** run `python make_backup_npz.py TIC:SECTOR -o data` on Colab or any machine that can reach MAST, for example `python make_backup_npz.py 287196418:14 -o data`. It needs `lightkurve` installed. Commit the resulting `.npz` file to the `data/` folder.

## References and credits

- **LEO-Vetter:** Kunimoto et al. 2025, *LEO-Vetter: Fully Automated Flux- and Pixel-Level Vetting of TESS Planet Candidates to Support Occurrence Rates*, The Astronomical Journal 170, 280 ([arXiv:2509.10619](https://arxiv.org/abs/2509.10619)). Package: [pypi.org/project/leo-vetter](https://pypi.org/project/leo-vetter/)
- **Lightkurve:** [lightkurve.org](https://lightkurve.org), the Python library used for TESS light curves
- **TESS data:** [MAST](https://mast.stsci.edu), the Mikulski Archive for Space Telescopes
- **Check real candidates:** [ExoFOP-TESS](https://exofop.ipac.caltech.edu/tess/)