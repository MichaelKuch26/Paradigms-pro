### Ex1. loop sum
arr = [1,2,3,4,5,6,7,8,9,10] # Объявляем массив arr
summ = 0                     # Объявляем переменную summ равно нулю
for el in arr:               # Перебираем элементы массива arr
  summ += el                 # на каждом шаге уыеличива summ на arr
print(summ)                  # Выводим summ на экран

### Ex2. Built-in sum()
arr = [1,2,3,4,5,6,7,8,9,10] # Объявляем массив arr
print(sum(arr))


### Ex3. Map and reduce
from functools import reduce
arr = [1,2,3,4,5,6,7,8,9,10]
res = reduce(lambda x, y: x+y, arr)
print(res)