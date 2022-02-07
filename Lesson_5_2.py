# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

new_file = open('test_1.txt', 'r')
cont = new_file.read()
print(f'в файле записано:\n{cont}')
new_file = open('test_1.txt', 'r')
cont = new_file.readlines()
print(f'количество строк в файле: {len(cont)}')
new_file = open('test_1.txt', 'r')
cont = new_file.readlines()
for el in range(len(cont)):
    print(f'количество символов в строках:{len(cont[el])}')
new_file = open('test_1.txt', 'r')
cont = new_file.read()
cont = cont.split()
print(cont)
print(f'общее количество слов: {len(cont)}')
