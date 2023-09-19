# Определяем функцию для вычисления логических выражений
def evaluate_expression(expression, values):
# Заменяем переменные в выражении на их значения
  for var, val in values.items():
    expression = expression.replace(var, str(val))
  # Вычисляем значение выражения и возвращаем его
  return eval(expression)

# Задаем выражение и значения переменных
logical_expression = "A and (B or C)"
variables = {"A": True, "B": False, "C": True}

# Вычисляем значение выражения
result = evaluate_expression(logical_expression, variables)

# Выводим результат
print(f"Результат вычисления выражения {logical_expression} при значениях переменных {variables}: {result}")