#aula 14.2 arquivo dict

# dict é uma coleção de objetos em que cada elemento está associado a uma chave única.
# Podemos usar qualquer dado imutável como chave, como strings, números ou tuplas.
# Os valores podem ser de qualquer tipo, incluindo outros dicionários.

# criando um dicionário
pessoa1 = {
    "nome": "paulo",
    "idade": 65,
    "cidade": "porto alegre",
    "profissao": "matematico"
}
print(pessoa1)  # saída: {'nome': 'paulo', 'idade': 65, 'cidade': 'porto alegre', 'profissao': 'matematico'}

# acessando valores
print(pessoa1["nome"])  # saída: paulo
print(pessoa1.get("idade"))  # saída: 65
print(pessoa1.get("pais", "brasil"))  # saída: brasil (valor padrão)
print(pessoa1.get("pais"))  # saída: None (chave não existe)

# adicionando ou atualizando valores
pessoa1["area"] = "analise aplicada"  # adiciona nova chave-valor
pessoa1["idade"] = 66  # atualiza valor existente
pessoa1.update({"cidade": "nova iorque"})
print(pessoa1)  # saída: {'nome': 'paulo', 'idade': 66, 'cidade': 'nova iorque', 'area': 'analise aplicada'}

# removendo valores
del pessoa1["cidade"]  # remove chave-valor
idade_removida = pessoa1.pop("idade")  # remove e retorna o valor
print(idade_removida)  # saída: 66
print(pessoa1)  # saída: {'nome': 'paulo', 'profissao': 'matematico'}

# iterando sobre um dicionário
for chave, valor in pessoa1.items():
    print(f"{chave}: {valor}")
# saída:
# nome: paulo
# profissao: matematico

# verificando se uma chave existe
if "nome" in pessoa1:
    print("a chave 'nome' existe no dicionário.")
# saída: a chave 'nome' existe no dicionário.
if "idade" not in pessoa1:
    print("a chave 'idade' não existe no dicionário.")
# saída: a chave 'idade' não existe no dicionário.

# limpando o dicionário
pessoa1.clear()
print(pessoa1)  # saída: {}

# dicionários aninhados
pessoa2 = {
    "nome": "josue",
    "idade": 33,
    "endereco": {
        "rua": "av. bento goncalves",
        "numero": 6000,
        "cidade": "porto alegre"
    }
}
print(pessoa2["endereco"]["cidade"])  # saída: porto alegre

# criando dicionário a partir de listas de tuplas
chaves = ["nome", "idade", "cidade", "profissao"]
valores = ["luan", 22, "sao paulo", "fisico"]
pessoa3 = dict(zip(chaves, valores)) # zip combina as listas em tuplas
print(pessoa3)  # saída: {'nome': 'luan', 'idade': 22, 'cidade': 'sao paulo', 'profissao': 'fisico'}

# compreensão de dicionários
# possui forma dict_comp = {expr-chave: expr-valor for item in colecao if condicao}
data = {"mateus": 1, "joao": 2, "felipe": 3, "rafael": 4, "maria luiza": 5}
ordem = {chave: valor for chave, valor in data.items() if valor <= 3}
print(ordem)  # saída: {'mateus': 1, 'joao': 2, 'felipe': 3}
# cria um novo dicionário apenas com os itens cujo valor é menor ou igual a 3