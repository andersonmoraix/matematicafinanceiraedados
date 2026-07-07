#aula 6 - graficos

import numpy as np
import matplotlib.pyplot as gr

#import math
from math import cos,exp

n=int(input('Numero de pontos a serem impressos= '))

x=np.zeros(n)
y=np.zeros(n)    # define vetores com n coordenadas
z=np.zeros(n)

for i in range(n):
    x[i]=i*0.1
    y[i]=exp(-0.1*x[i])*cos(x[i])
    z[i]=cos(x[i])+1


gr.plot(x,y,'-b',x,z,'-r')   # -=curva continua dos gráficos de y(x) e de z(x)
gr.title('Um título')

## -- = tracejado
## g=green, k=black
## '-og' - bolas
## '+og' - cruz
