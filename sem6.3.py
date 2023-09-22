# This is a sample Python script.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [22, 15, 1, 3, 44, 55, -3]

bubble_sort(arr)
print("Massive redy: ")
for i in range(len(arr)):
    print(arr[i])


# def bubble_sort(arr):
#     def swap(i, j):
#         arr[i], arr[j] = arr[j], arr[i]
#
#     n = len(arr)
#     for _ in range(n - 1):
#         swapped = False
#         for j in range(n - 1):
#             if arr[j] > arr[j + 1]:
#                 swap(j, j + 1)
#                 swapped = True
#         if not swapped:
#             break
#
# arr = [22, 15, 1, 3, 44, 55, -3]
#
# bubble_sort(arr)
# print("Отсортированный массив:")
# print(arr)