#aula 8 estruturas e series

# Biblioteca Pandas
# Analise de dados melhor que vetores, matrizes e listas

# Pandas parece com Access e tabela dinamica do Excel
# Util para data mining, investigações, tendências, análise
# de variabilidade

# Funcao Time Series - complemento para Statistics

# Não é possível misturar strings e dados em vetores. Mas com Pandas
# isso é possível! Com Time Series

import pandas as pd
import numpy as np

preco=pd.Series([3.4,4.3,5.5,12.3,5.0],index=['Tijolos','Tinta','Telhas','Cola','Solvente'])
print(preco)

preco['Tijolos']    # facilidade de busca

preco['Telhas']

print(preco.mean())   # estatistica basicas - facil de obter
print(preco.std())

print(preco.describe())   # colecao de estatisticas

quadrado=preco**2
precolog=np.log(preco)  # podemos combinar com numpy

print(quadrado)
