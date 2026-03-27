# 📊 Guía 2: Limpieza y Preprocesamiento de Datos (Pandas)

Este repositorio contiene la solución de la **Guía 2** del curso, cuyo objetivo es aplicar técnicas de **limpieza** y **preparación de datos** utilizando **Pandas** en Python.

---

## 🎯 Objetivo del proyecto

Procesar el archivo `notasdeestudiantes.csv`, que contiene datos académicos con múltiples problemas de calidad, y transformarlo en un **dataset limpio y listo para análisis**.

---

## 📁 Estructura del proyecto

```text
guia2/
│
├── data/                      # Archivos de datos originales
│   └── notasdeestudiantes.csv
│
├── notebooks/                 # Notebooks de Jupyter para análisis exploratorio
│   └── limpieza_analisis.ipynb
│
├── outputs/                   # Datos limpios y resultados generados
│   └── dataset_limpio.csv
│
├── src/                       # Módulos de Python reutilizables
│   ├── limpieza.py            # Funciones para limpiar y normalizar datos
│   └── analisis.py            # Funciones para análisis estadístico
│
└── README.md                  # Este archivo
```

---

## 🧹 Proceso de limpieza (`src/limpieza.py`)

Se implementa una función principal que realiza los siguientes pasos:

1. **Estandarización de columnas**
   - Convierte los nombres de columnas a minúsculas.
   - Elimina espacios innecesarios.

2. **Validación de estructura**
   - Verifica que existan las columnas esperadas:
     - `id_estudiante`, `nombre`, `carrera`, `nota_1`, `nota_2`, `nota_3`

3. **Limpieza de texto**
   - Elimina espacios extra al inicio y al final en `nombre` y `carrera`.
   - Normaliza nombres de carreras usando un diccionario.

4. **Conversión de notas**
   - Convierte notas a string.
   - Reemplaza comas por puntos (ej: `5,09` → `5.09`).
   - Convierte a tipo numérico (`float`).
   - Valores inválidos (`ausente`, `NR`, etc.) se transforman en `NaN`.

5. **Validación de rango**
   - Elimina valores fuera del rango válido **1.0 a 7.0**.

6. **Cálculo de promedio**
   - Crea la columna `nota` como el promedio de `nota_1`, `nota_2` y `nota_3`.

7. **Eliminación de duplicados**
   - Elimina filas completamente duplicadas.

8. **Eliminación de outliers (IQR)**
   - Aplica el método de rango intercuartílico sobre la columna `nota`.

9. **Imputación de valores faltantes**
   - Reemplaza valores faltantes con la **media** del dataset limpio.

---

## 📈 Análisis de datos (`src/analisis.py`)

Se generan las siguientes métricas:

### Resumen general
- Total de estudiantes
- Promedio general
- Nota mínima
- Nota máxima

### Promedio por carrera
- Promedio agrupado por `carrera`

---

## 📌 Resultados esperados

### Resumen general

| Métrica | Valor |
|---|---:|
| Total estudiantes | 178.00 |
| Promedio general | 4.72 |
| Nota mínima | 3.38 |
| Nota máxima | 6.18 |

### Promedio por carrera

| Carrera | Promedio |
|---|---:|
| Analista Programador | 4.62 |
| Data Science | 4.88 |
| Ingeniería Informática | 4.70 |
| Ingeniería en Redes | 4.75 |
