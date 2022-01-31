a = float (input ('введите дистанцию в первый день: '))
b = float (input ('введите цель: '))
day = 1
while a < b:
    a *= 1.1
    day += 1
print (f'Нужно дней: {day}')
