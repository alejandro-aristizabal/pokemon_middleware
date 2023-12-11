import logging
import sys
from typing import Union

from loguru import logger

from pokemon_middleware.settings import settings


class InterceptHandler(logging.Handler):
    """
    Controlador predeterminado de los ejemplos en la documentación de loguru.

    Este controlador intercepta todas las solicitudes de registro y
    las pasa a loguru.

    Para obtener más información, consulte:
    https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        """
        Propaga los registros a loguru.

        Args:
            record (logging.LogRecord): registro a propagar.
        """
        try:
            level: Union[str, int] = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Encontrar el origen del mensaje registrado
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back  # type: ignore
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def configure_logging() -> None:  # pragma: no cover
    """
    Configura el registro.

    Configura el sistema de registro para utilizar loguru
    y ajusta los niveles de registro según la configuración.
    """
    intercept_handler = InterceptHandler()

    logging.basicConfig(handlers=[intercept_handler], level=logging.NOTSET)

    for logger_name in logging.root.manager.loggerDict:
        if logger_name.startswith("uvicorn."):
            logging.getLogger(logger_name).handlers = []

    # cambiar el controlador para el registro uvicorn predeterminado
    logging.getLogger("uvicorn").handlers = [intercept_handler]
    logging.getLogger("uvicorn.access").handlers = [intercept_handler]

    # establecer la salida, el nivel y el formato de los registros
    logger.remove()
    logger.add(
        sys.stdout,
        level=settings.log_level.value,
    )
