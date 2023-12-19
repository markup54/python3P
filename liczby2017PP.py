def nwd(a,b):
    while b!=0:
        a,b =b,a%b
        """
        pomoc =a
        a=b
        b=pomoc%b
        
    while a!=b :
        #a,b rozne od zera
        if a>b :
            a=a-b
        else:
            b=b-a
            """
    return a

def suma_cyfr(liczba):
    suma =0
    for cyfra in liczba :
        suma=suma+int(cyfra)
    return suma


licznik =0
suma_nwd =0
sumy=[]
with open ("liczby.txt") as dane:
    for wiersz in dane:
        #print(wiersz)
        liczby_tekstowo = wiersz.split()
        s=0
        for liczba_tekst in liczby_tekstowo:
            s= s+suma_cyfr(liczba_tekst)
        sumy.append(s)
        liczby = [int(x) for x in liczby_tekstowo]
        print(liczby)
        liczby2=liczby.copy()
        liczby2.sort()
        suma_nwd = suma_nwd + nwd(nwd(liczby[0],liczby[1]),liczby[2])
        if liczby == liczby2:
            print("uporządkowane",liczby, wiersz)
            licznik = licznik+1
print("licznik ",licznik)
print("suma nwd",suma_nwd)
print(sumy.count(35))
print(max(sumy))
print(sumy.count(max(sumy)))
