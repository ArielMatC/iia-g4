# Universidad de Buenos Aires
### Carrera de Especialización en Inteligencia Artificial
### Cohorte 22 - Año 2025

<br>

# Introducción a la Inteligencia Artificial - Grupo 4
Este repositorio contiene el material de resolución de los ejercicios y trabajos prácticos correspondientes al grupo 4.

## Integrantes
- [SIU a2208] Ariel Matias Cabello <arielmcabello@gmail.com>
- [SIU a2213] Ignacio Agustin Costarelli <agustin@costarellisa.com.ar>
- [SIU a2214] Alex Martín Curellich <alexcurellich@gmail.com>
- [SIU a2221] Cesar Octavio Mejia <cemejia555@gmail.com>
- [SIU a2227] Carlos Alberto Rivas Araque <carlos.rivas.a@gmail.com>

<br>

# Requerimientos
- Python >=3.11,<3.13 (requerido por vizdoom)
- uv / Poetry / Pip / Conda
- Numpy, Pandas, SciPy
- Matplotlib, Seaborn
- Scikit-Learn
- Pygame

# Instalación del entorno

## Usando Poetry (Recomendado)

1. **Instalar Poetry**:
   ```bash
   # En Windows (PowerShell)
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   
   # O usando pip
   pip install poetry
   ```

2. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/ArielMatC/iia-g4.git
   cd iia-g4
   ```

3. **Instalar las dependencias**:
   ```bash
   poetry install
   ```

4. **Activar el entorno virtual**:
   ```bash
   poetry shell
   ```

## Usando pip (Alternativo)

1. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   # En Windows
   .\venv\Scripts\activate
   # En Linux/Mac
   source venv/bin/activate
   ```

2. **Instalar las dependencias**:
   ```bash
   pip install -e .
   ```

## Ejecutar Jupyter Lab

Una vez instalado el entorno, se puede ejecutar Jupyter Lab para trabajar con los notebooks:

```bash
# Con Poetry
poetry run jupyter lab

# Con pip (entorno virtual activado)
jupyter lab
```

## Ejecutar la implementación del trabajo práctico 1

```bash
# Con Poetry
poetry run python trabajo_practico_1/main.py
```
