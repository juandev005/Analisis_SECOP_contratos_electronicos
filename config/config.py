import os
import logging
from pathlib import Path
from typing import Any
import yaml
from dotenv import load_dotenv
from exceptions import NotSetRequiredEnvironmentVariableError, YamlFileError, YamlBadFormatError, YamlKeyError

logger = logging.getLogger(__name__)

load_dotenv()
config_path = Path("config/settings.yml")

try:
    with config_path.open("r", encoding="utf-8") as file:
        params = yaml.safe_load(file)

    if not isinstance(params, dict):
        msg = f"El archivo YAML no contiene un diccionario: {config_path}"
        logger.error(msg)
        raise YamlBadFormatError(msg)

    logger.info(f"Configuración cargada: {config_path}")

except FileNotFoundError as e:
    msg = f"No se encontró el archivo de configuración: {config_path}"
    logger.exception(msg)
    raise YamlFileError(msg) from e

except yaml.YAMLError as e:
    msg = f"El archivo YAML contiene un error de sintaxis: {config_path}"
    logger.exception(msg)
    raise YamlBadFormatError(msg) from e


def get_param(category_name: str, param_name: str) -> Any:
    if category_name not in params:
        msg = f"La categoría '{category_name}' no se encuentra en la configuración."
        logger.error(msg)
        raise YamlKeyError(msg)

    category = params[category_name]

    if not isinstance(category, dict) or param_name not in category:
        msg = f"El parámetro '{param_name}' no se encuentra en la categoría '{category_name}'."
        logger.error(msg)
        raise YamlKeyError(msg)

    value = category[param_name]

    if value is None or value == "":
        msg = f"El parámetro '{category_name}.{param_name}' tiene un valor vacío o nulo."
        logger.error(msg)
        raise YamlKeyError(msg)

    return value


order_by = get_param("extraccion", "order_by")


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

    SOCRATA_DATASET_ID = get_param("fuente", "dataset_id")
    SOCRATA_URL_BASE = get_param("fuente", "base_url")
    SOCRATA_TIMEOUT = get_param("fuente", "timeout_s")