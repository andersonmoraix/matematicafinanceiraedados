#aula 19 graficos dinamicos e distribuições

# ==============================================================
# Gráficos Dinâmicos com Python 
# ==============================================================

import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Número de pontos
n = 50

# Tipos de distribuições
distribuicoes = ['Normal', 'Uniforme', 'Exponencial']

# Ativa o modo interativo (permite atualização do gráfico)
plt.ion()

# Loop principal — percorre cada distribuição
for dist in distribuicoes:

    # Vetores de dados
    x = np.arange(n)
    y = np.zeros(n)

    # Cria nova figura e eixos a cada distribuição
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

    # Configura os títulos e eixos
    ax1.set_title(f"Distribuição {dist}")
    ax1.set_xlabel("Índice da Amostra")
    ax1.set_ylabel("Valor Gerado")

    ax2.set_title("Histograma da Amostra")
    ax2.set_xlabel("Valor")
    ax2.set_ylabel("Frequência")

    # Geração e atualização dinâmica dos dados
    for i in range(n):
        # Gerando valor aleatório conforme o tipo de distribuição
        if dist == 'Normal':
            y[i] = random.gauss(0, 1)
        elif dist == 'Uniforme':
            y[i] = random.uniform(-2, 2)
        elif dist == 'Exponencial':
            y[i] = np.random.exponential(1)

        # Atualiza os gráficos
        ax1.clear()
        ax2.clear()

        # Reconfigura títulos e rótulos (eles são apagados com o clear)
        ax1.set_title(f"Distribuição {dist}")
        ax1.set_xlabel("Índice da Amostra")
        ax1.set_ylabel("Valor Gerado")

        ax2.set_title("Histograma da Amostra")
        ax2.set_xlabel("Valor")
        ax2.set_ylabel("Frequência")

        # Plota os pontos gerados até agora
        ax1.plot(x[:i+1], y[:i+1], '-o', color='tab:blue', alpha=0.7)
        ax2.hist(y[:i+1], bins=10, color='orange', alpha=0.7)

        # Ajusta o layout e pausa um instante
        plt.tight_layout()
        plt.pause(0.3)

    # Espera um pouco antes de passar para a próxima distribuição
    time.sleep(1.5)
    plt.close(fig)  # fecha a figura antiga

# Desativa o modo interativo e mostra o último gráfico (por segurança)
plt.ioff()
plt.show()
