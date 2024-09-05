from threading import Thread
from time import sleep
from datetime import datetime


class Knight(Thread):
    enemies = 100
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!\n')
        for d in range(1, self.enemies + 1):
            self.enemies -= self.power
            if self.enemies > 0:
                print(f'{self.name}, сражается {d} день (дней, дня)..., осталось {self.enemies} воинов\n')
            else:
                print(f'{self.name} одержал победу спустя {d} день (дней, дня)!\n')
                break
            sleep(1.0)
        return None



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')


