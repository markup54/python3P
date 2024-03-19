plik1 = open("wyniki_4_1.txt","w")

with open ("slowa.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        if wiersz.count("w") == wiersz.count("k"):
            plik1.write(wiersz+"\n")

plik1.close()