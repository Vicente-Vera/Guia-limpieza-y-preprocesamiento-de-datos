# Guia-limpieza-y-preprocesamiento-de-datos

📊 Guía 2: Limpieza y Preprocesamiento de Datos

Este repositorio contiene la solución de la Guía 2 del curso, cuyo objetivo es aplicar técnicas de limpieza y preparación de datos utilizando la biblioteca Pandas de Python.

📁 Estructura del Proyecto

El proyecto sigue la estructura de carpetas recomendada para mantener el código organizado y reutilizable:

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
🎯 Objetivo del Proyecto

Procesar el archivo notasdeestudiantes.csv, que contiene datos académicos con múltiples problemas de calidad, y transformarlo en un dataset limpio y listo para análisis.

🧹 Proceso de Limpieza (src/limpieza.py)

Se implementó una función principal que realiza los siguientes pasos:

Estandarización de Columnas:
Se convierten los nombres de las columnas a minúsculas y se eliminan espacios innecesarios.
Validación de Estructura:
Se verifica que todas las columnas esperadas (id_estudiante, nombre, carrera, nota_1, nota_2, nota_3) estén presentes.
Limpieza de Texto:
Se eliminan espacios extras al inicio y final de los campos de texto (nombre, carrera).
Se normalizan los nombres de las carreras usando un diccionario.
Conversión de Notas:
Se convierten todas las notas a tipo string.
Se reemplazan comas por puntos (ej: 5,09 → 5.09).
Se convierten a tipo numérico (float).
Valores inválidos (ausente, NR, etc.) se transforman en NaN.
Validación de Rango de Notas:
Se eliminan valores fuera del rango válido 1.0 a 7.0.
Cálculo de Promedio:
Se crea la columna nota como promedio de nota_1, nota_2 y nota_3.
Eliminación de Duplicados:
Se eliminan filas duplicadas completas.
Eliminación de Outliers (IQR):
Se aplica el método de rango intercuartil sobre la columna nota.
Imputación de Valores Faltantes:
Se reemplazan valores faltantes con la media del dataset limpio.

📈 Análisis de Datos (src/analisis.py)

Se generan las siguientes métricas:

Resumen General:
Total de estudiantes
Promedio general
Nota mínima
Nota máxima
Promedio por Carrera:
Promedio agrupado por carrera

📌 Resultados Esperados

Resumen General:
Total estudiantes 178.00
Promedio general 4.72
Nota mínima 3.38
Nota máxima 6.18

Promedio por Carrera:

Carrera	Promedio
Analista Programador	4.62
Data Science	4.88
Ingeniería Informática	4.70
Ingeniería en Redes	4.75
