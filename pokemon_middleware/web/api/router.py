from fastapi.routing import APIRouter

from pokemon_middleware.web.api import echo, monitoring, pokedex

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(pokedex.router, prefix="", tags=["pokedex"])
