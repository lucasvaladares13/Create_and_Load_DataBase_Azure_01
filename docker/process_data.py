import pandas as pd
import os

Dict_Cols = {'Bola1': 'Dig1',
'Bola2': 'Dig2',
'Bola3': 'Dig3',
'Bola4': 'Dig4',
'Bola5': 'Dig5',
'Bola6': 'Dig6',
'Bola7': 'Dig7',
'Bola8': 'Dig8',
'Bola9': 'Dig9',
'Bola10': 'Dig10',
'Bola11': 'Dig11',
'Bola12': 'Dig12',
'Bola13': 'Dig13',
'Bola14': 'Dig14',
'Bola15': 'Dig15',
'Data_Sorteio':'Data',
'Concurso':'ID'
}

path = os.path.dirname(os.path.realpath(__file__))
path = '\\'.join(path.split('\\')[0:-1])
print(path)
df = pd.read_csv(f'{path}\\Data\\hist_data.csv', sep= '\t', keep_default_na = False)
df['Concurso'] = pd.to_numeric(df['Concurso'], errors = 'coerce' )
df['Data_Sorteio'] = pd.to_datetime(df['Data_Sorteio'], errors = 'coerce', format = '%d/%m/%Y' )
df = df[(df.Concurso.notna() )& (df.Data_Sorteio.notna() )].reset_index(drop=True)
df['Concurso'] = df['Concurso'].astype(int)
for i in range(1,16):
    df[f'Bola{i}'] = df[f'Bola{i}'].astype(int)

df = df.rename(columns=Dict_Cols)
df = df[Dict_Cols.values()]

print(df)