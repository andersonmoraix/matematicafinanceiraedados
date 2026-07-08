#aula 8 filtrando dados e grupamentos

## Filtrando e agrupando dados com DataFrame, gravando em arquivo Excel
## Sugiro usar o prompt para examinar as informações com mais clareza

import pandas as pd

# personalizando linhas


df = pd.DataFrame(
    {
        'Produto': ['Tijolo', 'Tinta', 'Solvente', 'Telhas', 'Tijolo', 'Tinta'],
        'Preço':   [3.3, 4.5, 12, 27, 45.6, 5],
        'Qtde':    [10, 12, 23, 34, 4, 10],
        'Custo':   [0.5, 1.2, 1.4, 12, 12, 1.8]
    },
    index=['compra1', 'compra2', 'compra3', 'compra4', 'compra5', 'compra6']
)

print(df)

df['Produto']
df['Preço']    # andando por colunas

# loc - serve para achar indices (linhas)

df.loc['compra3']  # fornece o que está na linha 2


df.loc['compra3'].Produto # fornece o produto
# OU
df.loc['compra3']['Produto'] # fornece o produto

df.loc[(df['Produto']=='Tinta')].index
# acha as linhas que tiver Tijolo

# Se quisermos toda a informação
df.loc[(df['Produto']=='Tinta')]

# Se quisermos o preço
df.loc[(df['Produto']=='Tinta')].Preço
df.loc[(df['Produto']=='Tinta')]['Preço']

# Produtos com preços acima de 7 reais:
df.loc[df['Preço']>=7].Produto

df['Produto'].unique()   # sem repetição

df['Produto'].value_counts()  # quantidade

df['Produto'].value_counts(normalize=True)  # quantidade em percentual

###########################
# AGRUPAMENTOS - em blocos - groupby

# média - soma valores dos itens repetidos e divide pela quantidade
# Em geral, o agrupamento se refere a coisas que se repetem

x=df.groupby('Produto').mean()   

# mostra os valores maximos de cada coluna, para cada item
x=df.groupby('Produto').max()  

# elimina todas as linhas da coluna Preço
#axis=0 elimina ao longo das linhas
y=x.drop('Preço',axis=1) 


y.to_excel('plan2.xlsx')    # EXPORTA as informações
