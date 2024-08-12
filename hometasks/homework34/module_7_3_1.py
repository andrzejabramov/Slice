team1 = 'Мвстера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 0
time_avg = 0
challenge_result = 'Победа команды'


if (score1 > score2 and team1_time <= team2_time) or (score1 >= score2 and team1_time < team2_time):
    challenge_result = challenge_result + f" {team1}"
elif (score1 < score2 and team1_time >= team2_time) or (score1 <= score2 and team1_time > team2_time):
    challenge_result = challenge_result + f" {team2}"
else:
    challenge_result = 'Ничья'

tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / 2

print('В команде %s участников %s' % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print('Команда {} решила задач {}!'.format(team2, score2))
print('время, за которое команда {} решила задачи {} сек!'.format(team2, team1_time))
print(f"Команды решили {score1} и {score2} задач")
print('Результат битвы: ' + challenge_result)
print(f"Сегодня было решено {tasks_total} задач в среднем за {time_avg} секунды за задачу!")
