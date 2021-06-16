# RandomGraph
Repository created to generate and disseminate different random graphs.

## Source
The idea came while studying the backtracking algorithm, specifically the [“8 checkers on the board”] puzzle (https://es.wikipedia.org/wiki/Problema_de_las_ocho_reinas). When programming and solving it I noticed that the way the solution was built did not have a stable pattern, so I decided to ** explore ** and ** exploit ** its behavior.

## Objective
Document through a [twitter] page (https://twitter.com/bot_rv) the random behavior of this puzzle in a different way.

## Space  

| Variable  | Possible values  |   Description                                                         |
| --------- | ---------------- | --------------------------------------------------------------------- |
|   var0    |                  |   Initial iteration number to plot                                    |
|   var1    |      222222      |   Seed to vary randomness                                             |
|   var2    |         4        |   File number to read                                                 |
|   var3    |         4        |   Number of nodes                                                     |

### Dependencies
+ Python 3
+ csv
+ Matplotlib
+ Pandas
+ Random
+ Shapely
+ itertools
+ descartes
+ tweepy