parzyste =[]

def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma = suma +int(cyfra)
    return suma

def suma_cyfr2(liczba):
    suma =0
    while liczba>0:
        cyfra = liczba % 10
        suma = suma + cyfra
        liczba = liczba // 10 #dzielenie całkowite
    return suma


with open ("liczby.txt") as dane:
    for wiersz in dane:
        liczba = int(wiersz)
        if liczba%2 == 0:
            #print(liczba)
            parzyste.append(liczba)
        wiersz = wiersz.strip()
        if wiersz == wiersz[::-1]:
            print("palindrom: ",wiersz)
        if suma_cyfr(wiersz)>30:
            print("suma >30",wiersz)
        if suma_cyfr2(liczba)>30:
            print("suma >30", wiersz)
print("największa parzysta ",max(parzyste))
