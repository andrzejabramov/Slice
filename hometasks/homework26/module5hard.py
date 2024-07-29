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


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self) -> str:
        return f"{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}"

    def film(self):
        l = [self.title, self.duration, self.time_now, self.adult_mode]
        return list(l)


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
        print(f"{l=}")
        for i in range(len(UrTube.users)):
            nick = UrTube.users[i][:-1]
            print(f"{nick}")
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


    def watch_video(self):
        pass


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
print(v1)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
print(v2)
ur.add(v1, v2)
print(ur.videos)
a = ur.register('vasya_pupkin', 'lolkekcheburek', 13)
print(a)
b = ur.register('vasya_pupkin', 'lolkekcheb', 1)
print(b)
c = ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print(c)
print(ur.users)
d = ur.log_in('ghjgj', 'fsdsfd')
print(d)
e = ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(e)
f = ur.lod_out()
print(f)
g = ur.get_videos('ПРОГ')
print(g)
h = ur.get_videos('Лучш')
print(h)