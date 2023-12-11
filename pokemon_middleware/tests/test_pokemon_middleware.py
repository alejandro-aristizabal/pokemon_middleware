import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status


@pytest.mark.anyio
async def test_health(
    client: AsyncClient,
    fastapi_app: FastAPI,
) -> None:
    """
    Evalúa que el endpoint de health_check funcione.

    Args:
        client (AsyncClient): cliente para la aplicación.
        fastapi_app (FastAPI): actual aplicación FastAPI.
    """
    url = fastapi_app.url_path_for("health_check")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_read_pokemon_name_general(
    client: AsyncClient,
    fastapi_app: FastAPI,
) -> None:
    """
    Evalúa que el endpoint de read_pokemon_name_general funcione.

    Args:
        client (AsyncClient): cliente para la aplicación.
        fastapi_app (FastAPI): actual aplicación FastAPI.
    """
    url = fastapi_app.url_path_for("read_pokemon_name_general", pokemon_name="pikachu")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_read_pokemon_id_general(
    client: AsyncClient,
    fastapi_app: FastAPI,
) -> None:
    """
    Evalúa que el endpoint de read_pokemon_id_general funcione.

    Args:
        client (AsyncClient): cliente para la aplicación.
        fastapi_app (FastAPI): actual aplicación FastAPI.
    """
    url = fastapi_app.url_path_for("read_pokemon_id_general", pokemon_id=25)
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_read_pokemon_name_specific(
    client: AsyncClient,
    fastapi_app: FastAPI,
) -> None:
    """
    Evalúa que el endpoint de read_pokemon_name_specific funcione.

    Args:
        client (AsyncClient): cliente para la aplicación.
        fastapi_app (FastAPI): actual aplicación FastAPI.
    """
    url = fastapi_app.url_path_for("read_pokemon_name_specific", pokemon_name="pikachu")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_read_pokemon_id_specific(
    client: AsyncClient,
    fastapi_app: FastAPI,
) -> None:
    """
    Evalúa que el endpoint de read_pokemon_id_specific funcione.

    Args:
        client (AsyncClient): cliente para la aplicación.
        fastapi_app (FastAPI): actual aplicación FastAPI.
    """
    url = fastapi_app.url_path_for("read_pokemon_id_specific", pokemon_id=25)
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
