"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd
import numpy as np

def clean_data():

    df = pd.read_csv('solicitudes_credito.csv', sep = ';')

    df = df.dropna()

    df = df.drop(columns = ['Unnamed: 0'])

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(np.int64)

    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format = 'mixed', dayfirst = True)

    df['monto_del_credito'] = df['monto_del_credito'].str.split('.').str[0]
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(r'\D', '', regex = True)
    df['monto_del_credito'] = df['monto_del_credito'].astype(np.int64)

    string_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']
    replace_dict = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u',
        '-': ' ',
        '_': ' '
    }

    for string_column in string_columns:
        for key in replace_dict:
            df[string_column] = df[string_column].str.lower().str.replace(key, replace_dict[key])

    df = df.drop_duplicates()

    return df