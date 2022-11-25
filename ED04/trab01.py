"""
Na primeira pilha  vai as cartas maiores

na segunda vai os numeros restantes

"""
# somar os 4 maiores e acresentar o 2 ao final
pilha1 = [10,9,8,7,2]  # = 36


print("Pilha de cartas 1")
x = 0
soma_p1 = pilha1[0] + pilha1[1] + pilha1[2] + pilha1[3] + pilha1[4]
lmt = len(pilha1)

while  x > lmt:
  print(pilha1[x])  
  x-= 1
  
print("soma total Pilha 1 :", soma_p1)


# multiplicar os numeros restantes
pilha2 = [1,3,4,5,6] # 360

mul_p2 = pilha2[0] * pilha2[1] *pilha2[2] * pilha2[3] * pilha2[4]
lmt = len(pilha2)

while  x > lmt:
  print(pilha2[x])  
  x-= 1

print("Pilha de cartas 2")

 
print("soma total Pilha 2 :", mul_p2)
