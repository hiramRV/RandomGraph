# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 2021

@author: Steven Rubio
Code to use the backtracking method 
as a solution of the problem:
    n queens on board
"""

def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    #Variables globales
    global solution
    #Guardamos cada permutacion
    wr = ( str(solution), str(len(perm)))
    writer.writerow(wr)
    solution = solution+1
    if len(perm) == n:
        #print(perm)
        pass
        #exit()
    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)
            perm.pop()
#Libs
import csv

#Vars           
solution = 0
perm = []
n = 12

#Generate CSV with each iteration
with open('BT12.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('i', 'len'))
    extend(perm, n)
print(f"Number of iterations for n = {n} is: {solution}")

