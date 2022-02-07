# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

test = open('test.txt', 'w')
user = input('Введите текст \n')
while user:
    test.writelines(user)
    user = input('Введите текст \n')
    if not user:
        break
test.close()
test = open('test.txt', 'r')
cont = test.readlines()
print(cont)
test.close()
