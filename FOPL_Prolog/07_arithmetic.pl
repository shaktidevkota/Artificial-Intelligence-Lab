% Question 7: Arithmetic Operations
% Shakti Raj Devkota

arithmetic_operations :-
    write('Enter first number: '),
    read(A),
    write('Enter second number: '),
    read(B),
    Sum is A + B,
    Difference is A - B,
    Product is A * B,
    Division is A / B,
    write('Sum = '), write(Sum), nl,
    write('Difference = '), write(Difference), nl,
    write('Product = '), write(Product), nl,
    write('Division = '), write(Division), nl.