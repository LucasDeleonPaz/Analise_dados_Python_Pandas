import pandas as pd

df_aracaju = pd.read_excel('datasets\Aracaju.xlsx')
df_fortaleza = pd.read_excel('datasets\Fortaleza.xlsx')
df_natal = pd.read_excel('datasets\Datala.xlsx')
df_recife = pd.read_excel('datasets\Recife.xlsx')
df_salvador = pd.read_excel('datasets\Salvador.xlsx')

df = pd.concat([df_aracaju, df_fortaleza, df_natal, df_recife, df_salvador]) #Concateno as tabelas por mim anteriormente importadas
print(df.head(1000))
print(df.describe())
print("*" * 50)
print(df.sample(5)) #Trago os dados simples de 5 itens da tabela, com diferenciação entre sí (Valores de cada cidade posta)
print("*" * 50)
df["LojaID"] = df["LojaID"].astype("object") #Altero o tipo do dado da coluna "LojaID" para string (object)
print(df.dtypes)
print("*" * 50)

print(df.isnull().sum()) #Faço um contagem de todas as células com valores nulos na tabela.
print("*" * 50)
print(df["Vendas"].mean()) #Retiro a média da coluna "Vandas"
df.dropna(subset=['Vendas'],inplace=True) #Excluo qualquer linha que tenha valores nulos na coluna "Vendas"
print("*" * 50)

df["Receita"] = df["Vendas"].mul(df["Qtde"]) #Crio uma nova coluna, que receberá por valor a multiplicação dos valores de vendas por quantidade.
print(df.head(10))
print("*" * 50)

print(df["Receita"].max()) #Retorno a maior receita - Porém, não informa qual é a loja responsável por essa venda
print("*" * 50)

print(df.nlargest(10, "Receita")) #Retorno o TOP 10 de maiores receitas, trazendo todos os dados (Loja, Cidade, Valores e etc)
print("*" * 50)

print(df.nsmallest(10, "Receita")) #Retorno o TOP 10 de menores receitas, trazendo todos os dados relativos à essas receitas.
print("*" * 50)

vendas = df.groupby("Cidade")["Receita"].sum()
print(vendas.sort_values())
print("*" * 50)

print(df.sort_values("Receita", ascending=False).head(10))