% Question 11: Marcus and Caesar Problem
% Shakti Raj Devkota

pompeian(marcus).
ruler(caesar).
tries_assassinate(marcus, caesar).

roman(X) :-
    pompeian(X).

not_loyal_to(X, Y) :-
    tries_assassinate(X, Y).

hates(X, caesar) :-
    roman(X),
    not_loyal_to(X, caesar).