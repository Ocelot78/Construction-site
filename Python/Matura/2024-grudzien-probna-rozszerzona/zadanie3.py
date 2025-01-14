from math import sqrt
with open("liczby_przyklad.txt","r") as file:
    data = file.read().split()
def isPrime(a):
    for j in range(2,int(a/2)+1):
        if a % j == 0:
            return False
    return True
found = False
counter = 0
with open("wyniki3.txt","w") as result:
    result.write("Zadanie 3\n")
    for i in data:
        prime_counter = 0
        i = int(i)
        if sqrt(i) == int(sqrt(i)):
            counter += 1
            if found == False:
                result.write(f"Odpowiedza jest liczba {i}")
                found = True
                
        for k in range(2,int(i/2)+1):
            if isPrime(k):
                if i % k == 0:
                    prime_counter += 1
                    if prime_counter == 5:
                        result.write(f"\n{i}")
        i = str(i)
        minNumber = ''.join(sorted(i))
        maxNumber = minNumber[::-1]
        maxNumber = int(maxNumber)
        minNumber = int(minNumber)
        i = int(i)
        sub = maxNumber - minNumber
        diff = i /sub
        if diff == 0:
            print(f"Liczba {i} roznica {sub} jest rowna liczbie {i}")
        elif int(diff) >0:
            print(f"roznica {sub} jest mniejsza o {int(diff)} razy od {i}")
    result.write(f"\nIstnieje takich liczb: {counter}")
    