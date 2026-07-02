# No Python:
# 1. Programação difere letras maíusculas e minúsculas
# 2. Ao programar repetições, o alinhamento do texto importa (veremos depois)

# No Spyder:
# ctrl shift + : aumenta fonte
# ctrl - : diminui fonte
# Seta para cima: recupera comandos anteriores


# impressão de texto: print(x)
print("Olá")

# atribuição de variáveis: sinal de =
z = 5
print(z)

# numeros fracionarios: separação parte fracionaria é feita com ponto (.)
x = 3.1
print(x)

# exponenciação: dois asteriscos
y = 3**2
print(y)

# resto da divisão de dois números: sinal %
w = y % z
print(w)

# No print(), texto pode ser limitado por ' ou "

print("x= ", x)
print("x= ", x)
print("x=", x, " , y=", y, ",z=", z)


# Variáveis podem ser incluídas na string e podem ser substituídas pelo seu valor
# através da função format()
print("o valor de x é {valor_de_x}".format(valor_de_x=x))

# Com strings interpoladas, as variáveis podem ser incluídas diretamente
# na string. Strings interpoladas levam o prefixo f
print(f"O valor de x é {x}")
