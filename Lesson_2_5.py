my_list = [9, 7, 6, 4, 3, 3, 2, 1]
us_in = int(input('Введите число: '))
insd = False
for index, elem in enumerate(my_list):
    if us_in > elem:
        my_list.insert(index, us_in)
        insd = True
        break
if not insd:
    my_list.append(us_in)
print(my_list)
