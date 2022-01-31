num = input('Введите месяц: ')
a, b, c, d = 'зима', 'весна', 'лето', 'осень'

month = [a, a, b, b, b, c, c, c, d, d, d, a]
print(month [int(num) - 1])

month_1 = {'1':a, '2':a, '3':b, '4':b, '5':b, '6':c, '7':c, '8':c, '9':d, '10':d,'11':d, '12':a,}
print(month_1[num])
