#aula 20 SELIC na pratica

# =============================================================
# EP. 2 — SELIC via API do Banco Central (SGS)  [v2]
# Projeto de Extensão — Python e a Matemática de Dados Financeiros
# =============================================================
#
# Códigos de série úteis no SGS:
#   Série 11   = Taxa SELIC diária (% ao dia)
#   Série 12   = CDI diário        (% ao dia)
#   Série 433  = IPCA mensal       (% ao mês)
#   Série 4189 = SELIC anualizada  (% ao ano)
#
# Para consultar outros códigos:
#   https://www3.bcb.gov.br/sgspub/

import requests
import pandas as pd
import matplotlib.pyplot as plt


# =============================================================
# PARTE 1 — Puxando a SELIC diária
# =============================================================

codigo_serie = 11  # SELIC

url = (
    f"https://api.bcb.gov.br/dados/serie/"
    f"bcdata.sgs.{codigo_serie}/dados"
    f"?formato=json&dataInicial=01/01/2020&dataFinal=31/12/2024"
)

# requests.get(url) faz uma requisição HTTP e devolve um objeto Response.
# O timeout=15 evita que o programa fique travado se a API demorar a responder.
resposta = requests.get(url, timeout=15)
print(resposta.status_code)  # 200 = OK


# =============================================================
# PARTE 2 — Transformando JSON em DataFrame
# =============================================================
#
# O que é JSON?
# É um formato de texto usado por quase todas as APIs da internet
# para trocar dados. É basicamente uma lista de dicionários:
# cada item tem chaves ("data", "valor") e seus respectivos valores.
# O método .json() do objeto Response converte esse texto em uma
# estrutura nativa do Python (lista de dicts) que o pandas
# consegue transformar em DataFrame diretamente.
#
# Mais detalhes sobre JSON e leitura de arquivos estão na nossa
# página do Moodle.

dados = resposta.json()      # converte o texto JSON em lista de dicionários
df = pd.DataFrame(dados)      # cria um DataFrame a partir da lista
print(df.head())              # 👁  abra o "Variable Explorer" do Spyder
                              #     para visualizar o df como tabela

df['data']  = pd.to_datetime(df['data'], dayfirst=True)  # texto → datetime
df['valor'] = pd.to_numeric(df['valor'])                 # texto → float

print(df.dtypes)
print(f"\nTotal de registros: {len(df)}")
print(f"Período: {df['data'].min().date()} até {df['data'].max().date()}")


# =============================================================
# PARTE 3 — Da taxa diária para a taxa anual (juros compostos)
# =============================================================

ultimo = df['valor'].iloc[-1]
print(f"\nSELIC diária mais recente: {ultimo:.4f}%")

selic_diaria = ultimo / 100              # % → decimal
rf_anual = (1 + selic_diaria) ** 252 - 1 # juros compostos: M = C(1+i)^n → rf = (1+i)^252 - 1
print(f"Taxa livre de risco anual (rf): {rf_anual:.4%}")


# =============================================================
# PARTE 4 — Bônus: convertendo SELIC diária em taxas mensais
# =============================================================
#
# A SELIC mensal de um mês é a capitalização composta de todas
# as taxas diárias publicadas naquele mês:
#       (1 + d1) × (1 + d2) × ... × (1 + dN) - 1
# Em pandas isso vira um .resample('ME').apply(...)

df_decimal = df.copy()
df_decimal['valor'] = df['valor'] / 100  # converte para decimal

selic_mensal = (
    df_decimal
    .set_index('data')['valor']
    .resample('ME')                                  # agrupa por mês
    .apply(lambda x: (1 + x).prod() - 1)             # capitaliza
    * 100                                            # volta para %
)

print("\nSELIC acumulada por mês (últimos 6 meses):")
print(selic_mensal.tail(6).round(4))


# =============================================================
# PARTE 5 — Gráfico da SELIC diária
# =============================================================

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df['data'], df['valor'], color='steelblue', linewidth=1)
ax.set_title('Taxa SELIC diária — 2020 a 2024', fontsize=14)
ax.set_xlabel('Data')
ax.set_ylabel('Taxa (% ao dia)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# =============================================================
# PARTE 6 — Função genérica pra qualquer série do SGS
# =============================================================

def puxar_serie(codigo, inicio='01/01/2020', fim='31/12/2024'):
    """
    Puxa uma série temporal qualquer do SGS do Banco Central.

    Parâmetros
    ----------
    codigo : int
        Código numérico da série no SGS (ex.: 11 para SELIC).
    inicio, fim : str
        Datas de início e fim no formato DD/MM/AAAA.

    Retorna
    -------
    pd.DataFrame com colunas 'data' (datetime) e 'valor' (float).
    """
    url = (
        f"https://api.bcb.gov.br/dados/serie/"
        f"bcdata.sgs.{codigo}/dados"
        f"?formato=json&dataInicial={inicio}&dataFinal={fim}"
    )

    # 1) Faz a requisição HTTP — devolve um objeto Response.
    #    Se a internet falhar ou o BCB estiver fora do ar, o
    #    timeout=15 garante que o programa não trava esperando.
    r = requests.get(url, timeout=15)

    # 2) r.json() converte o texto retornado pela API (em formato
    #    JSON, que é uma lista de dicionários) em uma estrutura
    #    nativa do Python que o pandas aceita diretamente.
    df = pd.DataFrame(r.json())

    # 3) As colunas vêm como texto — precisamos converter:
    df['data']  = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = pd.to_numeric(df['valor'])

    return df


# =============================================================
# PARTE 7 — Comparando SELIC, CDI e IPCA na MESMA escala
# =============================================================
#
# Problema didático: SELIC e CDI são publicadas em % ao DIA.
# IPCA é publicado em % ao MÊS. Plotar os três juntos sem
# converter faz a SELIC e o CDI ficarem "esmagados" perto de zero
# enquanto o IPCA parece enorme.
#
# Solução: anualizar tudo.
#   • SELIC e CDI: aplicamos ponto a ponto (1 + i_diária)^252 - 1 —
#     a mesma fórmula de juros compostos da PARTE 3. Cada ponto
#     é a taxa que vigoraria em um ano se a taxa diária daquele
#     dia se repetisse. É o número que a mídia anuncia.
#   • IPCA: acumulado nos últimos 12 meses (janela móvel) —
#     o número padrão que o IBGE divulga e o Copom usa pra
#     calibrar a meta da SELIC.

# Puxando as séries diárias com a função
selic_diaria = puxar_serie(11)
cdi_diario   = puxar_serie(12)
ipca_mensal  = puxar_serie(433)

print("\nRegistros baixados:")
print("  SELIC:", len(selic_diaria), "registros (diários)")
print("  CDI:  ", len(cdi_diario),   "registros (diários)")
print("  IPCA: ", len(ipca_mensal),  "registros (mensais)")

# --- Anualizando SELIC e CDI ----------------------------------
# Aplicamos PONTO A PONTO a mesma fórmula de juros compostos da PARTE 3:
#       taxa_anual = (1 + taxa_diária) ** 252 - 1
# Cada ponto do gráfico responde à pergunta: "se a taxa diária de hoje
# vigorasse durante um ano útil inteiro (252 dias), quanto eu acumularia?"
# É exatamente o número que a mídia anuncia quando diz "SELIC a 13,75% a.a.".
# A curva fica em DEGRAUS — cada degrau é uma decisão do Copom.
def anualizar_diaria(df_dia):
    s = df_dia.set_index('data')['valor'] / 100
    return ((1 + s) ** 252 - 1) * 100

selic_anual = anualizar_diaria(selic_diaria)
cdi_anual   = anualizar_diaria(cdi_diario)

# --- Anualizando IPCA -----------------------------------------
# IPCA acumulado em 12 meses (janela móvel)
ipca = ipca_mensal.set_index('data')['valor'] / 100
ipca_anual = ((1 + ipca).rolling(window=12).apply(lambda x: x.prod()) - 1) * 100
ipca_anual = ipca_anual.dropna()

# --- Gráfico em escala comum ----------------------------------
fig, ax = plt.subplots(figsize=(12, 5.5))
ax.plot(selic_anual.index, selic_anual.values,
        label='SELIC (% a.a.)', color='steelblue', linewidth=1.6)
ax.plot(cdi_anual.index, cdi_anual.values,
        label='CDI (% a.a.)', color='orange', linewidth=1.6, linestyle='--')
ax.plot(ipca_anual.index, ipca_anual.values,
        label='IPCA acumulado 12m (% a.a.)', color='firebrick', linewidth=2)

ax.set_title('SELIC, CDI e IPCA — taxas anualizadas (2020–2024)', fontsize=14)
ax.set_xlabel('Data')
ax.set_ylabel('Taxa (% ao ano)')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

# Anotações: mínima histórica e pico da meta SELIC. Ambas ancoradas nos
# degraus reais da curva, com a caixa de texto posicionada DENTRO do gráfico.
ax.axhline(13.75, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
ax.annotate(
    'Meta SELIC trava em 13,75%\n(ago/2022 – ago/2023)',
    xy=(pd.Timestamp('2022-08-15'), 13.75),
    xytext=(pd.Timestamp('2020-04-01'), 11.0),
    fontsize=9, color='dimgray',
    arrowprops=dict(arrowstyle='->', color='gray', lw=0.8)
)
ax.annotate(
    'SELIC mínima histórica = 2%\n(ago/2020 – mar/2021)',
    xy=(pd.Timestamp('2020-12-15'), 2.0),
    xytext=(pd.Timestamp('2022-03-01'), 4.0),
    fontsize=9, color='dimgray',
    arrowprops=dict(arrowstyle='->', color='gray', lw=0.8)
)

plt.tight_layout()
plt.show()