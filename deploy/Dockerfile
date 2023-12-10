# Seleccionar una imagen base para la etapa de producción
FROM python:3.11.4-slim-bullseye as prod

# Instalar la versión específica de Poetry
RUN pip install poetry==1.4.2

# Configurar Poetry
RUN poetry config virtualenvs.create false

# Copiar los archivos de requerimientos del proyecto
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Instalar los requerimientos
RUN poetry install --only main

# Copiar la aplicación real
COPY . /app/src/
RUN poetry install --only main

# Comando para ejecutar la aplicación en la etapa de producción
CMD ["/usr/local/bin/python", "-m", "pokemon_middleware"]

# Crear una etapa de desarrollo basada en la etapa de producción
FROM prod as dev

# Instalar dependencias adicionales para desarrollo
RUN poetry install
