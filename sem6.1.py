# Реализовать сортировку слиянием на любом языке в любой парадигме. На вход ваша программа получает массив из чисел, а вернуть должна отсортированный массив.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделяем массив пополам
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем обе половины
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Сливаем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


# Пример использования функции merge_sort
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)
#
# result = []
# while (len(arr) > 0):
#     result.append(min(arr))
#     arr.remove(min(arr))