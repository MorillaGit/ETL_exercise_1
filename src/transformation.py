import pandas as pd
import numpy as np
import logging
from datetime import datetime

def data_transformation(csv_path: list) -> list[pd.DataFrame]:
    
    """
    transforma csv to sql table

    Parameters
    ----------
    csv_path : list
        path of the csv files.
    """

    logging.info('Starting data transformation')
    list_dataframes = []

    estancias_jesuiticas = pd.read_csv(csv_path[0])
    calchaqui = pd.read_csv(csv_path[1])
    yerbamate = pd.read_csv(csv_path[2])

    # select data columns form each dataframe

    # interest columns
    interes_cols = ['Cod_Loc', 'IdProvincia', 'IdDepartamento',
                    'Categoría', 'Provincia', 'Fuente','Localidad',
                    'Nombre', 'Localidad','Descripción','Monumentos',
                    'Museos', 'Latitud', 'Longitud','Artesanías típicas',
                    'Ferias', 'Comidas típicas','Sitios de interés']

    d1_sdf = pd.DataFrame(estancias_jesuiticas[interes_cols])
    d2_sdf = pd.DataFrame(yerbamate[interes_cols])
    d3_sdf = pd.DataFrame(calchaqui[interes_cols])

    d1_cols_rename =   {'Cod_Loc': 'cod_loc',
                        'IdProvincia': 'id_provincia',  
                        'IdDepartamento': 'id_departamento',
                        'Categoría': 'categoria',
                        'Provincia': 'provincia',
                        'Fuente': 'fuente',
                        'Localidad': 'localidad',
                        'Nombre': 'nombre',
                        'Descripción': 'descripcion',
                        'Monumentos': 'monumentos',
                        'Museos': 'museos',
                        'Latitud': 'latitud',
                        'Longitud': 'longitud',
                        'Artesanías típicas': 'artesanias_tipicas',
                        'Ferias': 'ferias',
                        'Comidas típicas': 'comidas_tipicas',
                        'Sitios de interés': 'sitios_de_interes'
                    }

    d1_sdf.rename(columns=d1_cols_rename, inplace=True)
    d2_sdf.rename(columns=d1_cols_rename, inplace=True)
    d3_sdf.rename(columns=d1_cols_rename, inplace=True)

    # create a single dataframe with the information from all categories
    main_df = pd.concat([d1_sdf, d2_sdf, d3_sdf], axis = 0)

    # drop colum fuentes
    clean_df = pd.DataFrame(main_df.drop('fuente', axis='columns'))
    clean_df.reset_index(drop=True, inplace=True)

    # add to list of dataframes
    list_dataframes.append(clean_df)

    # total columns "comida_tipica" per category
    comida_tipica = pd.DataFrame(main_df.groupby('categoria')['comidas_tipicas'].count().reset_index())
    comida_tipica.rename(columns={'total': 'Numero de comidas_tipicas'}, inplace=True)

    # total columns "ferias" per category
    ferias = pd.DataFrame(main_df.groupby('categoria')['ferias'].count().reset_index())
    ferias.rename(columns={'total': 'Numero de ferias'}, inplace=True)

    # Records per province and category
    cols = ["provincia", "categoria"]    
    provincias_museos = pd.DataFrame(main_df.groupby(cols)['museos'].size().reset_index(name='total'))
    provincias_museos.rename(columns={'total': 'Numero de museos'}, inplace=True)

    # Join the different information
    transform_data = pd.concat([ferias, comida_tipica,provincias_museos], axis=1)
    transform_data = transform_data.loc[:,~transform_data.columns.duplicated()]
    cols = list(transform_data)
    cols.insert(0, cols.pop(cols.index('provincia')))
    transform_data = transform_data.loc[:, cols]

    # add to list of dataframes
    list_dataframes.append(transform_data)

    logging.info('Data transformation finished')

    return list_dataframes