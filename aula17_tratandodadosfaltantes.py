#aula 17 complementar, tratando dados faltantes

import pandas as pd
import numpy as np

# Lista com os dados
dados = [
    {"ID": 1, "Ativo": "PETR4", "Data Fechamento": "2025-09-30", "Valor Fechamento": 38.45, "Quantidade": 100, "Total": 3845.00},
    {"ID": 2, "Ativo": "PETR4", "Data Fechamento": "2025-10-01", "Valor Fechamento": 0,     "Quantidade": 80,  "Total": 0.00},
    {"ID": 3, "Ativo": "PETR4", "Data Fechamento": "2025-10-02", "Valor Fechamento": np.nan, "Quantidade": 95,  "Total": np.nan},

    {"ID": 4, "Ativo": "VALE3", "Data Fechamento": "2025-09-30", "Valor Fechamento": 67.80, "Quantidade": 60,  "Total": 4068.00},
    {"ID": 5, "Ativo": "VALE3", "Data Fechamento": "2025-10-01", "Valor Fechamento": 68.05, "Quantidade": 50,  "Total": 3402.50},
    {"ID": 6, "Ativo": "VALE3", "Data Fechamento": "2025-10-02", "Valor Fechamento": 68.25, "Quantidade": 0,   "Total": 0.00},

    {"ID": 7, "Ativo": "ITUB4", "Data Fechamento": "2025-09-30", "Valor Fechamento": 28.90, "Quantidade": np.nan, "Total": np.nan},
    {"ID": 8, "Ativo": "ITUB4", "Data Fechamento": "2025-10-01", "Valor Fechamento": np.nan,    "Quantidade": 120,    "Total": np.nan},
    {"ID": 9, "Ativo": "ITUB4", "Data Fechamento": "2025-10-02", "Valor Fechamento": 29.00, "Quantidade": 0,      "Total": 0.00},

    {"ID": 10, "Ativo": "ABEV3", "Data Fechamento": "2025-09-30", "Valor Fechamento": 14.30, "Quantidade": 100, "Total": 1430.00},
    {"ID": 11, "Ativo": "ABEV3", "Data Fechamento": "2025-10-01", "Valor Fechamento": 0,     "Quantidade": 100,  "Total": 0.00},
    {"ID": 12, "Ativo": "ABEV3", "Data Fechamento": "2025-10-02", "Valor Fechamento": np.nan,"Quantidade": np.nan, "Total": np.nan},

    {"ID": 13, "Ativo": "",      "Data Fechamento": "2025-09-30", "Valor Fechamento": 15.75, "Quantidade": 0,    "Total": 0.00},
    {"ID": 14, "Ativo": "",      "Data Fechamento": "2025-10-01", "Valor Fechamento": "",    "Quantidade": "",   "Total": ""},
    {"ID": 15, "Ativo": "",      "Data Fechamento": "2025-10-02", "Valor Fechamento": 16.00, "Quantidade": 10,   "Total": 160.00},
]

# Criar DataFrame
df = pd.DataFrame(dados)

# Exibir o DataFrame
print("\nDataframe completo")
print(df)

#Identificando Texto Vazio

print("\nDataframe com campos vazios")
print(df[df["Ativo"] == ""])


#Identificando Valores zero

print("\nDataframe com zero")
print(df[df["Quantidade"] == 0])


#Identificando casos de NaN

print("\nDataframe com NaN")
print(df[df['Valor Fechamento'].isna()])

print(df.isnull().sum())

#Filtrando os dados para manter apenas os Ativos que não estão em branco

#Removendo textos vazios
df_texto_vazio_removido = df[df["Ativo"] != ""]

# Exibir o DataFrame
print("\nDataframe com textos em branco removidos")
print(df_texto_vazio_removido)


#Removendo zeros
df_zero_removido = df[df["Valor Fechamento"] != 0]

# Exibir o DataFrame
print("\nDataframe com zeros removidos")
print(df_zero_removido)

#Removendo textos vazios

df_nan_removido = df.dropna()

# Exibir o DataFrame
print("\nDataframe com NaN removidos")
print(df_nan_removido)


#Tratando dados faltantes

#Novo dataframe apenas com dados de ITUB4
df_itub4 = df[df["Ativo"] == "ITUB4"]
print(df_itub4)

#NaN alterado por Forward Fill

df_forward_fill = df_itub4.ffill()

#Exibe o dataframe
print("\nDataframe com NaN alterado por Forward Fill")
print(df_forward_fill)

#NaN alterado por Backward Fill

df_backward_fill = df_itub4.bfill()

#Exibe o dataframe
print("\nDataframe com NaN alterado por Backward Fill")
print(df_backward_fill)


#Nan alterado por Valor Estatıstico

df_itub4["Valor Fechamento"] = df_itub4["Valor Fechamento"].fillna(df_itub4["Valor Fechamento"].mean())

#Exibe o dataframe
print("\nDataframe com NaN alterado por Valor Estatıstico")
print(df_itub4)


#Nan alterado por Valor Estatıstico

df_itub4["Valor Fechamento"] = df_itub4["Valor Fechamento"].fillna(df_itub4["Valor Fechamento"].mean())


#Reconstituindo o df_itub4 para usa-lo no proximo exemplo
df_itub4 = df[df["Ativo"] == "ITUB4"]


#Nan alterado por Valor Fixo, método 1
df_itub4["Valor Fechamento"] = df_itub4["Valor Fechamento"].fillna(28.80)


#Exibe o dataframe
print("\nDataframe com NaN alterado por Valor Fixo 1")
print(df_itub4)


#Nan alterado por Valor Fixo, método 2
df_itub4.loc[(df_itub4['Data Fechamento'] == '2025-09-30') & (df_itub4['Quantidade'].isna()), 'Quantidade'] = 120


#Exibe o dataframe
print("\nDataframe com NaN alterado por Valor Fixo 2")
print(df_itub4)

#Valores alterados pro recalculo de coluna
df_itub4['Total'] = df_itub4['Quantidade'] * df_itub4['Valor Fechamento']


#Exibe o dataframe
print("\nRecalculando uma coluna")
print(df_itub4)