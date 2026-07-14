#aula 21.2 - tuplas e estruturas de dados

import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize


TICKERS = [
    "PETR4.SA", # Petrobras
    "ITUB4.SA", # Banco Itau
    "GGBR4.SA", # Gerdau
    "B3SA3.SA", # B3 S.A.
]

# funcao que calcula os retornos diarios de cada ativo
def returns(prices):
    returns_data = pd.DataFrame()
    for ticker in prices.columns:
        returns_data[ticker] = (
            (
                prices[ticker] - prices[ticker].shift(1)
            ) / prices[ticker].shift(1)
        )[1:]
    return returns_data

# funcao que calcula o retorno medio de cada ativo
# juntamente com a matriz de covariancias
def calculate_statistics(returns_data, ws=252):
    average_returns = returns_data[-ws:].mean() * ws
    cov_matrix = returns_data[-ws:].cov() * ws
    return average_returns, cov_matrix

# funcao que calcula o retorno esperado e o risco associados
# a uma matriz de pesos W, aqui chamada de portfolio_weights
def w_expected_return_and_risk(
    R, cov_matrix, portfolio_weights, ws=252
):
    # annual returns
    portfolio_return = np.sum(R.mean() * portfolio_weights) * ws
    portfolio_volatility = np.sqrt(
        np.dot(portfolio_weights.T, np.dot(cov_matrix, portfolio_weights))
    )

    return (
        portfolio_return,
        portfolio_volatility,

        # como a taxa de retorno livre de risco e' fixa, para tornar a
        # implementacao mais simples, podemos ignora-la
        portfolio_return / portfolio_volatility,  #sharpe ratio
    )

# Primeiro, vamos baixar os dados historicos de todas as acoes
# Usando a funcao .interpolate() para lidar com dados faltantes
raw_data = yf.download(
    " ".join(TICKERS), interval="1d", period="max", progress=False
).interpolate(axis=1)

# Usaremos apenas o preco de fechamento, na coluna "Close"
data = pd.DataFrame()
for ticker in TICKERS:
    data[ticker] = raw_data["Close"][ticker]
prices = data.dropna()

R = returns(data)
average_returns, cov_matrix = calculate_statistics(R)


# agora, vamos simular 50000 carteiras
NUM_PORTFOLIOS = 50000
portfolio_mean_returns = []
portfolio_risks = []
for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(len(TICKERS))
        w /= np.sum(w)

        w_return, w_risk, sharpe = w_expected_return_and_risk(R, cov_matrix, w)
        portfolio_mean_returns.append(w_return)
        portfolio_risks.append(w_risk)

# agora, a otimizacao
MAX_ACCEPTED_RISK = 0.17
def max_function_sharpe(w0, args):
    returns, cov_matrix = args
    _, _, sharpe_ratio = w_expected_return_and_risk(R, cov_matrix, w0)
    # aqui, devemos maximizar o valor da variavel sharpe_ratio
    # como o scipy apenas minimiza funcoes, minimizaremos (-1) * sharpe_ratio
    return -sharpe_ratio


def optimize_portfolio(w0, returns, cov_matrix):
    # usamos essa restricao para garantir que o vetor tem soma 1.
    # type: "eq" nos diz que a restricao e' do tipo igualdade
    # e a funcao fica np.sum(x) - 1
    # no scipy, sempre definimos um lado da equacao, o outro e' sempre
    # zero automaticamente
    w_sum_constraint = {"type": "eq", "fun": lambda x: np.sum(x) - 1}

    # limites dos pesos. sempre entre 0 e 1
    bounds = tuple((0, 1) for _ in range(len(TICKERS)))

    return optimize.minimize(
        fun=max_function_sharpe,
        x0=w0, # aqui, o w0 e' nosso w inicial. o otimizador trabalha a partir dele
        args=[returns, cov_matrix],
        method="SLSQP",
        bounds=bounds,
        constraints=w_sum_constraint,
    # a funcao 'optimize' retorna um objeto com varias propriedades, mas, aqui
    # a propriedade 'x' nos interessa e vamos retornar apenas ela. Neste caso
    # 'x' contem o resultado da otimizacao, ou seja, o vetor de pesos W otimo
    )["x"]

optimal = optimize_portfolio(np.random.random(len(TICKERS)), returns, cov_matrix)
optimal_return, optimal_risk, optimal_sharpe = w_expected_return_and_risk(
            R, cov_matrix, optimal
        )

plt.figure(figsize=(10, 6))
plt.scatter(portfolio_risks, portfolio_mean_returns, c=np.array(portfolio_mean_returns) / np.array(portfolio_risks), marker="o")
plt.plot(optimal_risk, optimal_return, "g*", markersize=15)
plt.show()