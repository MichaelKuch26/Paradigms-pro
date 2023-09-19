list_sum([],0).

list_sum([Enter|Tail], TotalSum):-
list_sum(Tail, Sum1),
TotalSum is Head+Sum1.


