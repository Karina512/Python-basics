# запускает скрипт расчета зараб.платы с 
# параметрами из командной строки

import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
result = a * b * c
print(result)

