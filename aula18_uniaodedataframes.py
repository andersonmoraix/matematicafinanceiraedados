#aula 18 uniao de data frames

import pandas as pd


#.concat(): Dois dataframes com mesmas colunas e dados distintos são unidos em termos das suas colunas gerando um dataframe único

#Primeiro dataframe

negocios_1 = pd.DataFrame({
    "Ticker": ["PETR4", "VALE3"],
    "Quantidade": [100, 50],
    "Preço": [37.20, 68.45]
   })

print("\nPrimeiro Dataframe:")
print(negocios_1)

#Segundo dataframe

negocios_2 = pd.DataFrame({
    "Ticker": ["ITUB4", "B3SA3"],
    "Quantidade": [200, 150],
    "Preço": [29.10, 13.75]
    })

print("\nSegundo Dataframe:")
print(negocios_2)

#Dataframe final resultado da união do tipo contact
negocios_total = pd.concat([negocios_1, negocios_2], ignore_index=True)

print("\nDataframe concatenado:")
print(negocios_total)

#.mrege(): Enriquecer um Dataframe com dados de outro Dataframe com base em uma coluna específica contida em ambos

#Primeiro dataframe
operacoes = pd.DataFrame({
    "Ticker": ["PETR4", "VALE3", "ITUB4"],
    "Tipo": ["Compra", "Venda", "Compra"],
    "Quantidade": [100, 50, 200]
    })

print("\nPrimeiro Dataframe:")
print(operacoes)

#Segundo dataframe
ativos = pd.DataFrame({
    "Ticker": ["PETR4", "VALE3", "ITUB4", "B3SA3"],
    "Setor": ["Petróleo", "Mineração", "Bancos", "Financeiro"],
    "Tipo_Ativo": ["PN", "ON", "PN", "ON"]
    })

print("\nSegundo Dataframe:")
print(ativos)


#Dataframe final resultado da união do tipo merge
dados_completos_left = pd.merge(operacoes, ativos, on="Ticker", how="left")
dados_completos_right = pd.merge(operacoes, ativos, on="Ticker", how="right")
dados_completos_inner = pd.merge(operacoes, ativos, on="Ticker", how="inner")

print("\nDataframe unido (left):")
print(dados_completos_left)
print("\nDataframe unido (right):")
print(dados_completos_right)
print("\nDataframe unido (inner):")
print(dados_completos_inner)