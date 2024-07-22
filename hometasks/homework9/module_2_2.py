while True:
    try:
        first = int(input('Введите первое число: '))
        print(first)
        second = int(input('Введите второе число: '))
        print(second)
        third = int(input('Введите третье число: '))
        print(third)
        if first == second == third:
            res = 3
        elif first == second != third or first != second == third or first == third != second:
            res = 2
        else:
            res = 0
        print(f"Совпадающих значений: {res}")
        break
    except Exception:
        print('Вы ввели не число')
