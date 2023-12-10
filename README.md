# pokemon_middleware

## Poetry

Este proyecto utiliza poetry. Es una herramienta moderna de gestión de dependencias.

Para ejecutar el proyecto, utiliza este conjunto de comandos:

```bash
poetry install
poetry run python -m pokemon_middleware
```

Esto iniciará el servidor en el host configurado.

Puedes encontrar la documentación de Swagger en /api/docs.

Puedes obtener más información sobre poetry aquí: https://python-poetry.org/

## Docker

Puedes iniciar el proyecto con Docker utilizando este comando:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

Si deseas desarrollar en Docker con recarga automática, agrega -f deploy/docker-compose.dev.yml a tu comando de Docker. Así:


```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

Este comando expone la aplicación web en el puerto 8000, monta el directorio actual y habilita la recarga automática.

Pero debes reconstruir la imagen cada vez que modifiques poetry.lock o pyproject.toml con este comando:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "pokemon_middleware"
pokemon_middleware
├── conftest.py  # Accesorios para todas las pruebas.
├── __main__.py  # Script de inicio. Inicia uvicorn.
├── services  # Paquete para diferentes servicios externos como rabbit o redis, etc. En caso de ser necesarios.
├── settings.py  # Configuración principal del proyecto.
├── static  # Contenido estático.
├── tests  # Pruebas para el proyecto.
└── web  # Paquete que contiene el servidor web. Controladores, configuración de inicio.
    ├── api  # Paquete con todos los controladores.
    │   └── router.py  # Enrutador principal.
    ├── application.py  # Configuración de la aplicación FastAPI.
    └── lifetime.py  # Contiene acciones a realizar en el inicio y cierre.
```

## Configuration

Esta aplicación se puede configurar con variables de entorno.

Puedes crear un archivo .env en el directorio raíz y colocar todas las
variables de entorno aquí.

Todas las variables de entorno deben comenzar con el prefijo "POKEMON_MIDDLEWARE_".

Por ejemplo, si ves en tu "pokemon_middleware/settings.py" una variable llamada
random_parameter, debes proporcionar la variable "POKEMON_MIDDLEWARE_RANDOM_PARAMETER"
para configurar el valor. Este comportamiento se puede cambiar sobrescribiendo la propiedad env_prefix
en pokemon_middleware.settings.Settings.Config.

Un ejemplo de archivo .env:

```bash
POKEMON_MIDDLEWARE_RELOAD="True"
POKEMON_MIDDLEWARE_PORT="8000"
POKEMON_MIDDLEWARE_ENVIRONMENT="dev"
```

Puedes obtener más información sobre la clase BaseSettings aquí: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

Para instalar pre-commit simplemente ejecuta dentro de la terminal:

```bash
pre-commit install
```

pre-commit es muy útil para verificar tu código antes de publicarlo.
Está configurado utilizando el archivo .pre-commit-config.yaml.

Por defecto, ejecuta:

black (formatea tu código);
mypy (valida tipos);
isort (ordena las importaciones en todos los archivos);
flake8 (detecta posibles errores);
Puedes obtener más información sobre pre-commit aquí: https://pre-commit.com/


## Running tests

1. Si deseas ejecutarlo en Docker, simplemente ejecuta:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

2. Para ejecutar pruebas en tu máquina local con pytest.

```bash
pytest -vv .
```
