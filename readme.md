# Codigo de Ejemplo para el Taller de CI/CD

En el proyecto van a encontrar una pequeña api servida con 1 endpoint para dar status de nuestra aplicacion hacia afuera.
La aplicacion ademas cuenta con 1 test para validar que el status sea OK.

## Requerimientos

Lista de requerimientos para lograr el correcto funcionamiento de la aplicacion.

### Instalacion de Python

Instalar Python en nuestras maquinas, preferiblemente Python 3.9

**Windows**

En windows pueden desde el mismo store de microsoft buscar Python y realizar la instalacion sin problemas.

`Descargar desde https://www.python.org/downloads/`

**Linux**

Abren un terminal y ejecutan

`sudo apt install python3 python3-pip`

### Instalar entorno virtual

Se debe realizar la instalacion del entorno virtual para no tener problemas con diferentes versiones de librerias.

**Windows && Linux**

Ejecutar en el root del proyecto el siguiente comando que creara nuestra carpeta para controlar el entorno virtual

`python -m venv venv`

### Activar entorno virtual

**Windows**

Primero se debe habilitar el permiso para ejecutar comandos por Power Shell en Windows.
Abren un PowerShell y ejecutan el siguiente comando para dar los permisos:

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Luego pueden ejecutar en el root del proyecto

`./venv/Scripts/Activate.ps1`

**Linux**

Se debe ejecutar en el root del proyecto:

`source ./venv/bin/activate`

### Instalar librerias

## Como ejecutar?

Una vez levantado el entorno virtual se puede realizar la instalacion de librerias, en este caso solo es necesario tener instalado en nuestro virtual environment "flask".

`pip install -r requirements.txt`

## Ejecutar el proyecto

Para poder inicializar el proyecto se debe ejecutar lo siguiente:

`flask run`

Vamos a ver un output como el siguiente:

```bash
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Ejecutar las pruebas

Para poder ejecutar las pruebas simplemente podemos hacer:

`python -W ignore -m unittest discover --quiet -p 'test.py'`

o bien

`python test.py`