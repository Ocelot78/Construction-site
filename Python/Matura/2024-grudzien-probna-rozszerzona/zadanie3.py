from math import sqrt

def process_number(number):
    digits = sorted(str(number))
    max_number = int(''.join(digits[::-1]))
    min_number = int(''.join(digits))
    return max_number - min_number

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def process_numbers():
    less, greater, equal = 0, 0, 0
    equals_list = []
    perfect_squares = []
    results = []

    with open('liczby.txt') as f:
        for line in f:
            num = int(line.strip())
            diff = process_number(num)

            if diff < num:
                less += 1
            elif diff > num:
                greater += 1
            else:
                equal += 1
                equals_list.append(num)

            if sqrt(num).is_integer():
                perfect_squares.append(num)

            divisor_count = 0
            for k in range(2, num // 2 + 1):
                if num % k == 0 and is_prime(k):
                    divisor_count += 1
                    if divisor_count >= 5:
                        results.append(num)
                        break

    with open("wyniki3.txt", "w") as out:
        out.write("Zadanie 3\n")
        if perfect_squares:
            out.write(f"Odpowiedz to liczba {perfect_squares[0]}\n")
        out.write(f"Liczb takich jest: {len(perfect_squares)}\n")
        for result in results:
            out.write(f"\n{result}")

    with open("zadanie3.txt", "w") as out:
        out.write(f'Liczba roznic mniejszych od liczby: {less}\n')
        out.write(f'Liczba roznic wiekszych od liczby: {greater}\n')
        out.write(f'Liczba roznic rownych liczbie: {equal}\n')
        out.write('Liczby, dla ktorych roznica jest rowna liczbie:\n')
        for number in equals_list:
            out.write(f'{number}\n')

process_numbers()
