# Сортировка вставками
array = [4, 3, 2, 10, 12, 1, 5, 6]


def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i
        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1
        array[j] = x
    return array


sorted = insert_sort(array)
print(sorted)


# from functools import reduce
#
# array = [4, 3, 2, 10, 12, 1, 5, 6]
#
# def insert_sort(arr):
#     # Вспомогательная функция для сортировки одного элемента в массиве
#     def sort_elem(acc, elem):
#         i, result = acc
#         while i > 0 and result[i - 1] > elem:
#             result[i] = result[i - 1]
#             i -= 1
#         result[i] = elem
#         return i + 1, result
#
#     # Используем reduce для применения sort_elem ко всем элементам массива
#     _, sorted_array = reduce(sort_elem, arr[1:], (1, arr))
#     return sorted_array
#
# sorted_array = insert_sort(array)
# print(sorted_array)