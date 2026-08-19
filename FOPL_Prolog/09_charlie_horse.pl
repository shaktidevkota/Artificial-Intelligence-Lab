% Question 9: Charlie Horse Problem
% Shakti Raj Devkota

horse(bluebeard).

horse(X) :-
    offspring(X, Y),
    horse(Y).

parent(bluebeard, charlie).

offspring(X, Y) :-
    parent(Y, X).

mammal(X) :-
    horse(X).

mammal(X) :-
    cow(X).

mammal(X) :-
    pig(X).