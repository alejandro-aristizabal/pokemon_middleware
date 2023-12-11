from typing import Any, AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from pokemon_middleware.web.application import get_app


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """Backend para el complemento de pytest anyio.

    Returns:
        str: nombre del backend
    """
    return "asyncio"


@pytest.fixture
def fastapi_app() -> FastAPI:
    """Accesorio para crear la aplicación FastAPI.

    Returns:
        FastAPI: aplicación FastAPI con dependencias simuladas.
    """
    application = get_app()
    return application  # noqa: WPS331


@pytest.fixture
async def client(
    fastapi_app: FastAPI,
    anyio_backend: Any,
) -> AsyncGenerator[AsyncClient, None]:
    """
    Accesorio que crea un cliente para solicitar al servidor.

    Args:
        fastapi_app (FastAPI): aplicación FastAPI con dependencias simuladas.
        anyio_backend (Any): nombre del backend.

    Yields:
        AsyncGenerator[AsyncClient, None]: cliente para la aplicación.
    """
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
