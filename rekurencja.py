"""
iteracja
for while
itaracja to jedno przejście pętli
rekurencja tylko if

silnia(5)  = 1*2*3*4*5
silnia(5) = silnia(4)*5 jeżeli n>1
silnia(n) = silnia(n-1)*n
silnia(1) = 1
silnia(0) =1
reklurencja to funkcja która wywołuje samą siebie
"""

def silnia_i(n):
    s=1
    for i in range(2,n+1):
        s = s * i
    return s
"""
silnia_i(5)
s=1
i=2 s = 2
i=3 s = 6
i=4 s = 24
i=5 s = 120
"""
print(silnia_i(5))

def silnia_r(n):
    if n<2:
        return 1
    else:
        return silnia_r(n-1)*n
"""
silnia_r(5) = silnia_r(4)*5 ->na stos
silnia_r(4) = silnia_r(3)*4 ->na stos
silnia_r(3) = silnia_r(2)*3 ->na stos
silnia_r(2) = silnia_r(1)*2 ->na stos
silnia_r(1) =1
silnia_r(2) = 1 *2 <- z stosu
silnia_r(3) = 2 *3 itd
"""

print("iteracja",silnia_i(500))
print("rekurencja",silnia_r(500))


"""
ciąg fibonacciego
f(n) =  f (n-1) + f(n-2) sumujemy dwa wyrazy poprzednie
f(0) =0 
f(1) =1
"""
def fib_r(n):
    if n<2:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)

print(fib_r(15))

def fib_i(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        c = a+b
        a = b
        b = c
    return c
print(fib_i(15))

def pot_r(n):
    if n == 0:
        return 1
    else:
        return pot_r(n-1)*2

print(pot_r(5))

#nwd iteracyjnie i rekurencyjnie
def nwd_i(a,b):
    while b!=0:
        a,b = b,a%b
    return a

print("nwd",nwd_i(25,70))


def nwd_r(a,b):
    if b==0:
        return a
    else:
        return nwd_r(b,a%b)

print("nwd",nwd_r(25,70))


#konwersjapomiędzy systemami iteracyjnie i rekurencyjnie

def na_dziesietne(liczba_tekstowo,system):
    wynik =0
    potega =1
    for cyferka in liczba_tekstowo[::-1]:
        wynik = wynik + int(cyferka,system)*potega
        potega = potega*system

    return wynik

print(na_dziesietne("1100",2))
print(na_dziesietne("23",8))
print(na_dziesietne("A2",16))

def z_dziesietnego(liczba,system):
    wynik = ""
    while liczba>0:
        cyfra = liczba%system
        wynik = str(cyfra) +wynik
        liczba = liczba//system
    return wynik
print(z_dziesietnego(12,2))