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
wszystkie_liczby =[]
with open("liczby.txt") as dane:
    for wiersz in dane:
        #print(wiersz)
        liczba= int(wiersz)
        wszystkie_liczby.append(liczba)
        if liczba in potegi:
            #print("potega",liczba)
            licznik += 1


        if liczba == suma_silnia(liczba):
            print(liczba)
print("zad a",licznik)
print(suma_silnia.__doc__)

print(wszystkie_liczby)
def nwd (a,b):
    """
    odejmowanie -> przy 0 pętla nieskończona
    :param a:
    :param b:
    :return:
    """
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def nwd_lepiej(a,b):
    while b!=0:
        a,b   = b,a%b #operacje na danych spakowanych
        """
        reszta = a%b
        a =b 
        b = pomoc
        """
    return a

print(nwd_lepiej(0,65))

ciag_liczb = [0]

nwd_wartosc = nwd(wszystkie_liczby[0],wszystkie_liczby[1])
for i in range(2,len(ciag_liczb)):
    if nwd_wartosc>1:
        ciag_liczb.append(ciag_liczb[-1]+1)
        nwd_wartosc = nwd(nwd_wartosc,wszystkie_liczby[i])
    else:
        ciag_liczb.append(0)
        nwd_wartosc = nwd(wszystkie_liczby[i-1],wszystkie_liczby[i])
print(max(ciag_liczb))