import pandas as pd


#Diccionario para normalizar nombres de carrera
Carreras_validas = {
    "ing. informática": "Ingeniería en Informática",
    "ingeniería en informática": "Ingeniería en Informática",
    "analista programador": "Analista Programador",
    "data science": "Data Science",
    "ingeniería en redes": "Ingeniería en Redes",
}

#Rango válido de notas
NOTA_MIN = 1.0
NOTA_MAX = 7.0

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:

    #Copiar dataframe original
    df = df.copy()

    #Normalizar nombres de columnas (minúsculas y sin espacios)
    df.columns = df.columns.str.lower().str.strip()

    #Validar columnas necesarias
    requeridas = {"nota_1", "nota_2", "nota_3", "carrera", "nombre"}
    faltantes = requeridas - set(df.columns)
    if faltantes:
        raise ValueError(f"Columnas faltantes: {faltantes}")

    #Limpiar espacios en texto
    for col in ["nombre", "carrera"]:
        df[col] = df[col].str.strip()

    #Normalizar nombres de carrera
    df["carrera"] = (
        df["carrera"]
        .str.lower()
        .str.strip()
        .map(Carreras_validas)
    )


    #Convertir notas (coma → punto)
    for col in ["nota_1", "nota_2", "nota_3"]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .pipe(pd.to_numeric, errors='coerce')
        )

    #Convertir a número y validar rango
    for col in ["nota_1", "nota_2", "nota_3"]:
       
        df[col] = df[col].where(df[col].between(NOTA_MIN, NOTA_MAX))

    #Calcular promedio
    df["nota"] = df[["nota_1", "nota_2", "nota_3"]].mean(axis=1)

    #Eliminar duplicados
    df = df.drop_duplicates()

    #Eliminar outliers con IQR
    q1 = df["nota"].quantile(0.25)
    q3 = df["nota"].quantile(0.75)
    iqr = q3 - q1

    li = max(q1 - 1.5 * iqr, NOTA_MIN)
    ls = min(q3 + 1.5 * iqr, NOTA_MAX)

    df = df[(df["nota"] >= li) & (df["nota"] <= ls)]

    #Rellenar valores faltantes con el promedio
    df["nota"] = df["nota"].fillna(df["nota"].mean())

    return df