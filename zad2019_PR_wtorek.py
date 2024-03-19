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

print("zadanie 4.2")
with open ("przyklad.txt") as dane:
    for wiersz in dane:
        liczba = int(wiersz)