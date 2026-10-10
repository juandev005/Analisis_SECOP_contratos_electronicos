import logging
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from exceptions import (
    YamlFileError,
    YamlBadFormatError,
    YamlKeyError,
)

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).with_name("settings.yml")


@lru_cache(maxsize=1)
def _load_yaml() -> dict[str, Any]:

    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            params = yaml.safe_load(file)

    except FileNotFoundError as e:
        msg = f"No se encontró el archivo YAML: {CONFIG_PATH}"
        logger.exception(msg)
        raise YamlFileError(msg) from e

    except yaml.YAMLError as e:
        msg = f"El archivo YAML contiene un error de sintaxis: {CONFIG_PATH}"
        logger.exception(msg)
        raise YamlBadFormatError(msg) from e

    if not isinstance(params, dict):
        msg = f"El archivo YAML no contiene un diccionario: {CONFIG_PATH}"
        logger.error(msg)
        raise YamlBadFormatError(msg)

    logger.info("Configuración YAML cargada: %s", CONFIG_PATH)

    return params


def get_param(category_name: str, param_name: str) -> Any:

    params = _load_yaml()

    if category_name not in params:
        msg = (
            f"La categoría '{category_name}' "
            "no se encuentra en la configuración."
        )
        logger.error(msg)
        raise YamlKeyError(msg)

    category = params[category_name]

    if not isinstance(category, dict):
        msg = f"La categoría '{category_name}' no contiene un diccionario."
        logger.error(msg)
        raise YamlBadFormatError(msg)

    if param_name not in category:
        msg = (
            f"El parámetro '{param_name}' no se encuentra "
            f"en la categoría '{category_name}'."
        )
        logger.error(msg)
        raise YamlKeyError(msg)

    value = category[param_name]

    if value is None or (isinstance(value, str) and not value.strip()):
        msg = (
            f"El parámetro '{category_name}.{param_name}' "
            "tiene un valor vacío o nulo."
        )
        logger.error(msg)
        raise YamlKeyError(msg)

    return value