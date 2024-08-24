class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin_number)
        self.__numbers = self.__is_valid_numbers(numbers)
    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) is False:
            return IncorrectVinNumber('type')
        elif vin_number < 1000000 or vin_number > 9999999:
            return IncorrectVinNumber('count')
        return True
    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) is False:
            return IncorrectCarNumbers('type')
        elif len(numbers) != 6:
            return IncorrectCarNumbers('len')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        if message == 'type':
            raise TypeError('Некорректный тип vin номер')
        elif message == 'count':
            raise TypeError('Неверный диапазон для vin номера')
        super().__init__(message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        if message == 'type':
            raise TypeError('Некорректный тип данных для номеров')
        elif message == 'len':
            raise TypeError('Неверная длина номера')
        super().__init__(message)


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')