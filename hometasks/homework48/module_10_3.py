from random import randint
from time import sleep
from threading import Thread, Lock


class Bank:
    trans = 100
    balance = 0
    lock = Lock()

    def deposit(self):
        for tr in range(1, self.trans+1):
            rand_ent = randint(50, 500)
            self.balance = self.balance + rand_ent
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rand_ent}. Баланс {self.balance}. ')
            sleep(0.001)
        return None


    def take(self):
        for tr in range(1, self.trans+1):
            rand_exp = randint(50, 500)
            print(f'Запрос на {rand_exp}. ')
            if rand_exp > self.balance:
                print('Запрос отклонен, недостаточно средств ')
                self.lock.acquire()
            else:
                self.balance = self.balance - rand_exp
                print(f'Снятие {rand_exp}. Баланс: {self.balance}. ')
            sleep(0.001)
        return None

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

