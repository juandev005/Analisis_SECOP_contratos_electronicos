import pandas as pd
from sodapy import Socrata
from config.config import Config
import requests
from exceptions import SecopNotRespondingError, SecopDataBaseNotRespondingError, SecopTokenNotValidError

def get_data():
    try:
        client = Socrata(Config.SOCRATA_URL_BASE, Config.SOCRATA_APP_TOKEN, timeout= Config.SOCRATA_TIMEOUT)
        results = client.get(Config.SOCRATA_DATASET_ID, limit=1)
        return pd.DataFrame.from_records(results)

    except requests.exceptions.ConnectionError as e:
        raise SecopNotRespondingError("La url de la api no responde: " + Config.SOCRATA_URL_BASE) from e

    except requests.exceptions.HTTPError as e:
            if "404" in str(e):
                raise SecopDataBaseNotRespondingError("La base de datos no responde. ID: " + Config.SOCRATA_DATASET_ID) from e

            if "403" in str(e):
                raise SecopTokenNotValidError("El token de la api no es valido. ") from e

    except requests.exceptions.ReadTimeout as e:
        raise SecopNotRespondingError("La url de la api no responde: " + Config.SOCRATA_URL_BASE) from e
