from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> None:
    """
    Verifica la salud del proyecto.

    Retorna 200 si el proyecto está saludable.
    """
