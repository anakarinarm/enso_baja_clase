# Preparación del repositorio plantilla en GitHub

1. Crea un repositorio nuevo en tu cuenta de GitHub, por ejemplo:
   `enso-baja-project-template`.
2. Copia el contenido de esta carpeta al repositorio.
3. Haz el primer commit y `push`.
4. En GitHub abre **Settings** del repositorio.
5. Activa **Template repository**.

Durante la clase, cada estudiante podrá usar:

**Use this template → Create a new repository**

y después clonar su propio repositorio con:

```bash
git clone URL_DE_SU_REPOSITORIO
```

La plantilla está adaptada del proyecto de ejemplo de ECCO Summer School 2025:
https://github.com/ECCO-Summer-School/ESS25_sample_project_repository

## Nota sobre JupyterLab y el ambiente

El archivo `environment.yml` incluye `ipykernel`.

Después de crear el ambiente por primera vez:

```bash
conda env create -f environment.yml
conda activate oceanografia
python -m ipykernel install --user --name oceanografia --display-name "Python (oceanografia)"
```

En JupyterLab, seleccionar:

**Kernel → Change Kernel → Python (oceanografia)**

Esto evita que Jupyter ejecute los notebooks con un Python distinto al ambiente del curso.
