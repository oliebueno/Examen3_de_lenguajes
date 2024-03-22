#
### CI5437 - Inteligencia Artificial 1
##### Prof. Carlos Infante
# Proyecto 3: CNF-SAT
Por Oliver Bueno, Alejandro Meneses

## Presentación del problema
En este proyecto se centra en la organización eficiente de un torneo, en donde se busca la asignación eficiente de fechas y horas para los juegos de un torneo. Frente a un conjunto de reglas y restricciones de tiempo, buscando garantizar que cada equipo juegue el número adecuado de partidos, tanto de local como de visitante, y que todos los juegos se programen de manera justa y dentro de un período específico.

Para abordar este problema, se recurre a la lógica proposicional y solucionadores SAT. Se han modelado y traducido las reglas del torneo a formato DISMAC CNF, de tal forma que el solucionador SAT puede procesarlo, lo que nos permite explorar los posibles horarios y encontrar uno que cumpla con todas las condiciones impuestas.

## Modelado de las restriciones
Para establecer las restriciones se establece la variable M con los sub-índices l(local), v(visitante), d(día), h(hora), en donde se establecen los siguientes domininios para los sub-índices:

- Dom l: Son todos los posibles equipos.
- Dom v: Son todos los posibles equipos.
- Dom d: Son todas las posibles fechas desde el día inicial, hasta el día final
- Dom h: Son todoas las posible horas en punto en las que puede empezar un juego, esto es, si la hora de inicio es 07:30:00 y la hora de culminación de la jornada es 14:00:00, el dominio de las horas para los encuentros es {08:00:00, 10:00:00, 12:00:00}. El dominio contiene la primera hora en punto más cercana al inicio y se va incrementando cada dos horas hasta la última hora válida.

Cada restricción se modela de la siguiente forma:

- Todos los juegos deben empezar en horas "en punto": Esto esta contemplado por la definicíon de la variable M, dado por el dominio del sub-índice h.
- Todos los juegos deben ocurrir entre una fecha inicial y una fecha final especificadas: Esto esta contemplado por la definicíon de la variable M, dado por el dominio del sub-índice d.
- Todos los juegos deben ocurrir entre un rango de horas especificado: Esto esta contemplado por la definicíon de la variable M, dado por el dominio del sub-índice h.
- Un participante no puede jugar de "visitante" en dos días consecutivos, ni de "local" dos días seguidos: Se definen las siguientes restricciones lógicas

  
  <math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mo stretchy="false">(</mo><mi mathvariant="normal">¬</mi><msub><mi>x</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>j</mi><mo separator="true">,</mo><mi>k</mi><mo separator="true">,</mo><mi>l</mi></mrow></msub><mo>∨</mo><mi mathvariant="normal">¬</mi><msub><mi>x</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>j</mi><mo separator="true">,</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo separator="true">,</mo><mi>l</mi></mrow></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(\neg x_{i,j,k,l} \lor \neg x_{i,j,k+1,l}) 
</annotation></semantics></math>
  
