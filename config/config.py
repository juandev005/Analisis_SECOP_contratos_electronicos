import os
from dotenv import load_dotenv
from exceptions import NotSetRequiredEnvironmentVariableError


load_dotenv()

def get_required_env(name: str, default: str = None) -> str:
    value = os.getenv(name)

    if not value:
        raise NotSetRequiredEnvironmentVariableError(f"La variable de entorno '{name}' es requerida")

    return value

class Config:
    POSTGRES_USER = get_required_env("POSTGRES_USER")
    POSTGRES_PASSWORD = get_required_env("POSTGRES_PASSWORD")
    POSTGRES_PORT = get_required_env("POSTGRES_PORT")
    POSTGRES_DB = get_required_env("POSTGRES_DB")
    POSTGRES_DATA = get_required_env("POSTGRES_DATA")