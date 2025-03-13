tab = input().split()

tabRoz = []
pierwszaLiczba = int(tab[0])
for i in tab:
    roznica = pierwszaLiczba - int(i) 
    if roznica < 0:
        print(i)
        print("Roznica: ",roznica)
        tabRoz.append(roznica)
roznicaMniejsza = max(tabRoz)
for j in range(len(tab)):
    if pierwszaLiczba - roznicaMniejsza == int(tab[j]):
        print("test")
        tab.remove(str(pierwszaLiczba))
        tab.insert(j-1,str(pierwszaLiczba))
        break
print(*tab)
        

