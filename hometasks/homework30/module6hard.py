"""
Создем общий родительский класс фигур с атрибутами стороны, цвет и заливка
"""
class Figure:
    sides_count = 0
    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color
    """
    Валидируем вводимые значения цвета в формате RGB. Сначала проверяем чтобы значения были в пределах от 0 до 255 включительно.
    Если это условие выполнено, то продолжаем проверку формата данных (все должны быть int). Метод возвращает либо None либо введенные параметры
    """
    def __is_valid_color(self, color):
        valid = color if min(color) >= 0 and max(color) <= 255 else None
        if valid:
            for i in valid:
                if type(i) != int:
                    valid = None
                    break
        return valid
    """
    Метод устанавливает новые данные цвета, если они валидированы приватным методом __is_valid_color
    либо уведомляет, что введенные данные не удовлетворяют требованиям задания и оставляет цвет прежним  
    """
    def set_color(self, color):
        note = "Введены неверные значения, цвет остался прежним"
        if self.__is_valid_color(color):
            self.__color = color
            return self.__color
        print(note)
        return self.__color
    """
    Метод валидирует ввод списка сторон фигуры. Проверка по типу данных (в качестве альтернативы можно использовать isinstance()),
    каждый элемент должен быть положительным числом и число аргументов равняться статическомк атрибуту sides_count.
    На втором этапе проверки для фигур с количеством сторон более 2-х (треугольник и выше) проверяется размеры сторон на условие
    чтобы любая сторона была меньше сумме остальных сторон 
    """
    def __is_valid_sides(self, args):
        for i in args:
            if type(i) == int and i > 0 and len(args) == self.sides_count:
                if len(args) > 2:
                    ans = True if (sum(args) - i) > i else False
                    return ans
                return True
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        note = 'Количество вводимых сторон или их размеры не соответсвует фигуре.'
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
            return self.__sides
        return note

"""
Создаем дочерний класс Окружность. Для усложнения задачи сначала из длины окружности вычисляем радиус, затем по радиусу площадь 
"""
class Circle(Figure):
    sides_count = 1
    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.__radius = self.get_sides() / 2 / 3.14

    def get_squqre(self):
        return 3.14 * self.__radius ** 2

"""
Дочерний класс Треугольник. Для усложнения задания по трем сторонам треугольника по формуле Герона вычисляем площадь, 
на основании ее и, определив основанием последний элемент списка сторон, расчитываем высоту, а уже по высоте и основанию - площадь 
"""
class Triangle(Figure):
    sides_count = 3
    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        p = sum(self.get_sides()) / 2
        q = 1
        for s in self.get_sides():
            q = q * (p - s)
        q = (q * p) ** 0.5
        #q = (p * (p - a) * (p - b) * (p - c)) ** 0.5 - формула Герона, где p - полупериметр
        self.__height = q * 2 / self.get_sides()[2]

    def get_square(self):
        return self.__height * self.get_sides()[2] / 2
"""
Создаем класс Cube, переопределяем атрибут sides (у куба все стороны равны и можно обойтись одним параметром), вычисляем площадь
"""
class Cube(Figure):
    sides_count = 12
    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3

"""
Блок исполнительного кода с пояснениями процесса
"""
print('Создаем экз класса Окружность\n')
c = Circle(314, [0, 0, 0], True)
print(f"Проверяем переданный цвет при вызове класса:\n{c.get_color()}\n")
print('Вводим значения цвета, имеющие атрибут за пределами верхней цветовой границы 255:')
c.set_color([3, 87, 280])
print(c.get_color())
print('\nВводим значения цвета, имеющие атрибут за пределами нижней цветовой границы 0:')
c.set_color([-5, 0, 0])
print(c.get_color())
print('\nВводим значения цвета, имеющие атрибут не int:')
c.set_color([1.5, 36.9, 200])
print(c.get_color())
print('\nВводим значения цвета, удовлетворяющие условиям задачи:')
c.set_color([200, 100, 50])
print(c.get_color())
print(f"\nПроверяем переданный атрибут заливка:\n{c.filled}\n")
print(f"Проверяем атрибут количество сторон:\n{c.sides_count}\n")
print(f"Проверяем переданный аргумент sides:\n{c.get_sides()}\n")
print(f"Пробуем изменить артумент sides разными способами:\n1. Устанавливаем значение меньше нуля: \n{c.set_sides(-17)}\n")
print(f"2. Вводим значение не int:\n{c.set_sides(5.0)}\n")
print(f"3. Задаем значения сторон более чем одна:\n{c.set_sides([10, 20])}\n")
print(f"4. Задаем значение, удовлетворяющее условия задания:\n{c.set_sides(314)}\n")
print(f"Распечатываем длину окружности:\n{c.__len__()}\n")
print(f"Вычисляем площадь окружности через вычисление радиуса и сохранение его в приватном атрибуте:\n{c.get_squqre()}\n")
print('Создаем экз класса Треугольник\nПроверять работоспособность атрибутов и методов, связанных с цветом и заливкой не будем: они аналогичны как у Окружности\n')
t = Triangle([24, 26, 30], [0, 120, 45], True)
print(f"Проверяем атрибут количество сторон:\n{t.sides_count}\n")
print(f"Проверяем переданный аргумент sides:\n{t.get_sides()}\n")
print('Проверять валидацию вводимых параметров сторон мы будем дополнительно к проверенным на окружности, а именно: ' \
      'у всех фигур, имеющих более двух сторон длина любой стороны должна быть меньше суммы остальных сторон\n')
print(t.set_sides([30, 15, 10]))
print(f"Значения остались прежними:\n{t.get_sides()}\n")
print(f"Вычисляем площадь Треугольника через высоту и основание (за основание выбираем последний элемент списка сторон)\n" \
      f"Для этого в методе __init__ вычисляем высоту треугольника через его площадь, определенную по формуле Герона. Площадь Треугольника:\n{t.get_square()}\n")
print('Создаем экз класса Cube и расчитаем только его объем, так как остальные родителькие атрибуты и методы мы проверили на предыдущих фигурах')
cb = Cube(5, [0, 0, 0], False)
print(f"Площадь куба равна:\n{cb.get_volume()}")
