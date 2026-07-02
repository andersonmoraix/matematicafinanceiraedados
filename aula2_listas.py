# Listas aula 2
# Começam com índice 0

dados = [2, 3, 4, -5]  # lista com 4 elementos, indexados de 0 a 3

print(dados)

print(dados[0])  # primeiro elemento da lista

print(dados[3])  # último elemento

print(dados[-1])  # último elemento da lista

print(dados[-2])  # penúltimo elemento

len(dados)  # comprimento da lista

lista2 = ["ações", "títulos", "criptoativos", "CDB", "FII", "multimercado", "ETF"]

print(lista2[0:3])  # elementos 0, 1 e 2 (vai um a menos)

print(lista2[0:6:2])  # começa em 0, indo até o índice 6, pulando de 2 em 2

print(lista2[::-1])  # lista de trás pra frente

############
# Busca: comando 'in' :

busca = "dolar" in lista2
print(busca)  # retorna 'False', pois a busca não está na lista

## Trocando elementos de uma lista:

lista2[1] = "dolar"
lista2[0:3] = ["reais", "ouro", "poupança"]

# Adicionando elementos:

lista2.append("euro")  # adiciona 1 palavra no final
lista2.extend(["peso", "dolar", "yen"])  #  adiciona lista ao final

# Ordenando lista:

lista2.sort()  # ordem crescente (separa maiusculas/minusculas)

# Ordenacao independente do caps (letras maiúsculas/minusculas):

lista2.sort(key=str.casefold)  # independente de caps

lista2.reverse()  # ordem reversa

lista2.remove("multimercado")  #  remove elementos

# Fatiando listas

lista2[1:]  # lista a partir do 1 até o final

lista2[3:]  # a partir de indice 3

lista2[:3]  # lista apenas com indices 0, 1, 2


# Outros comandos


lista2.index("ETF")  # menor indice que contem tal string
lista2.index("CBD")  # erro

lista2.insert(3, "outros")  # insere na posição 3 o elemento 'outros'

# lista2.clear() # remove todos os elementos