Sample code derived from [PandaSDMX ReadTheDocs](https://pandasdmx.readthedocs.io/en/latest/usage.html).

First you need to install the package with `pip install pandasdmx`

```python
from pandasdmx import Request
estat = Request('ESTAT')
dsdr = estat.datastructure(resource_id='DSD_avia_paoc', params={'references': 'all'})
dsd = dsdr.datastructure['DSD_avia_paoc']
dsd.dimensions.aslist()
# [Dimension | FREQ, Dimension | UNIT, Dimension | TRA_MEAS, Dimension | GEO, Dimension | TRA_COV, Dimension | SCHEDULE, TimeDimension | TIME_PERIOD]

dsdr.write().codelist.loc['GEO'].to_csv('geo.csv')

list(s for s in dsdr.write().codelist.loc['GEO'].index if s not in ['GEO', 'EU27', 'EU28'])

data_response = estat.data(resource_id = 'avia_paoc', key={'FREQ': 'M', 'UNIT': 'PAS', 'TRA_MEAS': 'PAS_CRD', 'GEO': 'UK', 'TRA_COV': 'TOTAL', 'SCHEDULE': 'TOT',}, params = {'startPeriod': '1993'}, dsd=dsd)
df = data_response.write(s for s in data_response.data.series)
```
