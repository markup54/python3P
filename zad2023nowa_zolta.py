plik_wyniki = open("wyniki4_1.txt","w") #w zapisujemy, jak pliku nie ma to go tworzymy
#jeżeli jest coś w pliku to wszystko nadpisujemy
#a jeżeli coś jest to dopisujemy na koncu
literki = "wakcje"
plik_wyniki2 = open("wynik4_2.txt","w")

with open("slowa.txt","r") as dane:
    # domyslnie r czyli plik do odczytu
    for wiersz in dane:
        wiersz = wiersz.strip()
        if wiersz.count("w") == wiersz.count("k"):
            plik_wyniki.write(wiersz+"\n")
        ile_wystapien = []
        for literka in literki:

            ile_wystapien.append(wiersz.count(literka))
        minimum = min(ile_wystapien)
        if minimum >= wiersz.count("a"):
            plik_wyniki2.write(str(minimum)+"\n")
        else:
            plik_wyniki2.write(str(wiersz.count("a")//2)+"\n")

plik_wyniki.close()
plik_wyniki2.close()