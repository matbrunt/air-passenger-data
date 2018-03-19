import pandas as pd
import numpy as np
import os
from glob import glob

from helpers import utils

logger = utils.get_logger(__name__)


def read_datafile(file_name):
    country_code = os.path.basename(file_name).replace('.csv', '')
    logger.info('Parsing %s' % country_code)
    return (
        pd.read_csv(file_name, skiprows=7, index_col=0, parse_dates=[0], header=None, names=['pax'])
        .assign(pax = lambda x: pd.to_numeric(x.pax, downcast='integer', errors='coerce'))
        .rename(columns={'pax': country_code})
    )


def combine_datafiles():
    combined = pd.DataFrame()
    for csv_file in [d for d in glob(utils.get_project_path('data', 'raw', 'eurostat', '*.csv'))]:
        if os.path.basename(csv_file) == 'geo.csv':
            continue
        df = read_datafile(csv_file)
        combined = pd.concat([combined, df], axis=1)
    
    combined.to_csv(utils.get_interim_file('eurostat.csv'))
    return combined


def melt_combined(df):
    melted = (
        pd.melt(df.reset_index(), id_vars=['index'], var_name='country', value_name='pax')
        .rename(columns={'index': 'date'})
    )

    melted.to_csv(utils.get_interim_file('eurostat_melt.csv'), index=False)
    return melted


if __name__ == "__main__":
    combine_datafiles()