% Question 12: Shyam Evil Problem
% Shakti Raj Devkota

greedy_leader(shyam).
honest_leader(gopal).

autocrat(X) :- greedy_leader(X).

evil(X) :- autocrat(X).
