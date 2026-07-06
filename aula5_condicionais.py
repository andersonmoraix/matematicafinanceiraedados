#aula 5

# Exemplos básicos do uso de condicionais


###################
# while

cont=1
x=0
while x<20:
 x=cont*3
 cont=cont+1
 print(x)


#####################
## if-then-else


x=float(input("\nDigite um valor para x= "))
y=float(input("Digite um valor para y= "))

if x>y:
  print("x=",x, "é maior que y=",y,)
elif x==y:
  print("x=",x, "é igual y=",y,)
else:
 print("x=",x, "é menor que y=",y,)
 
###################
# for

for i in range(0,10,2):  # números de 0 a 9, indo de 2 em 2
 print(i+10)
 
