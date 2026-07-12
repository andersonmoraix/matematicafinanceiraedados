#aula 21 Beta e CAPM 

# =============================================================
# EP. 14 — CAPM e estimação de Beta com Python
# Projeto de Extensão — Python e a Matemática de Dados Financeiros
# =============================================================
#
# O CAPM (Capital Asset Pricing Model) relaciona o retorno
# esperado de uma ação ao risco sistemático (beta) que ela
# carrega em relação ao mercado.
#
# Forma de regressão:
#     R_i - R_f  =  α  +  β · (R_m - R_f)  +  ε
#
# Onde:
#     R_i = retorno da ação
#     R_f = taxa livre de risco (SELIC)
#     R_m = retorno do mercado (Ibovespa)
#     α   = alfa de Jensen (intercepto)
#     β   = beta — sensibilidade ao mercado (inclinação)
#     ε   = erro

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


# =============================================================
# PARTE 1 — Parâmetros e download de dados
# =============================================================
#
# rf vem da SELIC anualizada — o número que calculamos no EP. 2
# usando a fórmula de juros compostos sobre 252 dias úteis.
# Para o vídeo, vamos hardcodar para manter o foco no CAPM.

rf_anual  = 0.1215           # SELIC anual ~12,15% (calculada no EP. 2)
rf_diario = (1 + rf_anual) ** (1/252) - 1   # converte para diária

# Ação principal e benchmark
acao      = "PETR4.SA"
benchmark = "^BVSP"          # Ibovespa


# =============================================================
# PARTE 2 — Baixando os preços históricos
# =============================================================
#
# yf.download() conecta na API pública do Yahoo Finance e baixa
# os preços de fechamento ajustados de qualquer ativo listado
# em bolsa. O parâmetro auto_adjust=True faz o yfinance corrigir
# automaticamente os preços por proventos (dividendos, splits),
# que é o que precisamos para calcular retornos corretamente.

precos = yf.download(
    [acao, benchmark],
    period='2y',
    auto_adjust=True,
    progress=False
)['Close']

precos = precos.dropna()     # remove dias em que algum dos dois não tem cotação
print(precos.head())
print(f"\nPeríodo: {precos.index[0].date()} → {precos.index[-1].date()}")
print(f"Total de pregões: {len(precos)}")

# 👁 Abra o Variable Explorer e veja `precos` como tabela:
#    duas colunas, uma para cada ticker, indexadas por data.


# =============================================================
# PARTE 3 — Calculando retornos diários
# =============================================================
#
# pct_change() calcula a variação percentual de um dia para o
# próximo. O primeiro valor sempre é NaN (não há dia anterior),
# por isso o dropna() em seguida.

retornos = precos.pct_change().dropna()
print(retornos.head())
print(f"\nRetorno médio diário de {acao}: {retornos[acao].mean():.4%}")
print(f"Retorno médio diário do Ibovespa: {retornos[benchmark].mean():.4%}")


# =============================================================
# PARTE 4 — Excesso de retorno
# =============================================================
#
# A regressão do CAPM não usa o retorno bruto — ela usa o
# excesso de retorno sobre a taxa livre de risco. Isso isola
# o "prêmio" que cada ativo entrega acima do que você ganharia
# sem correr risco no Tesouro.

excesso_acao = retornos[acao]      - rf_diario
excesso_mkt  = retornos[benchmark] - rf_diario


# =============================================================
# PARTE 5 — Estimando o beta por regressão linear
# =============================================================
#
# linregress(x, y) ajusta uma reta minimizando a soma dos
# quadrados dos resíduos. Devolve cinco valores:
#   slope     — inclinação (β do CAPM)
#   intercept — intercepto (α de Jensen)
#   rvalue    — correlação (R² é rvalue ao quadrado)
#   pvalue    — significância estatística do β
#   stderr    — erro padrão da estimação

resultado = linregress(excesso_mkt, excesso_acao)
beta  = resultado.slope
alfa  = resultado.intercept
r2    = resultado.rvalue ** 2

print(f"\n── Estimação CAPM para {acao} ──")
print(f"Beta  (β): {beta:.3f}")
print(f"Alfa  (α): {alfa:.6f}  (em retorno diário)")
print(f"R²       : {r2:.3f}")
print(f"p-valor  : {resultado.pvalue:.4e}")

# 👁 Variable Explorer: examine `resultado` para ver
#    todos os campos retornados pelo linregress.


# =============================================================
# PARTE 6 — Visualizando a regressão
# =============================================================
#
# O gráfico clássico do CAPM é um scatter onde cada ponto é um
# pregão: eixo X = excesso de retorno do mercado naquele dia,
# eixo Y = excesso de retorno da ação naquele dia. A reta
# ajustada tem inclinação β e intercepto α.

fig, ax = plt.subplots(figsize=(9, 7))

# Pontos da nuvem
ax.scatter(excesso_mkt, excesso_acao,
           alpha=0.4, s=18, color='steelblue',
           label='Pregões observados')

# Reta da regressão
x_reta = np.linspace(excesso_mkt.min(), excesso_mkt.max(), 100)
y_reta = alfa + beta * x_reta
ax.plot(x_reta, y_reta,
        color='firebrick', linewidth=2.2,
        label=f'Reta CAPM: α + β·(R_m - R_f)')

# Linhas guia em zero
ax.axhline(0, color='gray', linewidth=0.6, alpha=0.5)
ax.axvline(0, color='gray', linewidth=0.6, alpha=0.5)

# Anotação do beta — inclinação da reta
ax.annotate(
    f'β = {beta:.2f}\n(inclinação)',
    xy=(0.03, alfa + beta * 0.03),
    xytext=(0.045, -0.01),
    fontsize=11, color='firebrick',
    arrowprops=dict(arrowstyle='->', color='firebrick', alpha=0.7, lw=0.9)
)

# Anotação do alfa — intercepto
ax.annotate(
    f'α = {alfa*252:.2%} a.a.\n(intercepto)',
    xy=(0, alfa),
    xytext=(-0.05, 0.025),
    fontsize=11, color='darkgreen',
    arrowprops=dict(arrowstyle='->', color='darkgreen', alpha=0.7, lw=0.9)
)

ax.set_title(f'CAPM — {acao} vs Ibovespa', fontsize=14)
ax.set_xlabel('Excesso de retorno do mercado (R_m − R_f)')
ax.set_ylabel(f'Excesso de retorno de {acao} (R_i − R_f)')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# =============================================================
# PARTE 7 — Interpretando o beta
# =============================================================

if beta > 1.05:
    interpretacao = "MAIS volátil que o mercado (amplifica os movimentos)"
elif beta < 0.95:
    interpretacao = "MENOS volátil que o mercado (suaviza os movimentos)"
else:
    interpretacao = "se move junto com o mercado (beta próximo de 1)"

print(f"\n── Interpretação ──")
print(f"Beta = {beta:.3f} → {acao} {interpretacao}")
print(f"R² = {r2:.3f} → {r2:.1%} do risco de {acao} é explicado pelo mercado")
print(f"                ({1-r2:.1%} é risco específico, não-sistemático)")


# =============================================================
# PARTE 8 — Função reutilizável para estimar beta de qualquer ação
# =============================================================

def estimar_beta(ticker, benchmark='^BVSP', rf_anual=0.1215, periodo='2y'):
    """
    Estima o beta de uma ação contra um benchmark por regressão MQO.

    Parâmetros
    ----------
    ticker     : str   — ticker da ação (ex.: 'WEGE3.SA')
    benchmark  : str   — ticker do índice de mercado (default Ibovespa)
    rf_anual   : float — taxa livre de risco anual (decimal)
    periodo    : str   — janela do yfinance ('2y', '5y', etc.)

    Retorna
    -------
    dict com beta, alfa, R², p-valor e a regressão completa.
    """
    rf_dd = (1 + rf_anual) ** (1/252) - 1

    precos = yf.download([ticker, benchmark], period=periodo,
                         auto_adjust=True, progress=False)['Close'].dropna()
    rets   = precos.pct_change().dropna()

    res = linregress(rets[benchmark] - rf_dd, rets[ticker] - rf_dd)

    return {
        'ticker'  : ticker,
        'beta'    : res.slope,
        'alfa_aa' : res.intercept * 252,    # anualizado
        'r2'      : res.rvalue ** 2,
        'pvalor'  : res.pvalue,
        'n_obs'   : len(rets)
    }


# Comparação rápida com mais uma ação
print("\n── Beta de uma ação para comparação ──")
resultado_wege = estimar_beta('WEGE3.SA')
print(f"WEGE3.SA: β = {resultado_wege['beta']:.3f}, "
      f"R² = {resultado_wege['r2']:.3f}, "
      f"α = {resultado_wege['alfa_aa']:.2%} a.a.")