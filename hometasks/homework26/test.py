from time import sleep


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
                sec += 1
                print('Идет просмотр видео. '+dur)
                sleep(0.0001)
    break














#https://pygame.ru/blog/kak-sdelat-sekundomer-v-python.php
