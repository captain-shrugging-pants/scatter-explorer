from functools import lru_cache
from pathlib import Path

import numpy as np

from stellar_explorer.models import Star


class GapLoader:
    def __init__(
        self,
        lightcurve_dir,
        powerspectrum_dir,
    ):
        self.lightcurve_dir = Path(lightcurve_dir)
        self.powerspectrum_dir = Path(powerspectrum_dir)

    @lru_cache(maxsize=512)
    def load_lightcurve(self, tic: int, pipecad: str):
        path = self.lightcurve_dir / f"{tic}_{pipecad}.npz"
        print(path)
        if not path.exists():
            raise FileNotFoundError(f"Missing lightcurve file: {path}")

        data = np.load(path)

        return data["time"], data["flux"]

    @lru_cache(maxsize=512)
    def load_powerspectrum(self, tic: int, pipecad: str):
        path = self.powerspectrum_dir / f"{tic}_{pipecad}.npz"

        if not path.exists():
            raise FileNotFoundError(f"Missing powerspectrum file: {path}")

        data = np.load(path)

        return data["freq"], data["amp"]

    def load_star(self, star: Star):
        time, flux = self.load_lightcurve(star.tic, star.pipecad)
        freq, ampl = self.load_powerspectrum(star.tic, star.pipecad)

        return time, flux, freq, ampl
