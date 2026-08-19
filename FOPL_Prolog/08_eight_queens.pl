% Question 8: Eight Queens Problem
% Shakti Raj Devkota

queens(Qs) :-
    Qs = [_,_,_,_,_,_,_,_],
    permutation([1,2,3,4,5,6,7,8], Qs),
    safe(Qs).

safe([]).
safe([Q|Qs]) :-
    safe(Qs),
    noattack(Q, Qs, 1).

noattack(_, [], _).
noattack(Q, [Q1|Qs], Dist) :-
    Q =\= Q1 + Dist,
    Q =\= Q1 - Dist,
    Dist1 is Dist + 1,
    noattack(Q, Qs, Dist1).

find_all_queens :-
    findall(Qs, queens(Qs), Solutions),
    length(Solutions, Count),
    format('Total solutions: ~w~n', [Count]),
    print_solutions(Solutions, 1).

print_solutions([], _).
print_solutions([Qs|Rest], N) :-
    format('Solution ~w: ~w~n', [N, Qs]),
    N1 is N + 1,
    print_solutions(Rest, N1).