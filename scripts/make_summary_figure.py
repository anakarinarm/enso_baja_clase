import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

from analysis_tools import regional_mean


# 1. Leer datos
ds = xr.open_dataset("data/sst_baja_1981_2026.nc")

oni = pd.read_csv(
    "data/oni_mensual_1981_2026.csv",
    parse_dates=["time"]
).set_index("time")


# 2. Calcular una serie regional de SSTA
regional_ssta = regional_mean(
    ds.ssta,
    (28, 33),
    (-120, -115)
).to_series()


# 3. Alinear las series
analysis = pd.concat(
    [
        regional_ssta.rename("ssta_degC"),
        oni["oni_degC"]
    ],
    axis=1
)


# 4. Crear la figura
fig, axes = plt.subplots(
    nrows=2,
    figsize=(10, 6),
    sharex=True
)

analysis["ssta_degC"].plot(ax=axes[0])
axes[0].set_ylabel("SSTA (°C)")
axes[0].set_title("SSTA regional")

analysis["oni_degC"].plot(ax=axes[1])
axes[1].set_ylabel("ONI (°C)")
axes[1].set_xlabel("Tiempo")
axes[1].set_title("Oceanic Niño Index")

fig.tight_layout()
fig.savefig("figures/ssta_oni_summary.png", dpi=150)
