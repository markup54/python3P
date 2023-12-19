def szyfruj(slowo,klucz):
    szyfr =""
    klucz = klucz % 26

    for litera in slowo:
        #print(litera, ord(litera))
        kod =ord(litera)+klucz
        #print(chr(kod))
        if kod >ord('z'):
            kod = kod -26
        zaszyfrowana_litera = chr(kod)
        szyfr = szyfr+zaszyfrowana_litera
    return szyfr

def szyfruj2(slowo,klucz):
    szyfr = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    klucz = klucz % len(alfabet)
    alfabet_zaszyfrowany = alfabet[klucz:]+alfabet[:klucz]
    for literka in slowo:
        indeks = alfabet.index(literka)
        szyfr = szyfr +alfabet_zaszyfrowany[indeks]
    return szyfr


print(szyfruj2("programista",3))
print(szyfruj2("abc",3))
print(szyfruj2("def",-3))

print(szyfruj2("abc",102))
print(szyfruj2("xyz",3))

plik2=open("wyniki_6_2.txt","w")
with open ("dane_6_2.txt") as dane:
    for wiersz in dane:
        lista = wiersz.split()
        klucz =int(lista[1])
        slowo = lista[0]
        print(slowo,klucz)
        szyfr = szyfruj2(slowo,klucz)
        plik2.write(szyfr+"/n")
plik2.close()

for i in range(10):
    print(i)
