# Импорт необходимых функций и символьных переменных
from sympy import symbols, simplify, expand, Eq, solve, diff, integrate, limit, Matrix, solveset, S

# Создание символьных переменных
x, y, z = symbols('x y z')

# Пример 1: Упрощение выражения
expr = (x + y) ** 2
simplified_expr = simplify(expr)
print("Пример 1 - Упрощение выражения:")
print(simplified_expr)

# Пример 2: Раскрытие скобок
expr = (x + y) ** 2
expanded_expr = expand(expr)
print("\nПример 2 - Раскрытие скобок:")
print(expanded_expr)

# Пример 3: Решение уравнения
eq = Eq(x ** 2 - 4, 0)
solutions = solve(eq, x)
print("\nПример 3 - Решение уравнения:")
print(solutions)

# Пример 4: Вычисление производной
expr = x ** 3 + 2 * x ** 2 + 3 * x + 1
derivative = diff(expr, x)
print("\nПример 4 - Вычисление производной:")
print(derivative)

# Пример 5: Вычисление интеграла
expr = x ** 2 + 2 * x + 1
integral = integrate(expr, x)
print("\nПример 5 - Вычисление интеграла:")
print(integral)

# Пример 6: Вычисление предела
expr = 1 / x
lim = limit(expr, x, 0)
print("\nПример 6 - Вычисление предела:")
print(lim)

# Пример 7: Работа с матрицами
A = Matrix([[1, 2], [3, 4]])
B = Matrix([x, y])
result = A * B
print("\nПример 7 - Работа с матрицами:")
print(result)

# Пример 8: Решение уравнения с выводом решений в виде множества
eq = Eq(x ** 2 - 4, 0)
solutions = solveset(eq, x, domain=S.Reals)
print("\nПример 8 - Решение уравнения с выводом решений в виде множества:")
print(solutions)