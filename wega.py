#https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2018/formula_od_2015/informatyka/MIN-R2_1P-182.pdf
slowa = []
with open("przyklad.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        slowa.append(wiersz)

przeslanie =""
for i in range(39,len(slowa),40):
    przeslanie = przeslanie+slowa[i][9]
print(przeslanie)
maks_slowo=""
maks_litery=0
for slowko in slowa:
    litery_bez_powtorzen = set(slowko)
    #print(len(litery_bez_powtorzen),slowko)
    if len(litery_bez_powtorzen)>maks_litery:
        maks_litery = len(litery_bez_powtorzen)
        maks_slowo = slowko
print(maks_litery,maks_slowo)

for slowko in slowa:
    literki = list(slowko)
    if ord(max(literki)) - ord(min(literki)) <=10:
        #ord kod ascii z literki
        print(slowko)

