# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('test_4.txt', 'w+') as file:
    file.write(input('Введите числа через пробел: '))

with open('test_4.txt') as file:
    data = file.read().split()
sum =  0
for el in data:
    sum += int(el)
print(sum)
