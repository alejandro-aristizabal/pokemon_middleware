import requests  # type: ignore
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from requests.exceptions import JSONDecodeError  # type: ignore
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

router = APIRouter()


class PokemonMiddleware(BaseHTTPMiddleware):
    """Middleware para la pokedex."""

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Middleware para la pokedex.

        Args:
            request (Request): request
            call_next (RequestResponseEndpoint): endpoint

        Returns:
            Response: response
        """
        return await call_next(request)


@router.get("/pokedex_general/pokemon_name/{pokemon_name}")
def read_pokemon_name_general(pokemon_name: str) -> str:
    """Retorna la información del pokemon de acuerdo a la consulta.

    Args:
        pokemon_name (str): nombre del pokemon a consultar

    Returns:
        dict: información del pokemon
    """
    return f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"


@router.get("/pokedex_general/pokemon_id/{pokemon_id}")
def read_pokemon_id_general(pokemon_id: int) -> str:
    """Retorna la información del pokemon de acuerdo a la consulta.

    Args:
        pokemon_id (str): id del pokemon a consultar

    Returns:
        dict: información del pokemon
    """
    return f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"


@router.get("/pokedex_specific/pokemon_name/{pokemon_name}")
def read_pokemon_name_specific(pokemon_name: str) -> JSONResponse:
    """Retorna la información del pokemon, tales como.

        - Nombre
        - Habilidades
        - Número de la pokedex
        - Sprites
        - Tipo

    Args:
        pokemon_name (str): nombre del pokemon a consultar

    Returns:
        dict: información del pokemon
    """
    try:
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}",
            timeout=1,
        ).json()
        return JSONResponse(
            status_code=200,
            content={
                "name": response["name"],
                "abilities": response["abilities"],
                "id": response["id"],
                "sprites": response["sprites"],
                "types": response["types"],
            },
        )
    except JSONDecodeError:
        return JSONResponse(
            status_code=404,
            content={"message": "Pokemon not found"},
        )


@router.get("/pokedex_specific/pokemon_id/{pokemon_id}")
def read_pokemon_id_specific(pokemon_id: int) -> JSONResponse:
    """Retorna la información del pokemon, tales como.

        - Nombre
        - Habilidades
        - Número de la pokedex
        - Sprites
        - Tipo

    Args:
        pokemon_id (str): id del pokemon a consultar

    Returns:
        dict: información del pokemon
    """
    try:
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}",
            timeout=1,
        ).json()
        return JSONResponse(
            status_code=200,
            content={
                "name": response["name"],
                "abilities": response["abilities"],
                "id": response["id"],
                "sprites": response["sprites"],
                "types": response["types"],
            },
        )
    except JSONDecodeError:
        return JSONResponse(
            status_code=404,
            content={"message": "Pokemon not found"},
        )
