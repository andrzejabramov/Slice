class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed


class Plant:
    def __int__(self, name, edible=False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    def __init__(self, name, alive, fed):
        super().__init__(name, alive, fed)


    def eat(self, food):
          pass


class Predator(Animal)
        def __init__(self, name, alive, fed):
            super().__init__(name, alive, fed)

        def eat(self, food):
            pass


class Flower(Plant):
    self.name = name
    self.edible = edible

class Fruit(Plant):
    pass

