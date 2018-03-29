% Partition {1,..,n} into r sum-free sets

% input: positive integers n, r.

1 {in(I,1..r)} 1 :- I=1..n.
% achieved: set {1,...,n} is partitioned into
% subsets {I:in(I,1)},...,{I:in(I,r)}.

:- in(I,X), in(J,X), in(I+J,X).
% achieved: these subsets are sum-free


