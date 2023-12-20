# Análisis exploratorio de datos en Python

El objetivo principal de este proyecto es analizar, a través de métodos estadísticos, los salarios de los programadores en Europa, explorando los diversos factores que influyen en ellos. La meta es obtener información relevante y actualizada que permita a futuros programadores tomar decisiones informadas sobre su carrera. Este proyecto fue desarrollado para la clase de Inferencia estadística, utilizando Python con las bibliotecas Pandas, Matplotlib y Seaborn.

## Tabla de contenidos

- [Estructura del proyecto](#estructura-del-proyecto)
- [Materiales y métodos](#materiales-y-métodos)
  - [Base de datos](#base-de-datos)
  - [Lenguaje y librerías](#lenguaje-y-librerías)
  - [Resumen de los datos](#resumen-de-los-datos)
- [Análisis](#análisis)
- [Conclusiones](#conclusiones)

## Estructura del proyecto

Dentro del proyecto encontrarás los siguientes directorios y archivos:

´´´
/proyecto_analisis_datos
├── datos/
│   ├── original/
│   │   └── IT Salary Survey EU.csv
│   └── procesados/
├── notebooks/
├── reportes/
│   └── figuras/
└── README.md
´´´

Dentro del directorio `datos/`, encontrarás la base de datos original utilizada para este análisis en `datos/original/`. Asimismo, podrás explorar los datos después de pasar por el proceso de limpieza en el directorio `datos/procesados/`.

En el directorio `notebooks/`, encontrarás archivos `.ipynb` que contienen el código necesario tanto para el proceso de limpieza como para el análisis visual de los datos.

Finalmente, en `reportes/` encontrarás los gráficos generados en la carpeta `notebooks/figuras/`. Además, `reportes/` almacena archivos `.md` con interpretaciones y conclusiones sobre los datos, que utilizan las figuras mencionadas anteriormente.


## Materiales y métodos

### Base de datos

En este proyecto se hace uso de  [IT Salary Survey for EU region 2020](https://www.kaggle.com/datasets/parulpandey/2020-it-salary-survey-for-eu-region), una base de datos resultado de una encuesta anónima realizada a profesionales de tecnología de la información en Europa. La encuesta abarca datos demográficos, detalles laborales y características de las empresas. Iniciada en 2015 por Viktor Shcherban, la encuesta se ha repetido anualmente, ganando popularidad. La edición 2020, influenciada por la pandemia, destaca cambios en el trabajo remoto y la creciente demanda de profesionales de IT.

### Lenguaje y librerías

La manipulación y análisis de la base de datos se llevaron a cabo en Python debido a su amplia adopción, familiaridad y facilidad de uso. Para gestionar y explorar eficientemente los datos, se emplearon las siguientes librerías:

- **Pandas:** Utilizada para la manipulación y limpieza de datos.
- **Matplotlib:** Utilizada para la creación de gráficos y diagramas.
- **Seaborn:** Complementaria a Matplotlib, utilizada para generar gráficos atractivos.

### Resumen de los datos 

## Análisis

## Concluciones