us_im = input('введите слова: ')
us_im_1 = us_im.split( )
n = 0
for elem in us_im_1:
    '{}'.format(elem)
    print(f'#{n+1}, {elem[:10]}')
    n += 1
    