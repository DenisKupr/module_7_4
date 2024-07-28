# Входные данные
team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Расчет результата в зависимости от баллов и времени решения задач
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

# Использование %
formatted_string1 = "В команде Мастера кода участников: %d !" % team1_num
print(formatted_string1)

formatted_string2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(formatted_string2)

# Использование format()
formatted_string3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(formatted_string3)

formatted_string4 = "Волшебники данных решили задачи за {:.1f} с !".format(team1_time)
print(formatted_string4)

# Использование f-строк
formatted_string5 = f"Команды решили {score_1} и {score_2} задач."
print(formatted_string5)

formatted_string6 = f"Результат битвы: {result}"
print(formatted_string6)

formatted_string7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!."
print(formatted_string7)
