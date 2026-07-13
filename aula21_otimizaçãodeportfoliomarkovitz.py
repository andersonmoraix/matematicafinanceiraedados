import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

TICKERS = ["PETR4.SA", "ITUB4.SA", "GGBR4.SA", "B3SA3.SA"]

# ─── 1. Download dos dados ──────────────────────────────────────
raw_data = yf.download(
    TICKERS,
    period="2y",
    interval="1d",
    progress=False,
    auto_adjust=True,
)

# ─── 2. Extrai preços de fechamento ─────────────────────────────
# Nova estrutura do yfinance: colunas multiindex ('Close', ticker)
if isinstance(raw_data.columns, pd.MultiIndex):
    prices = raw_data['Close'][TICKERS]
else:
    prices = raw_data[['Close']]

prices = prices.dropna()
print(f"Total de dias válidos: {len(prices)}")
print(prices.tail())

# ─── 3. Cálculo dos retornos ────────────────────────────────────
returns_data = prices.pct_change().dropna()
print(f"\nRetornos calculados: {len(returns_data)} observações")
print(returns_data.head())

# ─── 4. Estatísticas anualizadas ────────────────────────────────
ws = 252
average_returns = returns_data.mean() * ws
cov_matrix = returns_data.cov() * ws

print(f"\nRetornos médios anualizados:")
print(average_returns)

# ─── 5. Função de retorno/risco ─────────────────────────────────
def w_expected_return_and_risk(avg_returns, cov, weights):
    port_return = np.dot(avg_returns, weights)
    port_vol = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))
    sharpe = port_return / port_vol if port_vol > 0 else 0
    return port_return, port_vol, sharpe

# ─── 6. Simulação de 50000 carteiras ────────────────────────────
NUM_PORTFOLIOS = 50000
portfolio_returns = np.zeros(NUM_PORTFOLIOS)
portfolio_risks = np.zeros(NUM_PORTFOLIOS)
portfolio_sharpes = np.zeros(NUM_PORTFOLIOS)

for i in range(NUM_PORTFOLIOS):
    w = np.random.random(len(TICKERS))
    w /= np.sum(w)
    ret, risk, sharpe = w_expected_return_and_risk(average_returns, cov_matrix, w)
    portfolio_returns[i] = ret
    portfolio_risks[i] = risk
    portfolio_sharpes[i] = sharpe

# ─── 7. Otimização ──────────────────────────────────────────────
def neg_sharpe(w):
    _, _, sharpe = w_expected_return_and_risk(average_returns, cov_matrix, w)
    return -sharpe

constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
bounds = tuple((0, 1) for _ in range(len(TICKERS)))
w0 = np.array([1/len(TICKERS)] * len(TICKERS))

result = optimize.minimize(
    neg_sharpe, w0, method="SLSQP",
    bounds=bounds, constraints=constraints
)
optimal = result.x
optimal_return, optimal_risk, optimal_sharpe = w_expected_return_and_risk(
    average_returns, cov_matrix, optimal
)

print(f"\n═══ CARTEIRA ÓTIMA ═══")
for ticker, peso in zip(TICKERS, optimal):
    print(f"  {ticker}: {peso*100:.2f}%")
print(f"Retorno esperado: {optimal_return*100:.2f}%")
print(f"Risco: {optimal_risk*100:.2f}%")
print(f"Sharpe Ratio: {optimal_sharpe:.4f}")

# ─── 8. Gráfico ─────────────────────────────────────────────────
plt.figure(figsize=(10, 6))
sc = plt.scatter(portfolio_risks, portfolio_returns,
                 c=portfolio_sharpes, cmap='viridis', marker='o', alpha=0.5)
plt.colorbar(sc, label='Sharpe Ratio')
plt.plot(optimal_risk, optimal_return, 'r*', markersize=25,
         label=f'Ótimo (Sharpe={optimal_sharpe:.3f})')
plt.xlabel('Risco (Volatilidade Anual)')
plt.ylabel('Retorno Esperado Anual')
plt.title('Fronteira Eficiente — Modelo de Markowitz')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
