from threading import Thread
import queue
from time import sleep
import random


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        return sleep(random.randint(3, 10))


class Cafe:
    que = queue.Queue()
    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        for g in guests:
            for tbl in self.tables:
                if tbl.guest is None:
                    g.start()
                    tbl.guest = g
                    print(f'{g.name} сел(-а) за стол номер {tbl.number}')
                    break
            else:
                self.que.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        for guest in guests:
            if guest.is_alive():
                guest.join()
        list_tables = list(self.tables)
        while len(list_tables) > 0:
            for tbl in list_tables:
                if tbl.guest != None:
                    print(f'{tbl.guest.name} покушал(-а) и ушел(ушла).\nСтол номер {tbl.number} свободен')
                    tbl.guest = None
                    if self.que.empty() == False:
                        g_que = self.que.get()
                        cafe.guest_arrival(g_que)
                        g_que.join()
                    else:
                        list_tables.remove(tbl)


tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()

