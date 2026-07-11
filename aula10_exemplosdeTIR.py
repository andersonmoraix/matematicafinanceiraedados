#aula 10 exemplos de TIR

# É preciso instalar
# pip install numpy_financial

import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as fig

FC=np.zeros(6)
FC[0]=-60000
for i in range(5):
    FC[i+1]=40000-10000

tir=npf.irr(FC)

print('TIR=', str(round(100*tir,2)),'%')

eixox=np.linspace(0,0.5,200) #para gerar 200 pontos espaçados
vpl=np.array([npf.npv(i,FC) for i in eixox]) #valor presente líquido para varias escolhas de taxas
fig.plot(eixox,vpl,'--k',linewidth=2)
fig.plot(tir,0,'kx',markersize=15)
fig.xlabel('Juros - i')
fig.title('TIR - taxa interna de retorno',fontsize=16)
fig.grid()