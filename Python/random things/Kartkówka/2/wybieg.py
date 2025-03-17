n = int(input())
linia1 = []
linia2 = []
linia3 = []
for i in range(n+2):
    linia1.append("#")

print(*linia1)
for j in range(n+2):
    if j == 0 or j == n+1:
        linia2.append("#")
    else:
        linia2.append("@")
print(*linia2)
for k in range(n+2):
    linia3.append("#")
print(*linia3)