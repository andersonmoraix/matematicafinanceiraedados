#aula 6 graficos histogramas e boxplot

# vetores - indicados com colchetes (mais versáteis que listas)
# devemos importar numpy
# sempre devem ser inicializados (np.zeros(n))

import numpy as np


n=int(input('numero de termos = '))

x=np.zeros(n)
y=np.zeros(n)

soma=0

for i in range(n):
 x[i]=float(input('x = '))
 y[i]=10*x[i]
 soma=soma+x[i]+y[i]
print("Soma das coordenadas de x e y=",soma)

print("\nMais informações\n")

print("Soma dos elementos de x= ",x.sum())     # soma os termos de x. Mais simples que usar for
print("Média dos elementos de x= ",x.mean())  # media dos elementos de y
print("Desvio padrão de x=",x.std())          # desvio padrao
print("Valor mínimo de x=",x.min())
print("Valor máximo de x=",x.max())
print("Posição do menor valor de x=",x.argmin()) 
print("Posição do maior valor de x=",x.argmax()) 

soma=x+y  # podemos somar vetores
print(soma)