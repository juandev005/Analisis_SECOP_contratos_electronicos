import os
import logging
from dotenv import load_dotenv
from exceptions import NotSetRequiredEnvironmentVariableError
logger = logging.getLogger(__name__)

load_dotenv()

def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        msg = f"La variable de entorno '{name}' es requerida."
        logger.error(msg)
        raise NotSetRequiredEnvironmentVariableError(msg)

    return value


class Config:

    POSTGRES_USER = get_required_env("POSTGRES_USER")
    POSTGRES_PASSWORD = get_required_env("POSTGRES_PASSWORD")
    POSTGRES_PORT = get_required_env("POSTGRES_PORT")
    POSTGRES_DB = get_required_env("POSTGRES_DB")
    POSTGRES_DATA = get_required_env("POSTGRES_DATA")

    SOCRATA_APP_TOKEN = get_required_env("SOCRATA_APP_TOKEN")