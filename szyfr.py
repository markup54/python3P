def szyfruj_cezar(slowo,klucz):
    """
    Metoda szyfruje sztfrem podstawieniowym
    :param slowo: tekst złożony z małych liter
    :param klucz: klucz o który przesuwamy litery
    :return: zaszyfrowane słowo
    """
    szyfr =""
    klucz = klucz %26
    for litera in slowo:
        print(litera,ord(litera)) #ord - zwraca kod znaku
        kod = ord(litera)+klucz
        if kod > ord("z"):
            kod = kod - 26
        print(chr(kod)) #chr - znak zapisany pod danym kodem
        szyfr = szyfr+chr(kod)
    return szyfr
def szyfruj_cezar_2(slowo,klucz):
    szyfr =""

    alfabet = "abcdefghijklmnopqrstuvwxyz"
    klucz = klucz % len(alfabet)
    alfabet_przesuniety = alfabet[klucz:]+alfabet[:klucz]
    for litera in slowo:
        indeks = alfabet.index(litera)
        litera_zaszyfrowana = alfabet_przesuniety[indeks]
        szyfr = szyfr+litera_zaszyfrowana
    return szyfr
print(szyfruj_cezar("xyz",3))
print(szyfruj_cezar("abc",-3))
print(szyfruj_cezar.__doc__)
print(szyfruj_cezar_2("xyz",3))
print(szyfruj_cezar_2("abc",-3))