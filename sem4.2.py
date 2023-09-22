# Исходные оценки студентов в различных форматах
grades_raw = ["5.0", "4.5", "4.0", "3.5", "A-"]

# Создаем пустой список для хранения стандартизированных оценок
grades_standardized = []

# Создаем словарь для сопоставления нестандартных оценок с их стандартными эквивалентами
grade_mapping = {
"A+": 5.0,
"A": 4.5,
"A-": 4.0,
"B+": 3.5,
"B": 3.0,
"B-": 2.5,
"C+": 2.0,
"C": 1.5,
"C-": 1.0,
"D": 0.5,
"F": 0.0
}

# Проходим по каждой нестандартной оценке
for grade_raw in grades_raw:
# Пробуем найти стандартный эквивалент в словаре
  if grade_raw in grade_mapping:
# Если нашли, добавляем стандартизированную оценку в список
    grade_standardized = grade_mapping[grade_raw]
    grades_standardized.append(grade_standardized)
  else:
# Если не нашли, выводим сообщение об ошибке и пропускаем оценку
    print(f"Ошибка: Не удалось стандартизировать оценку - {grade_raw}")

# Теперь у нас есть список стандартизированных оценок
print("Стандартизированные оценки:", grades_standardized)