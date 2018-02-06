pa(N,N*N+N+41) :- N+1=1..11.
pb(N,N*N+N+41) :- N=-10..10, N>=0.

pe(M,N) :- N=1..4, N=2*M.
%#show pe/2.

