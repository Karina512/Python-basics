'''Функция возвращения суммы двух наибольших аргументов'''

def my_func (num_1, num_2, num_3):
    new = [num_1, num_2, num_3]
    new.remove(min(num_1, num_2, num_3))
    return sum(new)

print(my_func(2, 6, 3))
