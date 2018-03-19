from pandasdmx import Request
from time import sleep

from helpers import utils


logger = utils.get_logger(__name__)


def fetch_total_passenger_counts():
    logger.info('Opening connection to Eurostat')
    estat = Request('ESTAT')
    dsdr = estat.datastructure(resource_id='DSD_avia_paoc', params={'references': 'all'})
    dsd = dsdr.datastructure['DSD_avia_paoc']

    logger.info('Writing Geo results')
    dsdr.write().codelist.loc['GEO'].to_csv(utils.get_project_path('data', 'raw', 'eurostat', 'geo.csv'))

    for geo in list(s for s in dsdr.write().codelist.loc['GEO'].index if s not in ['GEO', 'EU27', 'EU28']):
        logger.info('Fetching %s' % geo)
        res = estat.data(resource_id = 'avia_paoc', key={'FREQ': 'M', 'UNIT': 'PAS', 'TRA_MEAS': 'PAS_CRD', 'GEO': geo, 'TRA_COV': 'TOTAL', 'SCHEDULE': 'TOT',}, params = {'startPeriod': '1993'}, dsd=dsd)
        res.write().to_csv(utils.get_project_path('data', 'raw', 'eurostat', '%s.csv' % geo))
        sleep(2)


if __name__ == "__main__":
    fetch_total_passenger_counts()