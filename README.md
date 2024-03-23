#
### CI5437 - Inteligencia Artificial 1
##### Prof. Carlos Infante
# Proyecto 3: CNF-SAT
Por Oliver Bueno, Alejandro Meneses

## Presentación del problema
En este proyecto se centra en la organización eficiente de un torneo, en donde se busca la asignación eficiente de fechas y horas para los juegos de un torneo. Frente a un conjunto de reglas y restricciones de tiempo, buscando garantizar que cada equipo juegue el número adecuado de partidos, tanto de local como de visitante, y que todos los juegos se programen de manera justa y dentro de un período específico.

#### Resultados de las pruebas
| Nº Equipos | Horas | Días | Variables  | Clausulas     | Tiempo (s) |
|------------|-------|------|------------|---------------|------------|
| 4          | 4     | 6    | 168        | 5604          | 0.008594   |
| 4          | 4     | 31   | 744        | 43620         | 0.037973   |
| 4          | 6     | 61   | 2196       | 288138        | 0.411798   |
| 5          | 6     | 61   | 3660       | 538430        | 0.753633   |
| 5          | 8     | 61   | 4880       | 944180        | 1.505926   |
| 29.        | Negro   | -4    | 10          | 14         | 5.00004e-06 |
| 28.        | Blanco  | -4    | 64          | 91         | 3.80001e-05 |
| 27.        | Negro   | -4    | 125         | 177        | 7.70001e-05 |
| 26.        | Blanco  | -4    | 744         | 1049       | 0.000472   |
| 25.        | Negro   | -4    | 3168        | 4498       | 0.002021   |
| 24.        | Blanco  | -4    | 8597        | 11978      | 0.004796   |
| 23.        | Negro   | -4    | 55127       | 76826      | 0.03269    |

