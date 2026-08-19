% Question 15: Ram Naughty Problem
% Shakti Raj Devkota

oversmart(hari).
child(ram, hari).

stupid(X) :- oversmart(X).

naughty(X) :- child(X, Y), stupid(Y).
