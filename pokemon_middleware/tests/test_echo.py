import uuid

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status


@pytest.mark.anyio
async def test_echo(fastapi_app: FastAPI, client: AsyncClient) -> None:
    """
    Tests that echo route funciona.

    Args:
        fastapi_app (FastAPI): actual aplicación FastAPI.
        client (AsyncClient): cliente para la aplicación.
    """
    url = fastapi_app.url_path_for("send_echo_message")
    message = uuid.uuid4().hex
    response = await client.post(
        url,
        json={
            "message": message,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == message
