% Question 10: George Criminal Problem
% Shakti Raj Devkota

american(george).
enemy(iraq, america).
country(iraq).

has(iraq, missiles).
weapon(missiles).
sold_by(missiles, iraq, george).

hostile(X) :- enemy(X, america).

criminal(Person) :-
    american(Person),
    sold_by(Weapon, HN, Person),
    weapon(Weapon),
    hostile(HN).
