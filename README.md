# Proyecto: ENSO, SST y precipitación en Baja California

Este repositorio es el punto de partida para el proyecto final del minicurso
**Introducción a herramientas computacionales para Oceanografía Física**.

<!--
Reemplaza el título de arriba por un título que describa tu propio proyecto.
-->

## Pregunta

<!--
Escribe aquí una pregunta concreta que puedas explorar con los datos disponibles.

Ejemplos:
- ¿Cómo cambia la SST frente a Baja California durante eventos El Niño y La Niña?
- ¿Cómo se comporta la precipitación en Ensenada durante distintas fases de ENSO?
- ¿Existe una relación aparente entre ONI y anomalías regionales de SST?
-->

**Pregunta de investigación:** _Escribe aquí tu pregunta._

## Datos

Los datos disponibles para el proyecto incluyen:

- temperatura superficial del mar (SST) y anomalías de SST (SSTA) de NOAA OISST V2.1;
- Oceanic Niño Index (ONI);
- precipitación mensual acumulada en Ensenada.

Los archivos de datos se guardan localmente en `data/` y **no se versionan con Git**.

<!--
Completa esta sección:
- ¿Qué variables utilizaste?
- ¿Qué periodo analizaste?
- ¿Qué región geográfica seleccionaste?
- ¿Hay datos faltantes?
-->

## Métodos

<!--
Describe brevemente lo que hiciste, no cada línea de código.

Por ejemplo:
1. Abrí el NetCDF con xarray.
2. Seleccioné una región frente a Baja California.
3. Calculé una media espacial de SSTA.
4. Leí ONI/precipitación con pandas.
5. Alineé las series por fecha.
6. Comparé las variables mediante...
-->

_Describe aquí tu análisis._

## Resultados

<!--
Incluye una o dos figuras relevantes. Si guardas una figura en figures/, puedes
mostrarla aquí con:

![Descripción de la figura](figures/mi_figura.png)

Después escribe 2–4 frases distinguiendo:
1. lo que observas;
2. tu interpretación.
-->

_Resume aquí tus resultados principales._

## Cómo reproducir el análisis

El ambiente de Python utilizado en este proyecto está descrito en `environment.yml`.

Para crearlo por primera vez:

```bash
conda env create -f environment.yml
```

Para activarlo:

```bash
conda activate oceanografia
```

La primera vez que uses este ambiente con Jupyter, regístralo como un kernel:

```bash
python -m ipykernel install --user \
    --name oceanografia \
    --display-name "Python (oceanografia)"
```

Después, desde la raíz del proyecto:

```bash
jupyter lab
```

Dentro de JupyterLab verifica que el notebook esté usando:

**Kernel → Change Kernel → Python (oceanografia)**

> Activar un ambiente con `conda activate` y abrir JupyterLab no garantiza por sí solo
> que el notebook use ese mismo ambiente. El kernel determina qué instalación de Python
> ejecuta las celdas del notebook.

Si el proyecto contiene un script reproducible, indica aquí cómo ejecutarlo. Por ejemplo:

```bash
python scripts/make_summary_figure.py
```

## Estructura del repositorio

```text
.
├── data/            # Datos locales; Git ignora su contenido
├── notebooks/       # Exploración y análisis en Jupyter
├── scripts/         # Funciones y scripts reutilizables
├── figures/         # Figuras seleccionadas del proyecto
├── .gitignore
├── environment.yml
└── README.md
```

## Autora/or

**Nombre:** _Escribe aquí tu nombre._

Posgrado en Oceanografía Física, CICESE.

---

### Origen de este template

La estructura de este repositorio fue adaptada para el minicurso a partir del
[Sample Project Repository de ECCO Summer School 2025](https://github.com/ECCO-Summer-School/ESS25_sample_project_repository).
