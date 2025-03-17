tab = input().split()
tabWyrazien = []
licznik = 0
for i in range(int(tab[0])):
    b = input()
    tabWyrazien.append(b)
for j in tabWyrazien:
    if len(j) > int(tab[1]):
        licznik += 1
print(licznik)