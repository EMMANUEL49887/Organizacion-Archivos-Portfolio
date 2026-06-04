# Sistema de Control de Acceso con Tarjetas RFID

## Descripción

Sistema desarrollado para gestionar y controlar el acceso a áreas restringidas mediante tarjetas RFID. Permite validar usuarios autorizados, registrar intentos de acceso y mantener un historial de auditoría utilizando archivos JSON y TXT como mecanismos de almacenamiento.

## Objetivo

Desarrollar un sistema que permita controlar el acceso de personal autorizado a instalaciones o almacenes de forma segura y eficiente. El sistema busca garantizar la protección de áreas restringidas mediante la validación de tarjetas RFID y el registro detallado de todos los accesos realizados.

## Tecnologías Utilizadas

* Python (Procesamiento de datos y validación de accesos)
* JSON (Almacenamiento de usuarios autorizados)
* Archivos TXT (Registro de auditorías y eventos)
* RFID (Identificación mediante tarjetas)
* Hardware de lectura RFID (Control de acceso físico)

## Estructura del Proyecto

* usuarios.json: Archivo que contiene la información de los usuarios autorizados.
* auditoria.txt: Archivo donde se registran todos los intentos de acceso.
* sistema.py: Programa principal encargado de validar tarjetas y gestionar accesos.
* lector RFID: Dispositivo utilizado para capturar el identificador de las tarjetas.
* Documentación técnica: Explicación detallada del funcionamiento del sistema.

## Formatos de Archivo Utilizados

### JSON: Configuración de Usuarios

El sistema emplea archivos JSON (usuarios.json) para definir a los usuarios autorizados y sus niveles de seguridad. Se eligió este formato por las siguientes ventajas:

* **Estructura clara y legible:** El formato JSON permite organizar los datos de cada usuario de forma ordenada y jerárquica, facilitando la identificación de campos como id_tarjeta, nombre_empleado, departamento y nivel_seguridad.
* **Facilidad de integración:** Al ser un estándar ampliamente utilizado en el desarrollo de software, Python puede interpretar fácilmente la información y convertirla en estructuras de datos nativas para su procesamiento.
* **Validación de datos:** La estructura permite implementar verificaciones sencillas para asegurar que la información almacenada sea correcta y consistente, evitando errores durante la carga de datos.

### TXT: Registro de Auditoría

El sistema utiliza archivos de texto plano (auditoria.txt) para almacenar todos los intentos de acceso realizados. Las principales ventajas de esta elección son:

* **Independencia y sencillez:** Los archivos TXT no requieren bases de datos ni servidores adicionales, permitiendo que el sistema funcione de manera local y confiable.
* **Registro continuo y eficiente:** Utilizando el modo de escritura de adición (append), cada nuevo acceso se agrega al final del archivo sin afectar los registros anteriores.
* **Auditoría y trazabilidad:** Cada registro almacena la fecha, hora y resultado de la validación, permitiendo conocer quién intentó acceder y cuándo ocurrió.
* **Bajo costo y alta velocidad:** La implementación es simple, rápida y requiere pocos recursos, facilitando el mantenimiento del sistema.

## Funcionamiento del Sistema

1. Registrar los usuarios autorizados en el archivo usuarios.json.
2. Iniciar el programa principal del sistema.
3. Acercar una tarjeta RFID al lector.
4. El sistema verifica si la tarjeta se encuentra registrada.
5. Si el usuario está autorizado, se concede el acceso.
6. Si el usuario no está autorizado, el acceso es rechazado.
7. Todos los eventos son almacenados automáticamente en auditoria.txt para su posterior revisión.

## Capturas del Sistema Funcionando

Se incluyen evidencias del funcionamiento del sistema, mostrando el proceso de lectura de tarjetas, validación de usuarios y registro de auditorías.

## Diagrama de Flujo

El diagrama de flujo representa la secuencia lógica del sistema, desde la lectura de la tarjeta RFID hasta la autorización o rechazo del acceso y el almacenamiento del evento en el archivo de auditoría.

## Maqueta de Lector de Tarjetas Físico

Se desarrolló una maqueta representativa del sistema de control de acceso, integrando el lector RFID y simulando el funcionamiento de un punto de acceso seguro para personal autorizado.

## Documentación

La documentación técnica incluye la descripción de cada módulo del sistema, la estructura de los archivos utilizados, el proceso de validación de usuarios y la gestión de registros de auditoría.
