child(X,Y) :- parent(Y,X).
parent(ann,bob). parent(bob,carol). parent(bob,dan).
% #show child/2.
