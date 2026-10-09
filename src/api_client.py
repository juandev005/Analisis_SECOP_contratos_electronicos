import pandas as pd
from sodapy import Socrata
from config.config import Config

def get_data():
    client = Socrata(Config.SOCRATA_URL_BASE, Config.SOCRATA_APP_TOKEN, timeout= Config.SOCRATA_TIMEOUT)
    results = client.get(Config.SOCRATA_DATASET_ID, limit=1)

    return pd.DataFrame.from_records(results)