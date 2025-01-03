# Peso Tracker

## Descripción General

Este proyecto es un ETL (Extract-Transform-Load) que extrae y procesa los datos históricos de la cotización del peso uruguayo (UYU) con respecto a diversas monedas como el dólar estadounidense (USD), el euro (EUR), el real brasileño (BRL) y el peso argentino (ARS). Los datos provienen del Instituto Nacional de Estadística de Uruguay (INE) y están disponibles de manera actualizada en la página oficial de estadísticas de series históricas.

La extracción de los datos se realiza de manera **diaria** mediante una automatización configurada con <a href="https://github.com/features/actions" target="_blank">**GitHub Actions**</a>, y los datos procesados se almacenan en una base de datos en <a href="https://supabase.com/" target="_blank">**Supabase**</a>, para su posterior uso y análisis.

## Dataset

El dataset utilizado en este proyecto proviene del Instituto Nacional de Estadística de Uruguay, que ofrece datos históricos de la cotización de diversas monedas. Los datos se encuentran en la siguiente URL:

https://www.gub.uy/instituto-nacional-estadistica/datos-y-estadisticas/estadisticas/series-historicas-cotizacion%20monedas

El proyecto extrae los datos desde esta fuente, los procesa y los carga en una base de datos.

## Estructura del Proyecto

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

📁 **peso_tracker**  
│  
├── 📄 **README.md**  
├── 📄 **pyproject.toml**  
├── 📄 **requirements.txt**  
├── 📄 **uv.lock**  
├── 📄 **.python-version**  
│  
├── 📁 **etl**  
│ ├── 📄 **main.py** # Script principal para ejecutar el proceso ETL  
│ ├── 📁 **data**  
│ │ ├── 📄 \***\*init**.py**  
│ │ ├── 📁 **procesed** # Carpeta con los datos procesados  
│ │ │ ├── 📄 \*\***init**.py**  
│ │ │ └── 📄 **procesed.py** # Funciones de procesamiento de datos  
│ │ └── 📁 **raw** # Carpeta con los datos crudos extraídos  
│ │ ├── 📄 \***\*init**.py**  
│ │ └── 📄 **raw.py** # Funciones para la extracción de datos  
│ └── 📁 **database**  
│ ├── 📄 \*\***init**.py**  
│ ├── 📄 **supabase_insertion.py** # Función para insertar datos en la base de datos  
│ └── 📄 **supabasedb.py** # Configuración y conexión a Supabase  
│  
└── 📁 **.github**  
 └── 📁 **workflows**  
 └── 📄 **update-database.yml** # Workflow para actualizar la base de datos

## Requisitos

Este proyecto requiere las siguientes dependencias:

- **Python 3.x**
- **Supabase** para la base de datos.
- **Bibliotecas de Python** listadas en el archivo `requirements.txt`.

Para instalar las dependencias, ejecuta:

```bash
pip install -r requirements.txt
```

## Configuración de la Base de Datos

Este proyecto utiliza Supabase como servicio de base de datos. Para configurarlo, asegúrate de:

- Crear una cuenta en Supabase.
- Crear un nuevo proyecto y configurar tu base de datos.
- Configurar las credenciales de acceso en el archivo supabasedb.py.

## Actualización de la Base de Datos

Este proyecto incluye un workflow de GitHub Actions (update-database.yml) que permite actualizar la base de datos automáticamente de acuerdo a un cronograma o cuando se realicen cambios en el repositorio.
