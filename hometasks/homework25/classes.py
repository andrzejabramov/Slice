class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        note = 'Такого этажа не существует'
        if new_floor > 0 and new_floor < self.number_of_floors:
            for fl in range(1, new_floor+1):
                print(fl)
            return ''
        else:
            return note

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        return other if isinstance(other, int) else other.number_of_floors

    def __eq__(self, other):
            fl = self.__verify_data(other)
            return self.number_of_floors == fl

    def __lt__(self, other):
        fl = self.__verify_data(other)
        return self.number_of_floors < fl

    def __le__(self, other):
        fl = self.__verify_data(other)
        return self.number_of_floors <= fl

    def __gt__(self, other):
        fl = self.__verify_data(other)
        return self.number_of_floors > fl

    def __ge__(self, other):
        fl = self.__verify_data(other)
        return self.number_of_floors >= fl

    def __ne__(self, other):
        fl = self.__verify_data(other)
        return self.number_of_floors != fl

    def __add__(self, other):
        fl = self.__verify_data(other)
        return House(self.name, self.number_of_floors + fl)

    def __radd__(self, other):
        fl = self.__verify_data(other)
        return House(self.name, self.number_of_floors + fl)

    def __iadd__(self, other):
        fl = self.__verify_data(other)
        return House(self.name, self.number_of_floors + fl)
