potegi = []

p=1
for i in range(10):
    potegi.append(p)
    p=p*3

silnie=[]
s=1
for i in range(1,11):
    silnie.append(s)
    s=s*i
print(silnie)

def suma_silnia(liczba):
    """
    funkcja zwraca sumę silnii cyfr z liczby
    :param liczba: liczba całkowita dodatnia
    :return: suma silnii cyfr
    """
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        liczba = liczba // 10
        suma = suma + silnie[cyfra]
    return suma
licznik=0
with open("liczby.txt") as dane:
    for wiersz in dane:
        #print(wiersz)
        liczba= int(wiersz)
        if liczba in potegi:
            #print("potega",liczba)
            licznik += 1


        if liczba == suma_silnia(liczba):
            print(liczba)
print("zad a",licznik)
print(suma_silnia.__doc__)