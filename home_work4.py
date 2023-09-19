# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно упростит вам жизнь.

import math

array1 = [10, 6, 1, 13, 5]
array2 = [12, 10, 7, 6, 8]

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
  if len(x) == len(y):
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diff_prod = 0
    x_diff2 = 0
    y_diff2 = 0
    for id_x in range(n):
        x_diff = x[id_x] - avg_x
        y_diff = y[id_x] - avg_y
        diff_prod += x_diff * y_diff
        x_diff2 += x_diff * x_diff
        y_diff2 += y_diff * y_diff
    return diff_prod / math.sqrt(x_diff2 * y_diff2)
  else: 
    return ValueError ("Массивы имеют разный размер")
print (pearson_def(array1, array2))