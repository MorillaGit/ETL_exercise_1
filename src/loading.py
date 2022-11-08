import logging
from sqlalchemy import create_engine
from setting import *
import pandas as pd

def data_loading(list_dataframes: list[pd.DataFrame]) -> None:

    """
    load dataframes to sql database
    
    Parameters
    ----------
    list_dataframes : list[pd.DataFrame]
        list of dataframes to load.
    """
    logging.info('Starting data loading')
    # Create engine to connect to database
    engine = create_engine(f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    # Create empty table from .sql file
    engine.execute(open('src/tables.sql', 'r', encoding='utf-8').read())

    # Load dataframes to database
    for dataframe in list_dataframes:
        dataframe.to_sql(dataframe.name, engine, if_exists='append', index=False)

    logging.info('Data loading finished')

    return