num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

'''Функция деления двух чисел, введенных пользователем,
возвращает результат деления'''
def my_func (num_1, num_2):
    if num_2 == 0:
        return 0
    else:
        return num_1 / num_2

result = my_func(num_1, num_2)
print(result)
