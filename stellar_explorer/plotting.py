import numpy as np


class StarPlotter:
    def __init__(self, ax_lightcurve, ax_spectrum):
        self.ax_lightcurve = ax_lightcurve
        self.ax_spectrum = ax_spectrum

    def plot_star(
        self,
        star,
        time: np.ndarray,
        flux: np.ndarray,
        freq: np.ndarray,
        ampl: np.ndarray,
        xlim=(0, 100),
    ):
        self._plot_lightcurve(star, time, flux)
        self._plot_spectrum(star, freq, ampl, xlim=xlim)

    def _plot_lightcurve(self, star, time, flux):
        ax = self.ax_lightcurve
        ax.clear()

        star_name = (
            f"HD {star.hd}"
            if star.hd not in ["none", "no_simbad"]
            else f"TIC {star.tic}"
        )

        fbarac = 10 ** ((star.M_mag + 1.4) / 3.01)

        title = (
            f"{star_name}, "
            f"$M_G$={star.M_mag:.2f}, "
            f"$f_B$={fbarac:.2f}"
        )

        ax.set_title(title, fontsize=9)

        ax.scatter(
            time,
            flux,
            s=2,
            lw=0.5,
            rasterized=True,
        )
        

        ax.set_xlabel("Time")
        ax.set_ylabel("Flux")

    def _plot_spectrum(
        self, star,
        freq,
        ampl,
        xlim=(0, 100),
    ):
        ax = self.ax_spectrum
        ax.clear()
        fbarac = 10 ** ((star.M_mag + 1.4) / 3.01)
        idx = (freq >= xlim[0]) & (freq <= xlim[1])

        ax.plot(
            freq[idx],
            ampl[idx],
            rasterized=True,
        )
        ax.axvline(x=fbarac, linestyle='--', color='red')
        ax.axvline(x=2*fbarac/3, linestyle='--', color='green')
        ax.set_xlim(*xlim)
        ax.set_xlabel("Frequency")
        ax.set_ylabel("Amplitude")
