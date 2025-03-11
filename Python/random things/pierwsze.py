from math import sqrt
tab = input().split()
tabWyn = []
def jest_pierwsza(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for j in range(int(tab[0]),int(tab[1])+1):
    if jest_pierwsza(j):
        tabWyn.append(j)
if len(tabWyn) == 0:
    print("BRAK")
else:
    print(*tabWyn)