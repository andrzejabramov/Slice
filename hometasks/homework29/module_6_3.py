class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        x_distance = super().run(dx)
        y_distance = super().fly(dy)
        return x_distance, y_distance

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        return Eagle.sound

p = Pegasus()
print(p.get_pos())
print(p.move(10, 15))
print(p.get_pos())
p.move(-5, 20)
print(p.get_pos())
print(p.voice())
