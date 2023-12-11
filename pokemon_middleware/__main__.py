import uvicorn

from pokemon_middleware.gunicorn_runner import GunicornApplication
from pokemon_middleware.settings import settings


def main() -> None:
    """Punto de entrada de la aplicación."""
    if settings.reload:
        uvicorn.run(
            "pokemon_middleware.web.application:get_app",
            workers=settings.workers_count,
            host=settings.host,
            port=settings.port,
            reload=settings.reload,
            log_level=settings.log_level.value.lower(),
            factory=True,
        )
    else:
        # Elegimos gunicorn solo si no se usa la opción de recarga,
        # porque la función de recarga no funciona con los workers de Uvicorn.
        GunicornApplication(
            "pokemon_middleware.web.application:get_app",
            host=settings.host,
            port=settings.port,
            workers=settings.workers_count,
            factory=True,
            accesslog="-",
            loglevel=settings.log_level.value.lower(),
            access_log_format='%r "-" %s "-" %Tf',  # noqa: WPS323
        ).run()


if __name__ == "__main__":
    main()
