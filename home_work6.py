# Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr, target):
    def binary_search_recursive(arr, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)

    left, right = 0, len(arr) - 1
    return binary_search_recursive(arr, target, left, right)

arr = [1, 3, 5, 7, 9, 11, 13, 15]

try:
    target = int(input("Введите искомое число: "))
except ValueError:
    print("Ошибка: Введите целое число.")
    exit(1)

result = binary_search(arr, target)

if result != -1:
    print(f"Искомый элемент {target} найден в массиве по индексу {result}.")
else:
    print(f"Искомый элемент {target} не найден в массиве.")
