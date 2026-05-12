import pandas as pd

from stellar_explorer.models import Star


class StarCatalog:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

        self._tic_index = self.df.set_index("tess")
        self._hd_index = self.df.set_index("HD")

    def get_star_by_tic(self, tic: int) -> Star:
        row = self._tic_index.loc[tic]

        return Star(
            tic=int(tic),
            hd=row["HD"],
            pipecad=row["pipecad"],
            M_mag=float(row["M_mag"]),
        )

    def get_star_by_hd(self, hd: str) -> Star:
        row = self._hd_index.loc[str(hd)]

        return Star(
            tic=int(row["tess"]),
            hd=row["HD"],
            pipecad=row["pipecad"],
            M_mag=float(row["M_mag"]),
        )

    def get_star(self, star_id):
        if isinstance(star_id, int):
            return self.get_star_by_tic(star_id)

        return self.get_star_by_hd(str(star_id))
