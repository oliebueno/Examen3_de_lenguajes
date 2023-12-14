%Predicado hermano/2
hermano(A, B) :- arco(C, A), arco(C, B), A \= B.

%Predicado alcanzable/2
alcanzable(A, A).
alcanzable(A, B) :- arco(A, C), alcanzable(C, B).

%Predicado lca/3
lca(A, B, C) :- alcanzable(C, A),
                alcanzable(C, B),
                not((alcanzable(C, D),
                     alcanzable(D, A),
                     alcanzable(D, B),
                     C \= D)).

%Predicado tree/1
tree(A) :- forall(arco(A, B), not(alcanzable(B, A))).
