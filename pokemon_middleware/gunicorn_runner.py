from typing import Any

from gunicorn.app.base import BaseApplication
from gunicorn.util import import_app
from uvicorn.workers import UvicornWorker as BaseUvicornWorker

try:
    import uvloop  # noqa: WPS433 (Se encontró una importación anidada)
except ImportError:
    uvloop = None  # type: ignore  # noqa: WPS440 (las variables se superponen)


class UvicornWorker(BaseUvicornWorker):
    """
    Configuración para los workers de uvicorn.

    Esta clase hereda de UvicornWorker y define
    algunos parámetros a nivel de clase, porque es imposible
    pasar estos parámetros a través de gunicorn.
    """

    CONFIG_KWARGS = {  # noqa: WPS115 (constante en mayúsculas en una clase)
        "loop": "uvloop" if uvloop is not None else "asyncio",
        "http": "httptools",
        "lifespan": "on",
        "factory": True,
        "proxy_headers": False,
    }


class GunicornApplication(BaseApplication):
    """
    Aplicación gunicorn personalizada.

    Esta clase se utiliza para iniciar gunicorn
    con workers de uvicorn personalizados.
    """

    def __init__(  # noqa: WPS211 (Demasiados argumentos)
        self,
        app: str,
        host: str,
        port: int,
        workers: int,
        **kwargs: Any,
    ):
        self.options = {
            "bind": f"{host}:{port}",
            "workers": workers,
            "worker_class": "pokemon_middleware.gunicorn_runner.UvicornWorker",
            **kwargs,
        }
        self.app = app
        super().__init__()

    def load_config(self) -> None:
        """
        Carga la configuración para el servidor web.

        Esta función se utiliza para establecer parámetros en el proceso principal de gunicorn.
        Solo establece parámetros que
        gunicorn puede manejar. Si pasa un parámetro desconocido
        a esto, se bloqueará con un error.
        """
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self) -> str:
        """
        Carga la aplicación real.

        Gunicorn carga la aplicación basada en el retorno de esta
        función. Devolvemos la ruta de Python a
        la fábrica de la aplicación.

        :returns: ruta de Python a la fábrica de la aplicación.
        """
        return import_app(self.app)
