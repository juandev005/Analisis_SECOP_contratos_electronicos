import logging
import time

import requests
from sodapy import Socrata

from config.config import Config
from config.yaml_config import get_param

from exceptions import (
    SecopError,
    SecopNotRespondingError,
    SecopDataBaseNotRespondingError,
    SecopTokenNotValidError,
    SecopQueryNotValidError,
)

logger = logging.getLogger(__name__)

HTTP_REINTENTABLES = {429, 500, 502, 503, 504}

class SecopApiClient:

    def __init__(self):
        self._client = Socrata(
            get_param("fuente", "base_url"),
            Config.SOCRATA_APP_TOKEN,
            timeout=get_param("fuente", "timeout_s"),
        )

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def close(self):
        self._client.close()

    def _traducir_http(self, status):
        dataset_id = get_param("fuente", "dataset_id")

        if status == 404:
            msg = f"El dataset no existe: {dataset_id}"
            logger.error(msg)
            return SecopDataBaseNotRespondingError(msg)

        if status in (401, 403):
            msg = "El token de la API no es valido."
            logger.error(msg)
            return SecopTokenNotValidError(msg)

        if status == 400:
            msg = "Consulta inválida (400): revisa $select / $where / $group."
            logger.error(msg)
            return SecopQueryNotValidError(msg)

        msg = f"Error HTTP inesperado ({status}) consultando el dataset: {dataset_id}"
        logger.error(msg)
        return SecopError(msg)

    def _get(self, **params):
        ultimo_error = None

        max_intentos = get_param("fuente", "max_intentos")
        espera_s_base = get_param("fuente", "espera_s_base")
        dataset_id = get_param("fuente", "dataset_id")
        base_url = get_param("fuente", "base_url")

        for intento in range(1, max_intentos + 1):
            espera = espera_s_base * 2 ** (intento - 1)

            try:
                logger.debug(
                    "GET %s %s (intento %d)",
                    dataset_id,
                    params,
                    intento,
                )

                
                return self._client.get(dataset_id, **params)

            except (requests.exceptions.ConnectionError,requests.exceptions.Timeout,) as e:
                ultimo_error = e

            except requests.exceptions.HTTPError as e:
                status = (
                    e.response.status_code
                    if e.response is not None
                    else None
                )

                if status not in HTTP_REINTENTABLES:
                    raise self._traducir_http(status) from e

                ultimo_error = e

            if intento < max_intentos:
                logger.warning(
                    "Fallo al consultar la API. Reintento en %ss.",
                    espera,
                )
                time.sleep(espera)

        msg = f"La API no respondió tras {max_intentos} intentos. ('{base_url}')"

        logger.error(msg)
        raise SecopNotRespondingError(msg) from ultimo_error

    def contar(self, where):
        filas = self._get(
            select="count(*) AS total",
            where=where,
        )
        return int(filas[0]["total"])

    def contar_por_anio(self, where, campo_fecha="fecha_de_firma"):
        anio = f"date_extract_y({campo_fecha})"

        filas = self._get(
            select=f"{anio} AS anio, count(*) AS total",
            where=where,
            group=anio,
            order=anio,
        )

        logger.debug("filas: %s", len(filas))
        logger.info("La consulta fue exitosa.")

        return {
            int(f["anio"]): int(f["total"])
            for f in filas
            if "anio" in f
        }
