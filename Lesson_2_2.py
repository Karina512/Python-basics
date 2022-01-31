user = input('введите числа: ')
us_list = user.split()
us_list_len = len(us_list) 
i = 0
if us_list_len > 1:
    while i < us_list_len -1:
        us_list[i], us_list[i+1] = us_list[i+1], us_list[i]
        i += 2
print(us_list)
