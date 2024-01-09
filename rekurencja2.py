def silnia_i(n):
    wynik =1
    for i in range(1,n+1):
        wynik = wynik*i
    return wynik

def silnia_r(n):
    if n==0:
        return 1
    else:
        return silnia_r(n-1)*n

def nwd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def nwd_r(a,b)
    if b==0:
        return a
    else:
        return nwd_r(b,a%b)

print(nwd(20,75))

print("silnia i",silnia_i(100))
print("silnia r",silnia_r(100))