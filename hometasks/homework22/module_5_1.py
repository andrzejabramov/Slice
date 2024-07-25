class House:
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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

print(h1.go_to(5))
print(h2.go_to(10))