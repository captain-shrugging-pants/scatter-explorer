import matplotlib.pyplot as plt

from stellar_explorer.catalog import StarCatalog
from stellar_explorer.loaders import GapLoader
from stellar_explorer.plotting import StarPlotter
from stellar_explorer.models import ScatterDataset


class StellarExplorer:
    def __init__(
        self,
        catalog_df,
        lightcurve_dir,
        powerspectrum_dir,
        figsize=(12, 5),
        dpi=120,
    ):
        self.catalog = StarCatalog(catalog_df)

        self.loader = GapLoader(
            lightcurve_dir=lightcurve_dir,
            powerspectrum_dir=powerspectrum_dir,
        )

        self.figsize = figsize
        self.dpi = dpi

        self.fig = None
        self.ax_scatter = None
        self.ax_lightcurve = None
        self.ax_spectrum = None

        self.selection_artist = None

        self.artist_to_dataset = {}

#     def show(
#         self,
#         datasets,
#         xlabel="x",
#         ylabel="y",
#         yscale="log",
#     ):

    def show(
        self,
        datasets,
        xlabel="x",
        ylabel="y",
        xscale="linear",
        yscale="log",
        xlim=None,
        ylim=None,
    ):
        self._build_figure()

        for dataset in datasets:
            self._add_dataset(dataset)

        self.ax_scatter.set_xlabel(xlabel)
        self.ax_scatter.set_ylabel(ylabel)
#         self.ax_scatter.set_yscale(yscale)
        self.ax_scatter.set_xscale(xscale)
        self.ax_scatter.set_yscale(yscale)

        if xlim is not None:
            self.ax_scatter.set_xlim(*xlim)

        if ylim is not None:
            self.ax_scatter.set_ylim(*ylim)

        self.ax_scatter.legend()

        self.selection_artist, = self.ax_scatter.plot(
            [],
            [],
            "o",
            markersize=15,
            mfc="none",
            mec="orange",
            lw=1.5,
        )

        self.fig.canvas.mpl_connect(
            "pick_event",
            self._on_pick,
        )

        plt.show()

    def _build_figure(self):
#         plt.ioff()

        self.fig = plt.figure(
            figsize=self.figsize,
            dpi=self.dpi,
        )

        gs = self.fig.add_gridspec(
            2,
            2,
            width_ratios=[1, 1],
            height_ratios=[1, 1],
            wspace=0.35,
            hspace=0.35,
        )

        self.ax_scatter = self.fig.add_subplot(gs[:, 0])
        self.ax_lightcurve = self.fig.add_subplot(gs[0, 1])
        self.ax_spectrum = self.fig.add_subplot(gs[1, 1])

        self.plotter = StarPlotter(
            self.ax_lightcurve,
            self.ax_spectrum,
        )

    def _add_dataset(self, dataset: ScatterDataset):
        artist = self.ax_scatter.scatter(
            dataset.x,
            dataset.y,
            s=dataset.size,
            c=dataset.color,
            cmap=dataset.cmap,
            vmin=dataset.vmin,
            vmax=dataset.vmax,
            marker=dataset.marker,
            lw=dataset.linewidth,
            alpha=dataset.alpha,
            picker=dataset.picker,
            rasterized=False,
            label=dataset.label,
        )

        self.artist_to_dataset[artist] = dataset

        if dataset.show_colorbar:
            cbar = self.fig.colorbar(
                artist,
                ax=self.ax_scatter,
                pad=0.02,
            )

            if dataset.colorbar_label is not None:
                cbar.set_label(dataset.colorbar_label)
                
                
    def _on_pick(self, event):
        artist = event.artist

        if artist not in self.artist_to_dataset:
            return

        dataset = self.artist_to_dataset[artist]

        index = event.ind[0]

        x = dataset.x[index]
        y = dataset.y[index]

        self.selection_artist.set_data([x], [y])

        star_id = dataset.ids[index]

        star = self.catalog.get_star(int(star_id))
        
        try:
            print(star)

            time, flux, freq, ampl = self.loader.load_star(star)

            print(time.shape, flux.shape)
            print(freq.shape, ampl.shape)

            self.plotter.plot_star(
                star=star,
                time=time,
                flux=flux,
                freq=freq,
                ampl=ampl,
            )

        except Exception as e:
            print("ERROR:", e)

#         time, flux, freq, ampl = self.loader.load_star(star)

#         self.plotter.plot_star(
#             star=star,
#             time=time,
#             flux=flux,
#             freq=freq,
#             ampl=ampl,
#         )

#         self.fig.canvas.draw_idle()
