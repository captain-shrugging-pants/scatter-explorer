from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass(slots=True)
class Star:
    tic: int
    hd: Optional[str]
    pipecad: str
    M_mag: float


@dataclass(slots=True)
class ScatterDataset:
    x: np.ndarray
    y: np.ndarray
    ids: np.ndarray

    label: str = ""

    color: str | np.ndarray = "tab:blue"

    cmap: str = "viridis"
    vmin: float | None = None
    vmax: float | None = None

    show_colorbar: bool = False
    colorbar_label: str | None = None

    marker: str = "o"
    size: float = 15
    linewidth: float = 0.3
    alpha: float = 1.0
    picker: int = 5