def is_prime(func):
    def wrapper(*args):
        for y in range(2, func(*args)):
            if func(*args) % y == 0:
                return 'Составное\n' + str(func(*args))
                break
        return 'Простое\n' + str(func(*args))
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
