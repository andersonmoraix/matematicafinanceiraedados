# Lendo e escrevendo arquivos
#aula 3


x = [4, 10, 20, 40]
f = open("hello.txt", "w")  # abre um arquivo para escrita (w=write)

f.write(
    "%d %d %d" % (x[0], x[1], x[2])
)  # grava os 3 primeiros elementos de x (d=numero inteiro)

f.close()  # fecha o arquivo

f = open("hello.txt", "r")  # abre o arquivo em modo leitura (r=read)

y = f.read()  # y lê as informações do arquivo hello.txt
f.close()

print(y)


f = open("hello2.txt", "w")

# f.write('%d %d %d' % (x[0],x[1],x[2]))
# grava 3 inteiros

# Imprimindo em colunas, não linhas: comando \n é uma quebra de linha
f.write("%d\n%d\n%d" % (x[0], x[1], x[2]))
f.close()

# - outros formatos para print


print("%s %5.2f %10.4e %d" % ("texto", 7.3, 1e-10, 341))

# 5.2f significa:
# 5=número de digitos para todo o número, incluindo o ponto
# 2=número de casas depois da vírgula
# ==> 7.3 vira 7.30, onde há uma casa em branco na frente

# 10.4e, e=notacao cientifica, 4 casas decimais
# ==> 1e-10 vira 1.0000e-10 (10 dígitos incluindo o ponto)

#################

g = open("hello3.txt", "w")  # abre um arquivo para escrita (w=write)

y = list(range(4))  # Lista com 4 elementos

# gravando todo a uma lista y a partir de entradas do usuário (comando 'input')
for i in range(len(y)):
    y[i] = input(f"Entre com o valor inteiro de y[{i}]= ")
    g.write("%d " % int(y[i]))  # comando 'int' converte string para inteiro

g.close()


# A mesma operação de abertura de arquivo feita acima poderia ser feita através
# da palavra chave "with", que garante que o objeto criado pelo python para representar
# o arquivo será fechado no final, sem a necessidade de chamar g.close() explicitamente

with open("hello3.txt", "r") as my_file:
    # operaçoes com o arquivo vão neste bloco
    print("Conteúdo do arquivo hello3.txt:")
    print(my_file.read())
# no final do bloco, o python invalida automaticamente a variável my_file,
# fechando a conexão com o arquivo

######################
import statistics as st

w = [10, 9, 2, 3, 11, 20, 20]
print("\n", w)

print("Média=", st.mean(w))

print("Mediana=", st.median(w))

print("Moda=", st.mode(w))

print("Desvio padrão=", st.stdev(w))

print("Média harmônica=", st.harmonic_mean(w))

print("Variância=", st.variance(w))
