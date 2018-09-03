# Project Backlog

## Eurostat Data

- Group countries into arbitary regions and forecast per region

- ARIMA and Prophet models
    - [ARIMA](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)
    - seasonal naive baseline

- ETL pipeline to take extract raw data into SQLite table
    - connect Tableau workbook to SQLite

- Airflow pipeline to process data

- Metadata file `run-output.txt` created on every pipeline stage
    - contains run date (e.g. extract data for fetch stage)
    - presence of file signals stage complete so next stage can run

- Prophet train stage
    - persist trained models to pickled files
    - metadata with pickle filename, country name, train date, train window

- Prophet predict stage
    - loads pickle model from earlier stage, uses for forecast
    - metadata with forecast horizon

- Evaluation metrics
    - produce on backtest
    - compare against Prophet and ARIMA models against actuals

- Document analysis pack
    - Jinja2 template to create markdown / epub with analysis
    - mobile friendly?

- Web dashboard to view analysis


## UK CAA Data

- Bring in UK passenger data from CAA, down to airport level

- UK to rest of world route analysis

- Flight data

- Reliability (service on-time) data

### Analysis

- Routes per region over time
    - do they remain constant, increase / decrease?