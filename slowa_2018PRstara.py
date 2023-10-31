#https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2020/formula_do_2014/informatyka/MIN-R2_1P-202s.pdf
with open("slowa.txt") as dane:
    ile_na_a = 0
    ile_zawiera=0
    ile_anagramy=0
    for wiersz in dane:
        slowa = wiersz.split() # split() wstawia tekst do listy domyślnie rozdzielony spacją
        """
        print(slowa)
        print("pierwsze ",slowa[0])
        print("drugie ",slowa[1])
        """
        if slowa[0][-1] == "A":
            ile_na_a+=1
            print(slowa[0])
        if slowa[1][-1] == "A":
            ile_na_a+=1
        if slowa[0] in slowa[1]:
            print("zawiera",slowa)
            ile_zawiera+=1
        litery1 = list(slowa[0])
        litery2 = list(slowa[1])
        litery1.sort()
        litery2.sort()
        if litery1 == litery2:
            print("anagramy ",slowa)
            ile_anagramy+=1
print("slów kończących się na a jest ",ile_na_a)
print("liczba wierszy w których pierwsze slowo zawiera się w drugim",ile_zawiera)
print("liczba anagramów",ile_anagramy)