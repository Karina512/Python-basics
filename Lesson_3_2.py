name = input('Ваше имя: ')
second_name = input('Фамилия: ')
year_of_birth = input('Год рождения: ')
city_residence = input('Ваш город: ')
e_mail = input('E-Mail: ')
number_phone = input('Телефон: ')

'''Функция вывода данных пользователя одной строкой'''
def my_func (a=name, b=second_name, с=year_of_birth, d=city_residence, f=e_mail, g=number_phone):
    return f'Пользователь:{a} {b} {с} {d} {f} {g}'

user = my_func(a=name, b=second_name, с=year_of_birth, d=city_residence, f=e_mail, g=number_phone)
print(user)
