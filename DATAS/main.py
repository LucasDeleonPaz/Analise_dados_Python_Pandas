import pandas as pd

df_aracaju = pd.read_excel('datasets\Aracaju.xlsx')
df_fortaleza = pd.read_excel('datasets\Fortaleza.xlsx')
df_natal = pd.read_excel('datasets\Datala.xlsx')
df_recife = pd.read_excel('datasets\Recife.xlsx')
df_salvador = pd.read_excel('datasets\Salvador.xlsx')

df = pd.concat([df_aracaju, df_fortaleza, df_natal, df_recife, df_salvador]) #Concateno as tabelas por mim anteriormente importadas

print(df.dtypes)
print("*" * 50)

df["Data"] = df["Data"].astype("int64")
print(df.dtypes)
print("*" * 50)

df["Data"] = pd.to_datetime(df["Data"])
print(df.dtypes)
print("*" * 50)

df["Receita"] = df["Vendas"].mul(df["Qtde"])

vendas_por_ano = df.groupby(df["Data"].dt.year)["Receita"].sum()
print(vendas_por_ano)
print("*" * 50)

df['Ano_Venda'] = df["Data"].dt.year
print(df.head(10))
print("*" * 50)

df['dia_venda'], df['mes_venda'] = (df["Data"].dt.day, df["Data"].dt.month)
print(df.sample(10))
print("*" * 50)

print(df["Data"].min())
print("*" * 50)

df['Diferenca_dias'] = df["Data"] - df["Data"].min()
print(df.sample(10))
print("*" * 50)

df['Trimestre_venda'] = df["Data"].dt.quarter
print(df.sample(10))
print("*" * 50)

vendas_abril_2019 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 4)]
print(vendas_abril_2019.head(10))
print("*" * 50)