1 {filled(R, C, 1..n*n)} 1 :- R=1..n, C=1..n.
% achieved: every square of the grid is filled with a number between 1 and n^2

R1=R2 :- filled(R1, _, X), filled(R2, _, X).
C1=C2 :- filled(_, C1, X), filled(_, C2, X).
% achieved: different squares are filled with different numbers

(R1-R2)**2+(C1-C2)**2<=2 :- filled(R1, C1, X), filled(R2, C2, X+1).
% achieved: consecutive numbers connect horizontally, vertically, or diagonally

% :- given (R, C, X), not filled(R, C, X).
% achieved: given/3 is a subset of filled/3.


#show filled/3.
