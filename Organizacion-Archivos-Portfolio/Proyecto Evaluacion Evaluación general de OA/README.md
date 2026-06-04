# Sistema de Comparación de Rendimiento entre CSV y JSON para Registros Médicos

## Descripción

Sistema desarrollado en Python para generar, almacenar y procesar millones de registros médicos simulados utilizando los formatos CSV y JSON. El programa permite comparar el rendimiento de ambos formatos mediante pruebas de lectura, escritura, almacenamiento y análisis estadístico. Además, incluye herramientas para realizar búsquedas de pacientes, generar estadísticas y crear gráficas que facilitan la interpretación de los datos.

## Objetivo

Desarrollar una aplicación que permita evaluar el rendimiento de los formatos CSV y JSON en el manejo de grandes volúmenes de información médica, analizando aspectos como velocidad de procesamiento, espacio de almacenamiento y facilidad para el análisis de datos.

## Tecnologías Utilizadas

* Python 3.x
* Pandas
* Matplotlib (Pyplot)
* CSV
* JSON
* Random
* Time
* OS
* Datetime
* Tabulate

## Estructura del Proyecto

* **config.py**: Configuración general del sistema y cantidad de registros a generar.
* **generador.py**: Generación automática de registros médicos simulados.
* **funciones.py**: Funciones de validación, búsqueda y procesamiento.
* **main.py**: Menú principal e interacción con el usuario.
* **datos.csv**: Base de datos médica en formato CSV.
* **datos.json**: Base de datos médica en formato JSON.
* **comparativa_resultados.txt**: Resultados de las pruebas de rendimiento.
* **graficas/**: Carpeta donde se almacenan las gráficas generadas.
* **docs/**: Documentación técnica del proyecto.

## Formatos de Archivo Utilizados

* **CSV**: Almacenamiento de registros médicos en formato tabular.
* **JSON**: Almacenamiento de registros médicos con estructura jerárquica.
* **TXT**: Reportes y resultados de las pruebas experimentales.
* **PY**: Código fuente del sistema.

## Ejecución

### 1. Configurar la cantidad de registros

Modificar la variable:

```python
NUM_REGISTROS
```

dentro del archivo `config.py`.

### 2. Ejecutar el programa

```bash
python main.py
```

### 3. Funcionalidades disponibles

* Generación masiva de registros médicos.
* Escritura automática en CSV y JSON.
* Comparación de tiempos de lectura y escritura.
* Consulta de pacientes por ID o nombre.
* Estadísticas médicas.
* Generación de gráficas.
* Comparación de tamaños de archivos.

## Documentación

La documentación completa incluye la metodología experimental, descripción de los algoritmos utilizados, análisis de resultados, comparación entre formatos CSV y JSON, generación de gráficas y conclusiones del proyecto. Esta información se encuentra disponible en la carpeta `docs`.

## Resultados Esperados

* Determinar cuál formato ofrece mejor rendimiento para grandes volúmenes de datos.
* Comparar el espacio de almacenamiento utilizado por cada formato.
* Analizar la velocidad de lectura y escritura de archivos.
* Evaluar la facilidad de integración con herramientas de análisis como Pandas.
* Identificar las ventajas y desventajas de CSV y JSON en entornos hospitalarios.

## Conclusión General

Los resultados demostraron que CSV ofrece un mejor rendimiento en velocidad y almacenamiento para el análisis masivo de datos, mientras que JSON proporciona una mayor flexibilidad para representar información compleja y facilitar la integración entre sistemas modernos. La combinación de ambos formatos representa una solución eficiente para sistemas hospitalarios de gran escala.
