# Допустим, у нас есть булева функция, которая представляет собой сложное логическое выражение:F(A, B, C, D) = (A AND B) OR (C AND D) OR (A AND C AND D)

from sympy import symbols, And, Or, Not, simplify_logic, to_cnf

# Определение символьных переменных
A, B, C, D = symbols('A B C D')

# Определение исходной булевой функции
F = Or(And(A, B), And(C, D), And(A, C, D))

# Упрощение функции
simplified_F = simplify_logic(F)

# Перевод функции в КНФ (Конъюнктивная нормальная форма)
cnf_F = to_cnf(F)

# Вывод результатов
print("Исходная функция F(A, B, C, D):", F)
print("Упрощенная функция:", simplified_F)
print("Функция в КНФ:", cnf_F)