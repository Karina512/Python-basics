a_1 = input ('введите выручку фирмы')
print (a_1)
b_1 = input ('введите издержки')
print (b_1)
if int(a_1) > int(b_1):
    print ('фирма работает с прибылью')
elif int(a_1) == int(b_1):
    print ('фирма работает без убытков и без прибыли')
else:
    print('фирма работает в убыток')
print ('рентабельность выручки составляет:')
c_1 = int(a_1) / int(b_1)
print (c_1)
d_1 = input ('введите количество сотрудников фирмы')
print (d_1)
f_1 = int(a_1) - int(b_1)
print ('прибыль фирмы в расчете на одного сотрудника составляет')
g_1 = f_1 / int(d_1)
print (g_1)
print ('Конец программы')
