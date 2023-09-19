from sympy import symbols, And, Not

# Определение символьных переменных
age = symbols('age') # Возраст
medical_condition = symbols('medical_condition') # Медицинские противопоказания
has_ticket = symbols('has_ticket') # Наличие билета
event_open = symbols('event_open') # Мероприятие открыто для посетителей

# Создание логических выражений для условий
condition1 = age >= 18 # Человек должен быть старше 18 лет
condition2 = Not(medical_condition) # Нет медицинских противопоказаний
condition3 = has_ticket # Есть билет на мероприятие
condition4 = event_open # Мероприятие открыто для посетителей

# Создание общего логического выражения для допуска на мероприятие
access_allowed = And(condition1, condition2, condition3, condition4)

# Проверка условий и вывод соответствующего сообщения
if access_allowed:
  print("Допуск разрешен. Приходите на мероприятие!")
else:
  print("Допуск запрещен. Условия не выполнены.")