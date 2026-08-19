% Question 3: HCF and LCM
% Name: Shakti Raj Devkota

% HCF using Euclidean Algorithm
gcd(A, 0, A) :- !.
gcd(A, B, GCD) :-
    R is A mod B,
    gcd(B, R, GCD).

% LCM
lcm(A, B, LCM) :-
    gcd(A, B, GCD),
    LCM is (A * B) // GCD.

% Find both HCF and LCM
hcf_lcm(A, B, HCF, LCM) :-
    gcd(A, B, HCF),
    lcm(A, B, LCM).