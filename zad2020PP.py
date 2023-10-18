def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma = suma+ int(cyfra)
    return suma

def czy_liczba_pierwsza(liczba):
    for i in range(2,liczba):
        if liczba % i ==0:
            return False
    return True

with open("liczby.txt") as dane:
    ile_liczb =0
    for wiersz in dane:
        liczba = int(wiersz)
        if liczba %2 ==1:
            #print(liczba)
            ile_liczb +=1
        if suma_cyfr(str(liczba)) == 11:
            print("suma 11",liczba)
        if liczba>4000 and liczba<5000 and czy_liczba_pierwsza(liczba):
            print("pierwsza",liczba)


    print("Liczb nieparzystych jest "+str(ile_liczb))
