class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, engin_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engin_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        return f"{self.get_model()}\n{self.get_horsepower()}\n" \
               f"{self.get_color()}\nИмя: {self.owner}"

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
            return self.__color
        return f"Нельзя сменить цвет на {new_color}"


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner, model, engin_power, color):
        super().__init__(owner, model, engin_power, color)


s = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
print(s.print_info())
s.set_color('Pink')
s.set_color('BLACK')
s.owner = 'Vasyok'
print(f'\n{s.print_info()}')