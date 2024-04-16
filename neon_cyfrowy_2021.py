instrukcje =[]
ciagi =[1]
with open("przyklad.txt") as dane:
    przeslanie = ""
    for wiersz in dane:
        wiersz = wiersz.strip()
        print(wiersz)
        instrukcje.append(wiersz[:-2])
        if wiersz.count("DOPISZ")>0:
            przeslanie = przeslanie+wiersz[-1]
            print(przeslanie)
        if wiersz.count("USUN"):
            przeslanie = przeslanie[:-1]
print(przeslanie)
print(len(przeslanie))
print(instrukcje)
for i in range(1,len(instrukcje)):
    if instrukcje[i-1] == instrukcje[i]:
        ciagi.append(ciagi[-1]+1)
    else:
        ciagi.append(1)
print(max(ciagi))
print(instrukcje[ciagi.index(max(ciagi))])