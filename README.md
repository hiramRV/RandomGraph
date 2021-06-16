**_English version, [Here](./README2.md)._**

# RandomGraph
Repositorio creado para generar y difundir diferentes grafos aleatorios.  

## Origen
La idea vino mientras estudiaba el algoritmo de backtracking, específicamente el rompecabezas de [“8 damas en el tablero”](https://es.wikipedia.org/wiki/Problema_de_las_ocho_reinas). Al programar y resolverlo noté que la forma en que la solución se construía no tenía un patrón estable, por lo que decidí **explorar** y **explotar** su comportamiento.

## Objetivo
Documentar mediante una página de [twitter](https://twitter.com/bot_rv) el comportamiento aleatorio de este rompecabezas de una formas diferentes. 

## Espacio  

| Variable  | Posibles valores | Descripcion                                                           |
| --------- | ---------------- | --------------------------------------------------------------------- |
|   var0    |                  |   Numero de iteración inicial a graficar                              |
|   var1    |      222222      |   Semilla para variar aleatoriedad                                    |
|   var2    |         4        |   Numero de archivo a leer                                            |
|   var3    |         4        |   Cantidad de nodos.                                                  |

### Dependencias
+ Python 3
+ csv
+ Matplotlib
+ Pandas
+ Random
+ Shapely
+ itertools
+ descartes
+ tweepy
