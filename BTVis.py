# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19  2021

@author: Steven Rubio
Code to generate random plots base on the
Backtracking solution of the problem:
    n queens on board
"""
    
#Importamos librerias
import matplotlib.pyplot as plt
import pandas as pd
from random import seed
from random import randint

#seed random number generator
seed(randint(0,222))
#Files and Random read  
Files = ['BT04.csv','BT06.csv','BT08.csv','BT10.csv','BT12.csv']
n = randint(0,4)
dfe = pd.read_csv(Files[n])

#CSVData
i = dfe['i']
lbt = dfe['len']

#Chek for every casi n>0
if(max(i)>16):
    #We Select a random range of 16 iterations
    x0 = randint(0,max(i)-16)
    i = i[x0:x0+16]
    lbt = lbt[x0:x0+16]

#Plot
fig, ax = plt.subplots(figsize= (8,6))
ax.scatter(dfe['i'],dfe['len'], c = '#707270', marker = 'o',edgecolor= 'k')
        
#Random Nodes
cont = randint(10,2*int(-min(i)+max(i)))
for random in range(cont):
    #Seach 2 random nodes
    rv= dfe[dfe.i.eq(randint(min(i),max(i)))]
    rv2= dfe[dfe.i.eq(randint(min(i),max(i)))]
    rpnt = [int(rv['i']),int(rv['len'])]
    rpnt2 = [int(rv2['i']),int(rv2['len'])]
    #Plot line
    ax.plot([rpnt[0],rpnt2[0]],[rpnt[1],rpnt2[1]], 'k')
    #cont = cont-1

#Plot text and axis
ax.set_title(f"Nodes of: Backtracking {max(dfe['len'])} Queens on board (cont = {cont})")
ax.set_ylabel('Queens on board')
ax.set_xlabel('Iterations')
ax.set_xlim(xmin = min(i)-0.5, xmax=max(i)+0.5)
ax.set_ylim(ymin=min(lbt)-0.5, ymax=max(lbt)+0.5)        
#Clean whitespace
fig.tight_layout()
#Save
fig.savefig(f"BT_{max(dfe['len'])}QOB{cont}N.png")
