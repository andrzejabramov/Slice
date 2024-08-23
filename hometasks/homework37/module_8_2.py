from collections.abc import Iterable

def personal_sum(numbers):
    incorrect_data = result = 0
    if isinstance(numbers, Iterable):
        for el in numbers:
            try:
                result = result + el
            except TypeError:
                print(f"Некорректный тип данных для подсчёта суммы - {el}")
                incorrect_data += 1
            continue
    else:
        print('В numbers записан некорректный тип данных')
        return None
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        devide = personal_sum(numbers)
        devidend = devide[0]
        devider = (len(numbers) - devide[1])
        calc = devidend / devider
        return calc
    except ZeroDivisionError:
        return 0
    except TypeError:
        return devide


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
