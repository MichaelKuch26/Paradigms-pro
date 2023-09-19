from sympy import symbols, Not, And, Or, simplify_logic

# Определение символьных переменных
A, B, C = symbols('A B C')

# Создание логического выражения
expression = And(A, Or(B, Not(C)))

# Упрощение логического выражения
simplified_expression = simplify_logic(expression)

# Вывод упрощенного выражения
print(simplified_expression)