##aula 13 - Tópicos Complementares

from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np

dados = load_workbook("Teste dados python.xlsx", data_only = True)
pag = dados['Sheet1']

x = pag['A'] # Colunas A, C e E contêm os dados de X
y = pag['B'] # Colunas B, D e F contêm os dados de Y

X = np.array([c.value for c in x])
Y = np.array([c.value for c in y])

A = np.vstack([X, np.ones(len(X))]).T # Trocar a matriz de acordo com a função:
                                    # X, np.ones(len(X))) para linear
                                    # X**2, X, np.ones(len(X)) para quadrática
                                    # X para exponencial

m, b = np.linalg.lstsq(A, Y)[0] # Trocar os parâmetros de acordo com a função:
                                # Para a função linear, coeficiente m e b, para quadrática, a b e c
                                # Para exponencial, lna (não esqueça de fazer np.log(lna) para extrair o valor de a)

print(m, b)

eixoX = np.linspace(-20, 20) # Trocar o alcance para (0,4) com a função exponencial

plt.subplot(111)
plt.scatter(X, Y, s=8)
plt.plot(eixoX, eixoX*m + b) # Trocar a função de acordo com o teste sendo feito
                            # eixoX*m+b para linear
                            # a*eixoX**2+b*eixoX+c para quadrática
                            # a**eixoX para exponencial
