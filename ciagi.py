import random
wylosowane = [random.randint(1,100) for i in range(20)]
print(wylosowane)
if wylosowane[0]%2 == 0:
    ciagi = [1]
else:
    ciagi = [0]

for i in range(1,len(wylosowane)):
    if wylosowane[i]%2 ==0 :
        ciagi.append(ciagi[-1]+1)
    else:
        ciagi.append(0)

dlugosc = max(ciagi)
print(ciagi)
print("dlugosc najdluzszego ciagu",dlugosc)
print("ile takich ciagow",ciagi.count(dlugosc))

def nwd(a,b):
    while b!=0:
        a,b =b,a%b
    return b