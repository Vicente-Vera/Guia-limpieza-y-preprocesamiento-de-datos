import pandas as pd

# Resumen general
def resumen_general(df: pd.DataFrame) -> pd.Series:

    return pd.Series({
        "total_estudiantes": df.shape[0],
        "promedio_general": df["nota"].mean(),
        "nota_minima": df["nota"].min(),
        "nota_maxima": df["nota"].max()
    })

# Promedio por carrera
def promedio_por_carrera(df: pd.DataFrame) -> pd.DataFrame:

    return (
        df
        .groupby("carrera")["nota"]
        .mean()
        .reset_index(name="promedio")
    )