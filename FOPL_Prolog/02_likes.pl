% Question 2: Likes and Hobbies
% Shakti Raj Devkota

likes(ram, sita).
likes(ram, trains).
likes(suresh, fast_cars).

likes(X, Y) :-
    hobby(X, H),
    hobby(Y, H).

hobby(ram, trainspotting).
hobby(saroj, sailing).
hobby(tina, trainspotting).
hobby(prakash, sailing).