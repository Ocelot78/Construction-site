r = int(input())
if (r % 4 == 0 and r % 100 != 0) or r % 400 == 0:
    print("TAK")
else:
    print("NIE")