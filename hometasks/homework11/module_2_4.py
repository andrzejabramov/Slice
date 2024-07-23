numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2]
not_primes = []


for element in numbers:
    res = False
    if element != 1 and element != 2:
        for el in range(2, element):
            if element % el == 0:
                res = True
                break
        primes.append(element) if res is False else not_primes.append(element)

print(f"простые числа: {primes}")
print(f"составные числа: {not_primes}")