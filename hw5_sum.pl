# Написать программу на языке Prolog для вычисления суммы элементов списка. На вход подаётся целочисленный массив. На выходе - сумма элементов массива.

list_sum([],0).

list_sum([Enter|Tail], TotalSum):-
list_sum(Tail, Sum1),
TotalSum is Head+Sum1.

# Вызов: ?- list_sum([1,9,9,1], Sum).
