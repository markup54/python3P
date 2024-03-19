lista_poteg =[]
potega =1
for i in range(15):
    lista_poteg.append(potega)
    potega = potega *3
print("#1 sposób")
with open ("liczby.txt") as dane:
    for wiersz in dane:
        liczba = int(wiersz)
        if liczba in lista_poteg:
            print(liczba)
print("2 sposób")
with open ("liczby.txt") as dane:
    for wiersz in dane:
        liczba = int(wiersz)
        pomoc = liczba
        while liczba%3 ==0:
            liczba = liczba//3
        if liczba == 1:
            print(pomoc)

lista_silni_cyfr = [1]
silnia = 1
for i in range(1,10):
    #5 ! = 1*2*3*4*5
    silnia =silnia*i
    lista_silni_cyfr.append(silnia)
print(lista_silni_cyfr)

print("zadanie 4.2")
with open ("liczby.txt") as dane:
    for wiersz in dane:
        #suma silni cyfr == liczba
        liczba = int(wiersz)
        suma =0
        pomoc = liczba
        while liczba > 0:
            cyfra = liczba%10
            suma = suma +lista_silni_cyfr[cyfra]
            liczba = liczba//10
        if pomoc==suma:
            print(pomoc)

print("zadanie 4.3")

def nwd(a,b):
    while a !=b:
        if a>b :
            a=a-b
        else:
            b= b-a
    return a

liczby_wczytane_z_pliku = []
with open ("liczby.txt") as dane:
    for wiersz in dane:
        liczby_wczytane_z_pliku.append(int(wiersz))
