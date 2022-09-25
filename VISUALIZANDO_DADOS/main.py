import pandas as pd
import matplotlib as plt


df_aracaju = pd.read_excel('datasets\Aracaju.xlsx')
df_fortaleza = pd.read_excel('datasets\Fortaleza.xlsx')
df_natal = pd.read_excel('datasets\Datala.xlsx')
df_recife = pd.read_excel('datasets\Recife.xlsx')
df_salvador = pd.read_excel('datasets\Salvador.xlsx')

df = pd.concat([df_aracaju, df_fortaleza, df_natal, df_recife, df_salvador]) #Concateno as tabelas por mim anteriormente importadas
valores = df["LojaID"].value_counts(ascending=False).plot.barh()

print(valores)
