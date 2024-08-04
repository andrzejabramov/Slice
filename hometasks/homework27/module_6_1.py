class Animal:
    alive = True #статический параметр живой
    fed = False #статический параметр сытый
    def __init__(self, name): #инициализируем динамический параметр имя
        self.name = name


    def eat(self, food): #задаем метод родительского класса
        e = food.edible #присваиванем переменной параметр входного дочернего класса
        if e: #если переменная True (можно не указывать == True)
            self.fed = True # животное сытое
            return f"{self.name} съел {food.name}"
        self.alive = False # иначе (если переменная False) животное погибает
        return f"{self.name} не стал есть {food.name}"


class Plant:
    edible = False # устанавливаем статический параметр по условию задания
    def __init__(self, name): # инициализируем динамический параметр имя растения
        self.name = name


class Mammal(Animal): # по услвиям задания устанавливать параметры и методы дочернего класса нет необходимости
    pass


class Predator(Animal): # по услвиям задания устанавливать параметры и методы дочернего класса нет необходимости
    pass


class Flower(Plant): # по услвиям задания устанавливать параметры и методы дочернего класса нет необходимости
    pass


class Fruit(Plant): # переопределяем параметр родительского класа
    edible = True


"""
Задаем экземпляры дочерних классов
"""
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
"""
проверяем в консоли парамеры созданных экземпляров
"""
print(f'name = {a1.name}, alive = {a1.alive}, fed = {a1.fed}')
print(f'name = {a2.name}, alive = {a2.alive}, fed = {a2.fed}')
print(f"name = {p1.name}, edible = {p1.edible}")
print(f"name = {p2.name}, edible = {p2.edible}")
"""
проверяем работу программы в соответствии с заданием
"""
print(a2.eat(p2))
print(f"Теперь {a2.name} жиаой? {a2.alive} и сытый?: {a2.fed}")
print(a1.eat(p1))
print(f"Теперь {a1.name} живой? {a1.alive}")