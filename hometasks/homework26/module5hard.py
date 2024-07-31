from time import sleep


"""
Класс участвует в процессах регистрации и авторизации пользователей, а также создания списка пользователей
"""
class User:
    def __init__(self, nickname, password, age=None):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self) -> str:
        return f"{self.nickname}, {hash(self.password)}, {self.age}"

    def user_list(self) -> list:
        l = [self.nickname, hash(self.password), self.age]
        return list(l)


"""
Класс участвует в процессах создания списка видео для фильмотеки, проверки соответствия введенных параметров 
пользователем (время воспроизведения фильма не может быть больше длительности фильма)
"""
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        if time_now > duration:
            print('Вы ввели время просмотра видео больше его длительности,\n' \
                  'поэтому просмотр будет длиться до окончания фильма')
            self.time_now = duration

    def __str__(self) -> str:
        return f"{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}"

    def film(self):
        l = [self.title, self.duration, self.time_now, self.adult_mode]
        return list(l)


"""
 Класс выполняет основную работу в приложении и его методы создают список юзеров, фильмотеку 
 путем добавления параметров соответсвующих классов в статические параметры - матрицы, а также
 осуществляют авторизацию, выход из аккаунта, поиск фильма в фильмотеке и сенанс просмотра с 
 предварительной проверкой параметров фильмов и пользователей 
 """
class UrTube:
    users = []
    videos = []
    def __init__(self, current_user=None):
        self.current_user = current_user

    def __str__(self):
        return f"{self.users}, {self.videos}, {self.current_user}"

    def log_in(self, nickname, password):
        u = User(nickname, password)
        l = u.user_list()[:-1]
        for i in range(len(UrTube.users)):
            nick = UrTube.users[i][:-1]
            if nick == l:
                self.current_user = nickname
                return f"Добро, пожаловать, {nickname}!"
        return f"Неверно введен логин {nickname} или пароль"

    def register(self, nickname, password, age):
        u = User(nickname, password, age)
        l = u.user_list()
        if len(UrTube.users) > 0:
             for i in range(len(UrTube.users)):
                  if UrTube.users[i][0] == nickname:
                      return f"Пользователь {nickname} уже существует"
        UrTube.users.append(l)
        self.current_user = nickname
        return f"{nickname}! Поздравляем с регистрацией!"

    def lod_out(self):
        nick = self.current_user
        self.current_user = None
        return f"{nick}, Вы вышли из аккаунта"

    def add(self, *args):
        for v in args:
            f = Video.film(v)
            if len(UrTube.videos) > 0:
                for i in range(len(UrTube.videos)):
                    if UrTube.videos[i][0] == f[0]:
                        return None
            UrTube.videos.append(f)
        return None

    def get_videos(self, template):
        l = []
        for temp in range(len(UrTube.videos)):
            name = UrTube.videos[temp][0]
            if template.lower() in name.lower():
                l.append(name)
        return l

    def watch_video(self, name):
        if self.current_user == None:
            return 'Для просмотра видео авторизуйтесь пожалуйста'
        for i in range(len(UrTube.videos)):
            if name == UrTube.videos[i][0]:
                for u in range(len(UrTube.users)):
                    if self.current_user == UrTube.users[u][0]:
                        if UrTube.users[u][2] < 18 and (UrTube.videos[i][3] is True):
                            return 'Вам нет 18 лет, пожалуйста покиньте страницу'
                view = self._dur_video(UrTube.videos[i][2])
                return view
        return f"Фильм {name} в фильмотеке не обнаружен"

    def _dur_video(self, time_now=0):
        while True:
            tm = mn = h = '00'
            sec = 0
            for q in range(0, 24):
                h = tm[:-len(str(q))] + str(q)
                for j in range(0, 60):
                    mn = tm[:-len(str(j))] + str(j)
                    for i in range(0, 60):
                        sc = tm[:-len(str(i))]+str(i)
                        dur = h+':'+mn+':'+sc
                        print('Идет просмотр видео. '+dur)
                        sleep(0.5)#для предотвращения времени вывода печати в консоль сократил время засыпания вдвое
                        if sec == time_now:
                            return 'Конец видео'
                        sec += 1
            return 'Конец видео'


ur = UrTube()#создаем экземпляр класса UrTube
print(' \nсоздаем экз класса Video с обработкой ошибок установки параметров\n' \
      '(время просмотра файла более длительности воспроизведения и без возрастных ограничений)\n')
v1 = Video('Лучший язык программирования 2024 года', 20, 200)
print(v1)
print('\nСоздаем экз класса Video с возрастными ограничениями')
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
print(v2)
print('\nДобавляем оба фильма в фильмотеку (параметр videos) методом add класса UrTube')
ur.add(v1, v2)
print(ur.videos)
print('\nрегистрируем в списке пользователей пользователя младше 18 лет\n' \
      '(параметр users класса UrTube) через метод register')
a = ur.register('vasya_pupkin', 'lolkekcheburek', 13)
print(a)
print('\nпробуем повторно зарегистрироваться')
b = ur.register('vasya_pupkin', 'lolkekcheb', 1)
print(b)
print('\nрегистрируем второго пользователя старше 18 лет')
c = ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print(c)
print('\nПроверяем список пользователей')
print(ur.users)
print('\nПробуем авторизовать пользователя с несуществующим логином или ошибочным паролем')
d = ur.log_in('ghjgj', 'fsdsfd')
print(d)
print('\nавторизуем зарегистрированного пользователя с помощью метода log_in класса UrTube')
e = ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(e)
print('\nвыходим из аккаунта только что авторизованного пользователя с помощью метода log_out класса UrTube')
f = ur.lod_out()
print(f)
print('\nищем фильмы в фильмотеке по строке с помощью метода get_videos класса UrTube')
g = ur.get_videos('ПРОГ')
print(g)
h = ur.get_videos('Лучш')
print(h)
print('\nхотим посмотреть фильмы из фильмотеки с помощью метода whatch_video класса UrYube (нет авторизованных пользователей)')
j = ur.watch_video('Для чего девушкам парень программист?')
print(j)
print('\nавторизуем для просмотра фильма 18+ пользователя младше 18')
k = ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(k)
print('\nпытаемся воспроизвести фильм')
m = ur.watch_video('Для чего девушкам парень программист?')
print(m)
print('\nменяем запрос на фильм без возрастных ограничений и начинаем просмотр фильма')
o = ur.watch_video('Лучший язык программирования 2024 года')
print(o)
print('\nвыходим из аккаунта пользователя младше 18')
p = ur.lod_out()
print(p)
print('\nавторизуем пользователя старше 18')
t = ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(t)
print('\nвводим название фильма для просмотра с ошибкой')
v = ur.watch_video('ля чего девушкам парень программист')
print(v)
print('\nисправляем ошибки в названии видео')
w = ur.watch_video('Для чего девушкам парень программист?')
print(w)