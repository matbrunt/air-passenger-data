import requests
import json
from time import sleep

from helpers import utils


logger = utils.get_logger(__name__)

base_url = 'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/avia_paoc?precision=1&unit=PAS&schedule=TOT&shortLabel=1&tra_cov=TOTAL&tra_meas=PAS_CRD&freq=M'

countries = {
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CH": "Switzerland",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "EL": "Greece",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IS": "Iceland",
    "IT": "Italy",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "ME": "Montenegro",
    "MK": "Macedonia",
    "MT": "Malta",
    "NL": "Netherlands",
    "NO": "Norway",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
    "UK": "United Kingdom"
}

def fetch_total_passenger_counts():
    url = base_url + '&geo=UK'
    logger.info('Fetching UK')
    r = requests.get(url)
    if r.status_code == 200:
        filename = utils.get_raw_file('UK.json')
        with open(filename, 'w') as f:
            logger.info('writing %s file ' % filename)
            f.write(r.text)
        # json.dump(data, fp, sort_keys=True, indent=2)


if __name__ == "__main__":
    fetch_total_passenger_counts()