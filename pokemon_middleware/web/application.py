from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from pokemon_middleware.logging import configure_logging
from pokemon_middleware.web.api.pokedex.views import PokemonMiddleware
from pokemon_middleware.web.api.router import api_router
from pokemon_middleware.web.lifetime import (
    register_shutdown_event,
    register_startup_event,
)


def get_app() -> FastAPI:
    """
    Obtener la aplicación FastAPI.

    Este es el constructor principal de la aplicación.

    Returns:
        FastAPI: aplicación FastAPI.
    """
    configure_logging()
    app = FastAPI(
        title="pokemon_middleware",
        version=metadata.version("pokemon_middleware"),
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.add_middleware(PokemonMiddleware)

    # Agrega eventos de inicio y apagado.
    register_startup_event(app)
    register_shutdown_event(app)

    # Enrutador principal para la API.
    app.include_router(router=api_router, prefix="/api")

    return app
