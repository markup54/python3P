lista=[]
import random
for i in range(10):
    lista.append(random.randint(1,1000))

def suma(liczba):
    s=0
    for cyfra in str(liczba):
        s=s+int(cyfra)
    return s
print("lista",lista)
print("max",max(lista))
print("min",min(lista))
for liczba in lista:
    if suma(liczba) == 11:
        print("suma11",liczba)