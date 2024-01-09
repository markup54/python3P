caly_ekran=[]
ile_do_usuniecia = 0
with open("dane.txt") as dane:
    for wiersz in dane:
        piksele_w_wierszu = wiersz.split()
        piksele_w_wierszu = [int(x) for x in piksele_w_wierszu]
        if piksele_w_wierszu != piksele_w_wierszu[::-1]:
            ile_do_usuniecia+=1
        print(piksele_w_wierszu)
        #caly_ekran.extend(piksele_w_wierszu)
        caly_ekran.append(piksele_w_wierszu)
        print(len(piksele_w_wierszu))

#print(max(caly_ekran))
#print(min(caly_ekran))
print(ile_do_usuniecia)
print(len(caly_ekran))
for nr_wiersz in range(200):
    for nr_kolumny in  range(320):
        if abs(caly_ekran[nr_wiersz][nr_kolumny] - caly_ekran[nr_wiersz+1][nr_kolumny])>128:
            pass
        
