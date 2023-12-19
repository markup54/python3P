licznikliter =[0 for x in range(13)]
slowa =[]
with open("slowa.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        slowa.append(wiersz)
        print(wiersz,len(wiersz))
        licznikliter[len(wiersz)]+=1
print(licznikliter)
nowe =[]
with open("nowe.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        nowe.append(wiersz)

for slowko in nowe:
    print(slowko,slowa.count(slowko))