from fastapi import APIRouter

from pokemon_middleware.web.api.echo.schema import Message

router = APIRouter()


@router.post("/", response_model=Message)
async def send_echo_message(
    incoming_message: Message,
) -> Message:
    """
    Envía un eco de vuelta al usuario.

    Args:
        incoming_message: mensaje entrante.

    Returns:
        mensaje igual al entrante.
    """
    return incoming_message
