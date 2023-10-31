def nwd(a,b):
    while b!=0:
        #a,b = b, a%b operacje na danych spakowany
        r = a%b
        a = b
        b = r
    return a

with open("liczby.txt") as dane:
    for wiersz in dane:
        liczby=wiersz.split()
        liczby_int=[]
        for liczba in liczby:
            liczby_int.append(int(liczba))
        #liczby =[int(x) for x in liczby]
        #print(liczby)
        #print(liczby_int)
        liczby_do_sort=liczby_int.copy()
        liczby_do_sort.sort()

        if liczby_do_sort == liczby_int:
            print(wiersz)
            print(liczby_int)
            print(liczby_do_sort)
        if liczby_int[0]<=liczby_int[1] and liczby_int[1]<=liczby_int[2]:
            print(wiersz)
        nwd_3 = nwd(nwd(liczby_int[0],liczby_int[1]),liczby_int[2])
        print(liczby_int,nwd_3)