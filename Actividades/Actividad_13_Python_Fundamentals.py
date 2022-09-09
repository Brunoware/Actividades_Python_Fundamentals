#############################################################################################################
##########################################ACTIVIDAD: Básica##################################################
#############################################################################################################
# importar librerias 
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
## COMPETIDOR VETERANO
# leer dataframes
df=pd.read_csv('datasets/athlete_events.csv')
# quitar los nan
sample=df.loc[(df.Age.notna())&(df.Medal.notna())]
# competidor mayor
registro=sample.loc[sample.Age==sample.Age.max(),['Name','Age','Medal']].to_dict('record')[0]
# mostrar datos
print('Persona veterana con medalla de oro')
for key,value in registro.items():
    print(f'{key}: {value}')

## COMPETIDOR MAS JOVEN
df_oro=df.loc[df.Medal=='Gold']
registro_joven=df_oro.loc[df_oro.Age==df_oro.Age.min(),['Name','Age','Medal']].to_dict('record')[0]
# mostrar datos
print('\nPersona mas joven que ha recibido una medalla de oro')
for key,value in registro_joven.items():
    print(f'{key}: {value}')

## ENCONTRAR AL COMPETIDOR MAS GANADOR DE LA HISTORIA
# usando el dataframe limpio en medalla
print('\nPersona mas ganadora')
df_medal=df.loc[df.Medal.notna()]
nombre=df_medal.Name.value_counts().index[0]
registro_ganador=df_medal[df_medal.Name==nombre].to_dict('record')[0]
for key,value in registro_ganador.items():
    print(f'{key}: {value}')