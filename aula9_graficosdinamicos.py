#aula 9 graficos dinamicos

# Gráfico dinâmico gerado a partir de amostra aleatória
# obtida segundo a distribuição normal (gaussiana)

import matplotlib.pyplot as gr
import random
import numpy as np

n = 20
x = np.zeros(n)
y = np.zeros(n)

for i in range(n):
    x[i] = i
    y[i] = random.gauss(0, 1)

ax = gr.subplot(111)
ax.set_xlim(0, n)         # define limites do eixo X
ax.set_ylim(-3, 3)        # define limites do eixo Y (dados gaussianos)

for i in range(1, n + 1): # começa em 1 e vai até n
    ax.plot(x[0:i], y[0:i], '-k')
    gr.pause(0.5)

gr.show()