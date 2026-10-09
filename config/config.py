import os
from pathlib import Path
from typing import Any
import yaml
from dotenv import load_dotenv
from exceptions import NotSetRequiredEnvironmentVariableError, YamlFileError, YamlBadFormatError, YamlKeyError


load_dotenv()


config_path = Path("config/settings.yml")

try:
    with config_path.open("r", encoding="utf-8") as file:
        params = yaml.safe_load(file)

        if not isinstance(params, dict):
            raise YamlBadFormatError(
                f"El archivo YAML contiene un error de sintaxis: {config_path}"
            )

except FileNotFoundError as e:
    raise YamlFileError(
        f"No se encontró el archivo de configuración: {config_path}"
    ) from e

except yaml.YAMLError as e:
    raise YamlBadFormatError(
        f"El archivo YAML contiene un error de sintaxis: {config_path}"
    ) from e


def get_param(category_name: str, param_name: str) -> Any:
    category = params.get(category_name)


    if category_name not in params:
        raise YamlKeyError(
            f"Categoría '{category_name}' no encontrada en la configuración."
        )

    if param_name not in category:
        raise YamlKeyError(
            f"Parámetro '{param_name}' no encontrado en la categoría '{category_name}'."
        )
    value = category[param_name]

    if value is None or value == "":
        raise YamlKeyError(
            f"El parámetro '{category_name}.{param_name}' tiene un valor vacío o nulo."
        )

    return value

order_by = get_param("extraccion","order_by")

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
    
    SOCRATA_APP_TOKEN = get_required_env("SOCRATA_APP_TOKEN")

    SOCRATA_DATASET_ID = get_param("fuente","dataset_id")
    SOCRATA_URL_BASE = get_param("fuente","base_url")
    SOCRATA_TIMEOUT = get_param("fuente","timeout_s")