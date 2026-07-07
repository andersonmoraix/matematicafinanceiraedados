#aula 6 aplicando estatistica

# ajuste de distrib probabilidade

import statistics as st
import matplotlib.pyplot as fig
import numpy as np      # necessario para vetores

from scipy.stats import norm       # curva gaussiana

# from permite importar apenas algumas coisas, e não
# o pacote inteiro

x=[4,2,1,0,4,10,9,8,11,14]

# fig.hist(x,bins=5,normed=True)

fig.hist(x,bins=6,density=True)

# bin=numero de barras
# normed=true - dados normalizados (versoes antigas)
# melhor usar 'density'

media=st.mean(x)
desvio=st.stdev(x)

# precisamos disto a seguir para a curva gaussiana
xmin,xmax=fig.xlim()    # limites do eixo x (dois valores)

eixox=np.linspace(xmin-4,xmax+4,100)   # o +-4 prolonga a curva para
#melhor visualizar a gaussiana e mostrar que o gráfico vai a zero nas bordas

eixoy=norm.pdf(eixox,media,desvio)

#pdf=prob distrib fcn (ver também cdf - cumulative)

fig.plot(eixox,eixoy)