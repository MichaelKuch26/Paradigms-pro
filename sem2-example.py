# Пример структурного программирования
# Задача: Найти сумму всех чисел от 1 до N.


n = int(input("Введите число N: "))  # Ввод данных
sum_of_numbers = 0                   # Инициализация переменной для хранения суммы
for i in range(1, n + 1):            # Вычисление суммы
  sum_of_numbers += i
print(f"Сумма всех чисел от 1 до {n} равна {sum_of_numbers}")  # Вывод результата


# Пример процедурного программирования
# Задача: Найти сумму всех чисел от 1 до N.


def calculate_sum(n):                # Функция для вычисления суммы чисел
  sum_of_numbers = 0
  for i in range(1, n + 1):
    sum_of_numbers += i
  return sum_of_numbers

def display_result(n, result):       # Функция для вывода результата
  print(f"Сумма всех чисел от 1 до {n} равна {result}")
n = int(input("Введите число N: "))  # Ввод данных
total_sum = calculate_sum(n)         # Вызов функций
display_result(n, total_sum)


# Пример структурного программирования


students = [                                  # Входные данные: список студентов с оценками
{"имя": "Анна", "оценки": [90, 85, 88]},
{"имя": "Петр", "оценки": [78, 92, 88]},
{"имя": "Мария", "оценки": [85, 87, 92]},
]
total_score = 0                               # Инициализация переменных для суммы и среднего значения
total_students = len(students)
for student in students:                      # Вычисление суммы оценок
  total_score += sum(student["оценки"])
average_score = total_score / (total_students * len(students[0]["оценки"]))         # Вычисление среднего балла
print(f"Средний балл студентов: {average_score:.2f}")     # Вывод результата


# Пример процедурного программирования

def calculate_average(scores):                # Функция для вычисления среднего балла студента
  return sum(scores) / len(scores)

def calculate_class_average(students):        # Функция для вычисления среднего балла всех студентов
  total_score = 0
  total_students = len(students)

  for student in students:
    total_score += calculate_average(student["оценки"])
  return total_score / total_students

students = [                                  # Входные данные: список студентов с оценками
{"имя": "Анна", "оценки": [90, 85, 88]},
{"имя": "Петр", "оценки": [78, 92, 88]},
{"имя": "Мария", "оценки": [85, 87, 92]},
]

average_score = calculate_class_average(students)     # Вычисление среднего балла
print(f"Средний балл студентов: {average_score:.2f}")     # Вывод результата