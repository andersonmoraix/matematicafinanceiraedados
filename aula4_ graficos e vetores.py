#aula 4 graficos e vetores(numpy e maplotlib)

#MENU PREFERENCIAS - IPYTHON - GRÁFICOS - SAIDA GRÁFICA - 
#colocar saída automática (produz gráfico em janela separada)


import numpy as np

import matplotlib.pyplot as gr

x=np.arange(-10,10) # vetor sequencial

y=3*x**2-1     #- cria um novo vetor a partir de x

gr.plot(x,y)


gr.plot(x,y);gr.xlabel('Eixo x');gr.ylabel('Eixo y')

gr.title("$y = 3x^2-1$")  # expressão em LaTex

gr.grid() #- coloca uma grade ao fundo

gr.savefig('fig1.jpg')


import numpy as np

import matplotlib.pyplot as gr

x = np.arange(-10,10)

y=3*x**2-1

gr.plot(x,y)
Out[5]: [<matplotlib.lines.Line2D at 0x7b9c5c2cd810>]

gr.plot(x,y);gr.xlabel('Eixo x');gr.ylabel('Eixo y')
Out[6]: Text(0, 0.5, 'Eixo y')

gr.title("$y=3x²-1$")
Out[7]: Text(0.5, 1.0, '$y=3x²-1$')

gr.savefig('fig1.jpeg')
<Figure size 864x576 with 0 Axes>

import matplotlib.pyplot as gr

x = np.arange(-10,10)

y=2*x

z=x**5+7

w=-2*x**2-1

gr.subplot(311);gr.plot(x,y);gr.title('mais graficos');gr.grid()

gr.subplot(312);gr.plot(x,z);gr.title('mais graficos');gr.grid()

gr.subplot(313);gr.plot(x,w);gr.title('mais graficos');gr.grid()

lista=[10,2,-4,5,1,15,7]

vetor=np.array(lista)

ret=vetor[1:7]-vetor[0:6]/vetor[0:6]

gr.plot(ret)
Out[20]: [<matplotlib.lines.Line2D at 0x7b9c4735e5d0>]