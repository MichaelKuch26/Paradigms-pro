# Реализовать процедуру для вычисления MSE на любом языке в любой парадигме. Программа получает на вход два вектора и возвращает число - оценку MSE для этих векторов.

def calculate_mse(vector1, vector2):
    # Проверяем, что векторы имеют одинаковую длину
    if len(vector1) != len(vector2):
        raise ValueError("Длины векторов должны совпадать")

    # Вычисляем сумму квадратов разностей элементов векторов
    squared_errors = [(x - y) ** 2 for x, y in zip(vector1, vector2)]

    # Вычисляем среднее значение суммы квадратов
    mse = sum(squared_errors) / len(vector1)

    return mse


# Пример использования функции
vector1 = [1, 2, 3, 4, 5]
vector2 = [1.5, 2.2, 2.8, 3.7, 5.1]

mse = calculate_mse(vector1, vector2)
print(f"MSE: {mse}")