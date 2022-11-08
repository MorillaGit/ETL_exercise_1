import logging
from sqlalchemy import create_engine
from setting import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
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
    list_dataframes[0].to_sql('ppal_table', con=engine, if_exists='replace', index=False)
    list_dataframes[1].to_sql('transformation_table', con=engine, if_exists='replace', index=False)

    logging.info('Data loading finished')

    return