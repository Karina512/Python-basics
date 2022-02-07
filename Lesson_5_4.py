# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

my_list = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
my_file = []
with open('test_3.txt', 'r') as file_obj:
    for el in file_obj:
        el = el.split(' ', 1)
        my_file.append(my_list[el[0]] + ' ' + el[1])
        print(my_file)
with open('test_3_1.txt', 'w') as file_obj_1:
    file_obj_1.writelines(my_file)
