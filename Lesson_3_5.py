us_in = input('Введите числа через пробел или "+" для выхода: ')

"""Функция должна возвращать сумму введенных чисел.. Но у меня
она работет только, если ввести +. В противном случае - 
считает до бесконечности. Извините.."""
def my_func():
    res = 0
    while True:
        number = us_in.split()
        for i in number:
            if i == '+':
                return (f'Сумма равна: {res}. Выход из программы')
            else:
                res += int(i)
                print(f'Сумма равна {res}')

us_in = my_func()
print(us_in)
