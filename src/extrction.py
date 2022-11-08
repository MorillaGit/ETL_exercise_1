import requests
import logging
from pathlib import Path
from datetime import datetime

def data_extraction() -> list:
    """
    Download data from url, format csv, using its urls and save them locally in directory data/raw. called  "Data"
    """

    logging.info('Starting data extraction')

    # Define list of paths to save the data
    csv_paths = []

    categories_dict = {'estancias_jesuiticas': "https://datos.cultura.gob.ar/dataset/rutas-culturales/",
                       'calchaqui': "https://datos.cultura.gob.ar/dataset/rutas-culturales",
                       'yerbamate': "https://datos.cultura.gob.ar/dataset/rutas-culturales"
                          }

    # Generate the .csv files
    for category, url in categories_dict.items():
        b_path = Path('data/' + category + datetime.now().strftime('/%y-%m/'))
        f_path = category + '.csv'
        final_path = b_path / f_path

    # Create directory to save data
    b_path.mkdir(parents=True, exist_ok=True)

    # Save data
    with open(final_path, 'wb') as f:
        f.write(r)
        csv_paths.append(final_path)

    logging.info('Data extracted')

    return csv_paths


                