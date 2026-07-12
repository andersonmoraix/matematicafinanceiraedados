#aula 15.1 exemplo 2

from faker import Faker
import json

fake = Faker('pt_BR')

# Exemplo 1: Gerando um fluxo de caixa para cálculo de VPL
print("--- Exemplo 1: Fluxo de Caixa para VPL ---")
investimento_inicial = -fake.random_int(min=50000, max=100000)
fluxo_caixa = [investimento_inicial]
for _ in range(5):  # 5 anos de retorno
    retorno = fake.random_int(min=10000, max=30000)
    fluxo_caixa.append(retorno)

print(f"Investimento e Retornos (6 períodos): {fluxo_caixa}")

# Exemplo 2: Gerando uma carteira de ações fictícia
print("\n--- Exemplo 2: Carteira de Ações Fictícia ---")
carteira = []
for _ in range(4):  # 4 ativos na carteira
    ativo = {
        'ticker': fake.lexify(text='????4.SA', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        'quantidade': fake.random_int(min=100, max=1000),
        'preco_compra': round(fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=10, max_value=80), 2)
    }
    carteira.append(ativo)

# Usando json.dumps para uma impressão mais legível (pretty-print)
print(json.dumps(carteira, indent=2, ensure_ascii=False))