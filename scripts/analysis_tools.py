def regional_mean(da, lat_range, lon_range):
    """Calcula la media espacial de un DataArray en una región rectangular."""

    region = da.sel(
        lat=slice(*lat_range),
        lon=slice(*lon_range)
    )

    return region.mean(
        dim=("lat", "lon"),
        skipna=True
    )


def enso_phase(oni_value):
    """Clasifica de manera simplificada un valor individual de ONI."""

    if oni_value >= 0.5:
        return "El Niño"
    elif oni_value <= -0.5:
        return "La Niña"
    else:
        return "Neutral"