# 1. У вас есть список чисел, и вам нужно вычислить среднее значение этого списка чисел.


# Структурное программирование

numbers = [12, 45, 78, 90, 56, 23, 67, 89]
summ = 0
numb=len(numbers)
for number in numbers:
  summ+=number
sz = summ/numb
print(sz)

# Процедурное программирование

numbers = [12, 45, 78, 90, 56, 23, 67, 89]

def average(numbers):
  summ = sum(numbers)
  count = len(numbers)
  
  if count == 0:
    return None

  average = summ/count
  return average

aver = average(numbers)
print(aver)

#2. Представьте, что у вас есть онлайн-магазин, и вы хотите реализовать функцию расчета скидки на покупку, в зависимости от следующих условий: Если общая сумма покупки больше или равна 1000 рублей, то скидка составляет 10%. Если общая сумма покупки больше или равна 500 рублей, то скидка составляет 5%. В остальных случаях скидки нет.

# Процедурное программирование

def count_sale(summm):    # Функция для расчета скидки
  if summm >= 1000:
    sale = summm*0.10     # 10%
  elif summm >= 500:
    sale = summm*0.05     # 5%
  else:
    sale = 0
  return sale

summm = 1200

print(count_sale(summm))


# У нас есть отсортированный список целых чисел, и мы хотим найти определенное число в этом списке. Нам нужно реализовать функцию для поиска числа в списке.

# Структурное программирование

sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]  # Отсортированный список
target_number = 7                             # Искомое число


if target_number in sorted_numbers:
  result = sorted_numbers.index(target_number)
  print(f"Число {target_number} найдено в позиции {result+1}.")
else:
  print(f"Число {target_number} не найдено в списке.")
  

if result != -1:                              # Проверяем результат и выводим сообщение
  print(f"Число {target_number} найдено в позиции {result+1}.")
else:
  print(f"Число {target_number} не найдено в списке.")  



# Процедурное программирование

sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]  # Отсортированный список
target_number = 7                             # Искомое число

def search(sorted_numbers, target_number):
  if target_number in sorted_numbers:
    result = sorted_numbers.index(target_number)
    print(f"Число {target_number} найдено в позиции {result+1}.")
  else:
    print(f"Число {target_number} не найдено в списке.")
    
print(search(sorted_numbers, target_number))