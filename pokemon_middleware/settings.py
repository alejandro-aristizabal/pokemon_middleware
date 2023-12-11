import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings, SettingsConfigDict

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    Estos parámetros pueden ser configurados
    con variables de entorno.
    """

    host: str = "127.0.0.1"
    port: int = 8000
    # cantidad de workers para el servidor uvicorn
    workers_count: int = 1
    # Habilita el hot reload
    reload: bool = False

    # Ambiente de ejecución
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="POKEMON_MIDDLEWARE_",
        env_file_encoding="utf-8",
    )


settings = Settings()
