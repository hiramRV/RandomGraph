# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 2021

@author: S. Hiram Rubio
Codigo que utiliza el algoritmo de 
"backtraking" para resolver el problema 
"n reinas en el tablero de ajedrez"

Code to use the backtracking method 
as a solution of the problem:
    n queens on board
    
Codigo fuente se basa de / Source code base on
https://www.coursera.org/learn/what-is-a-proof?specialization=discrete-mathematics 
"""

#Methods / Metodos
#--------------------------------------

#Extend validation / Validacion para extender
def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

#Exten on current solution / Extension en busqueda de solucion
def extend(perm, n):
    #Global variable / Variables globales
    global solution
    #Saving each iteration / Guardamos cada permutacion
    wr = ( str(solution), str(len(perm)))
    writer.writerow(wr)
    solution = solution+1
    #Print solution / print de soluciones
    if len(perm) == n:
        print(perm)
        pass
    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)
            perm.pop()
            
#Libs / Librerias
import csv

#Vars / Variables
solution = 0
perm = []
n = 8

#Generate CSV with each iteration / Generacion del CSV con cada iteracion
with open(f"Data/BT{n}.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('i', 'len'))
    extend(perm, n)
print(f"Number of iterations for n = {n} is: {solution}")

