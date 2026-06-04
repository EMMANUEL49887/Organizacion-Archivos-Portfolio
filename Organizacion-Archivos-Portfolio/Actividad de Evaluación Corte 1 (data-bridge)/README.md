## Actividad de Evaluación Corte 1 (data-bridge)

## Descripción

Sistema desarrollado para gestionar y consultar órdenes de un restaurante utilizando archivos planos (.txt). Permite registrar, almacenar, buscar y visualizar información relacionada con los pedidos realizados por los clientes. Las búsquedas pueden realizarse mediante diferentes criterios como número de orden, platillo, mesero o mesa.

## Objetivo

Desarrollar un sistema que facilite la administración y consulta de órdenes de un restaurante de forma rápida y organizada, utilizando archivos planos como mecanismo de almacenamiento. El sistema busca reducir el tiempo necesario para localizar información y mejorar el control de los pedidos registrados.

## Tecnologías Utilizadas

Python (Generación de datos simulados)
PHP (Procesamiento y consulta de información)
HTML (Interfaz de usuario)
CSS (Diseño y presentación visual)
Archivos TXT (Almacenamiento de datos)

## Estructura del Proyecto

generar.py: Genera las órdenes simuladas y crea el archivo maestro.txt.
index.php: Página principal del sistema y formulario de búsqueda.
procesar.php: Procesa los criterios de búsqueda ingresados por el usuario.
mostrar_todas.php: Muestra todas las órdenes almacenadas.
resultados.php: Presenta los resultados de las búsquedas realizadas.
descargar_txt.php: Permite descargar los resultados filtrados.
estilos.css: Contiene los estilos visuales de la aplicación.
maestro.txt: Archivo principal con todas las órdenes generadas.
filtrado.txt: Archivo temporal con los resultados de las búsquedas.
menu.jpeg: Imagen utilizada en la interfaz del sistema.

## Formatos de Archivo Utilizados

TXT: Almacenamiento de órdenes y resultados de búsqueda.
PHP: Desarrollo de la lógica del sistema web.
PY: Generación automática de datos.
CSS: Diseño visual de la interfaz.
JPEG: Recursos gráficos utilizados en la aplicación.

## Ejecución
1. Generar los datos de prueba

Ejecutar el archivo:

python generar.py

Esto creará el archivo maestro.txt con 300 órdenes simuladas.

2. Iniciar el servidor web

Colocar los archivos del proyecto en un servidor local compatible con PHP (por ejemplo, XAMPP o WAMP).

3. Acceder al sistema

Abrir el navegador y acceder a:

http://localhost/nombre_del_proyecto/

4. Realizar consultas
Ingresar uno o más criterios de búsqueda.
Consultar órdenes específicas.
Mostrar todas las órdenes registradas.
Descargar los resultados obtenidos en formato TXT.
Documentación

La documentación técnica completa incluye la descripción detallada de cada módulo del sistema, el funcionamiento de los archivos utilizados y la explicación del procesamiento de datos. Esta documentación puede encontrarse en la carpeta docs o en el reporte técnico del proyecto.
