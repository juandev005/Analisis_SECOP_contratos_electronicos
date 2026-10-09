import pandas as pd
import logging
from sodapy import Socrata
from config.config import Config
from config.logging_config import setup_logging
import requests
from exceptions import SecopNotRespondingError, SecopDataBaseNotRespondingError, SecopTokenNotValidError

log = logging.getLogger(__name__)

def get_data():
    client = Socrata(Config.SOCRATA_URL_BASE, Config.SOCRATA_APP_TOKEN, timeout=Config.SOCRATA_TIMEOUT)
    try:
        results = client.get(Config.SOCRATA_DATASET_ID, limit=1)
        log.info(f"Se descargaron {len(results)} registro/s de la base de datos.")
        return pd.DataFrame.from_records(results)

    except requests.exceptions.ConnectionError as e:
        msg = f"La url de la api no responde: {Config.SOCRATA_URL_BASE}"
        log.exception(msg)
        raise SecopNotRespondingError(msg) from e

    except requests.exceptions.ReadTimeout as e:
        msg = f"La api tardó más de {Config.SOCRATA_TIMEOUT}s en responder: {Config.SOCRATA_URL_BASE}"
        log.exception(msg)
        raise SecopNotRespondingError(msg) from e

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response is not None else None

        if status == 404:
            msg = f"La base de datos no existe o no responde. ID: {Config.SOCRATA_DATASET_ID}"
            log.exception(msg)
            raise SecopDataBaseNotRespondingError(msg) from e

        if status == 403:
            msg = "El token de la api no es válido."
            log.exception(msg)
            raise SecopTokenNotValidError(msg) from e

        log.exception(f"Error HTTP inesperado ({status}) consultando la api.")
        raise

    finally:
        client.close()