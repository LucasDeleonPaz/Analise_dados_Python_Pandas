import pandas as pd

df = pd.read_csv('datasets\Gapminder.csv', sep=";")

df = df.rename(columns={
    "country": "Pais",
    "continent": "Continente", 
    "year": "Ano",
    "lifeExp": "Expectativa de Vida",
    "pop": "Populacao",
    "gdpPercap": "PIB"})
print(df.head(10)) #Parâmetro para amostragens do número de linhas que queremos
print(df.shape) # Total de linhas e colunas
print(df.columns) #Retorna uma lista com o nome das colunas existentes
print(df.dtypes) #Retorna o typo dos valores das células
print(df.tail(10)) #Retorna os últimos 10 itens da lista
print(df.describe()) #Retorna uma análise dos dados relativo ao conjunto de dados passados
print(df["Continente"].unique()) #Retorna uma lista com todos os possíveis itens de uma coluna.
brasil = df.loc[df["Pais"] == "Brazil"]
print(brasil.head(100))
print(brasil.describe())
print(df.groupby("Continente")["Pais"].nunique())
print(df.groupby("Ano")["Expectativa de Vida"].mean().sort_values())