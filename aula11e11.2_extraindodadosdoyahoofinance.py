#aula 11 extraindo dados do yahoo finance

# Importação de ativos do Yahoo Finance
# Fazemos os gráficos de cada um dos ativos


import yfinance as yf
#import pandas as pd
import matplotlib.pyplot as gr
import numpy as np
import math as m
from scipy import stats


ticker = ["DIVO11.SA","KFOF11.SA"]

start_date = "2021-01-01"
end_date = "2025-08-15"


res=[]  # lista de DataFrames

# criamos uma lista onde cada elemento é um DataFrame (um para cada ativo)
# Depois, imprimimos os gráficos

for i in range(len(ticker)):
 res.append(yf.download(ticker[i], start=start_date, end=end_date))


# Colocamos os dados em uma matriz

lin=len(res[0].Close)
mat=np.zeros((lin,2))

for i in range(lin):
    for j in range(2):
        mat[i,j]=res[j].iloc[i,j];

print(mat)

eixox=np.arange(lin)
ax1=gr.subplot(211)

ax1.plot(eixox,mat[:,0],'--k',label='DIVO11')
ax1.set_title('Comparação entre DIVO11 e KFOF11 em 2025')


ax2=ax1.twinx()
ax2.plot(eixox,mat[:,1],'-b',label='KFOF11')
gr.legend()
ax2.grid()


########################
# Cálculo do retorno
res[0]['Retorno']=res[0].Close.pct_change(1)
res[1]['Retorno']=res[1].Close.pct_change(1)

ret1=res[0]['Retorno']
ret2=res[1]['Retorno']

eixR=np.arange(len(ret1))

ax1=gr.subplot(212)

ax1.plot(eixR,ret1,'--ok',label='DIVO11')
ax1.set_title('Retornos')

ax2=ax1.twinx()
ax2.plot(eixR,ret2,'-b',linewidth=1,label='KFOF11')
gr.legend()
gr.grid()

mi1=ret1.mean()
mi2=ret2.mean()
sigma1=ret1.std()
sigma2=ret2.std()
correl,pval=stats.pearsonr(ret1[1:],ret2[1:]) #correlação entre A e B

########################
# Risco de uma carteira formada por 70% de DIVO11 e 30% de KFOF11


pa=0.6
pb=1-pa
risco_cart=m.sqrt(pa**2*sigma1**2+pb**2*sigma2**2+2*pa*pb*correl*sigma1*sigma2)


#######################
# Risco da carteira

print('Média retorno (DIVO11)=',mi1)
print('Média retorno (KFOF11)=',mi2)
print('Desvio padrão (DIVO11)=',sigma1)
print('Desvio padrão (KFOF11)=',sigma2)
print('Coef. correlação dos ativos=',correl)
print('Risco da carteira=',risco_cart)

#########################
### Fronteira eficiente

p=np.arange(0,1,0.01)    
rc=np.zeros(len(p))
eixCart=np.zeros(len(p))
i=0

for x in p:
    y=1-x
    rc[i]=m.sqrt(x**2*sigma1**2+y**2*sigma2**2+2*x*y*correl*sigma1*sigma2)
    eixCart[i]=x
    i=i+1

gr.figure()
gr.plot(rc,eixCart,'-k')
gr.grid()
gr.xlabel('risco',fontsize=18)
gr.ylabel('retorno da carteira',fontsize=18)
gr.title('Fronteira Eficiente - (DIVO11, KFOF11)',fontsize=18)

# o valor minimo de risco ocorre, aproximadamente, para a escolha pa=0.6,
# produzindo risco 0.00810824
