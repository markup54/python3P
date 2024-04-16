import random
liczby = [random.randint(1,100) for i in range(30)]
#lista z 30 liczbami z zakresu 1,100

#liczby2 z klawiatury
liczby2=[]
for i in range(30):
    liczby2.append(random.randint(1,100))

print( random.randint.__doc__) #dokumentacja randint

ciagi = [1]

print(liczby)
for i in range(1,len(liczby)):
    if liczby[i]>liczby[i-1]:
        ciagi.append(ciagi[-1]+1)
    else:
        ciagi.append(1)
print(ciagi)
dl = max(ciagi)
print("najdłuższy ciąg ma dł "+str(dl))


ile_ciagow_naj = ciagi.count(dl)
for i in range(ile_ciagow_naj):
    indeks_konca = ciagi.index(dl)
    print(liczby[indeks_konca-dl+1:indeks_konca+1])
    ciagi = ciagi [indeks_konca+2:]
    liczby = liczby [indeks_konca+2:]


#najdluzszyciag liczb parzystych w liscie liczby2

ciagi =[0]
for element in liczby2:
    if element%2 == 0:
        ciagi.append(ciagi[-1]+1)
    else:
        ciagi.append(0)
ciagi.remove(0)
print(liczby2)
dl = max(ciagi)
print("najdłuższy ciąg ma dł "+str(dl))


ile_ciagow_naj = ciagi.count(dl)
for i in range(ile_ciagow_naj):
    indeks_konca = ciagi.index(dl)
    print(liczby2[indeks_konca-dl+1:indeks_konca+1])
    ciagi = ciagi [indeks_konca+2:]
    liczby2 = liczby2[indeks_konca+2:]


