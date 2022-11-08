# install libraries
from scr.extraction import *
from scr.transformation import *
from scr.loading import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':

    # Try to download data, process it and upload it to the database. If it fails, send a message error to the user.
    try:
        # logging
        logging.info('Starting the process')
        csv_paths = data_extraction()
        logging.info('Data extracted')
        all_data = data_transformation(csv_paths)
        logging.info('Data processed')
        data_loading(all_data)
        logging.info('Data loaded')
    except Exception as e:
        logging.error('Process failed')
        logging.error(e)
    
    else:
        logging.info('Process finished')
