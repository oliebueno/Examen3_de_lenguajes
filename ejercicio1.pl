%Predicado suma/3
suma(*, X, X).
suma(up(X), Y, up(Z)) :- suma(X, Y, Z).

%Predicado resta/3
resta(X, *, X).
resta(up(X), up(Y), Z) :- resta(X, Y, Z).

%Predicado producto/3
producto(*, _, *).
producto(_, *, *).
producto(up(X), Y, Z) :- producto(X, Y, A), suma(A, Y, Z).