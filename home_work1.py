# У вас есть массив целых чисел, в котором каждое число, кроме одного, повторяется дважды. Вам нужно найти это одиночное число.

# ver 1
arr =  [4, 3, 2, 4, 1, 3, 2]
result = 0

for i in arr:
  result^=i
print("Одиночное число:", result)

# ver 2
arr =  [4, 3, 2, 4, 1, 3, 2]

arr.sort()
i = 0
while i <= len(arr)-1:
  if i == len(arr)-1:
    print(arr[i])
    break
  if arr[i] == arr[i+1]:
    i += 2
  else:
    print(arr[i])
    break
