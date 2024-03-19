licznik=0
with open("slowa.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        liczba_zer = wiersz.count("0")
        liczba_jedynek = wiersz.count("1")
        if liczba_zer>liczba_jedynek:
            licznik +=1;
print(licznik)

#zad 2
licznik=0
potegi= [2**x for x in range (1,30)]
print(potegi)
with open("slowa.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        if wiersz[0] != '0':
            continue
        liczba = int(wiersz,2)+1
        if liczba in potegi:
            print(wiersz)
            licznik = licznik +1

print(licznik)

#zad2 inny sosób
licznik=0
with open("slowa.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        if "01" in wiersz:
            if "10" not in wiersz:
                licznik = licznik+1
print(licznik)

#zad3
licznik=0
slowo= "0"
with open("slowa.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        while slowo in wiersz:
            slowo = slowo+"0"
        #slowo = slowo [:-1]
        print(slowo)
print(licznik)