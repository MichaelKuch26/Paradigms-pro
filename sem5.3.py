from sympy import symbols, And, Or, Not, simplify_logic

# Определение символьных переменных
A, B, C, D = symbols('A B C D')

# Определение логических выражений
expression1 = Or(And(A, B), Not(C))
expression2 = And(Or(A, B), Or(C, D))
expression3 = Or(And(A, B), And(C, D))

# Ввод значений переменных
values = {A: True, B: False, C: True, D: False}

# Проверка истинности выражений с заданными значениями переменных
result1 = simplify_logic(expression1.subs(values))
result2 = simplify_logic(expression2.subs(values))
result3 = simplify_logic(expression3.subs(values))

# Вывод результатов
print("Выражение 1 истинно:", result1)
print("Выражение 2 истинно:", result2)
print("Выражение 3 истинно:", result3)