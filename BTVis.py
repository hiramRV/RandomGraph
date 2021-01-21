# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19  2021

@author: S. Hiram Rubio
Codigo para generar plots aleatorio con 
base a la solucion con "Backtracking" en 
el problema de "n queens on board"

Code to generate random plots base on the
Backtracking solution of the problem:
    n queens on board
"""
    

def random_graph():
    #Libs / librerias
    import matplotlib.pyplot as plt
    import pandas as pd
    from random import seed
    from random import randint
    
    #seed random number generator / Semilla para número aleatorio
    var1 = randint(0,222)
    seed(var1)
    #Files and Random read / Archivos y lectura random
    Files = ['BT04.csv','BT06.csv','BT08.csv','BT10.csv','BT12.csv']
    var2 = randint(0,4)
    dfe = pd.read_csv("Data/"+Files[var2])
    
    #CSVData
    i = dfe['i']
    lbt = dfe['len']
    
    #Check for every case n>0 / Revisa si es un caso diferente del caso 0
    var0 = 0
    if(max(i)>16):
        #We Select a random range of 16 iterations 
        #Seleccion de rango aleatorio de 16 iteraciones
        var0 = randint(0,max(i)-16)
        i = i[var0:var0+16]
        lbt = lbt[var0:var0+16]
    
    #Plot / Grafica
    fig, ax = plt.subplots(figsize= (8,6))
    ax.scatter(dfe['i'],dfe['len'], c = '#707270', marker = 'o',edgecolor= 'k')
            
    #Random Nodes / Nodos aleatorios
    var3 = randint(10,2*int(-min(i)+max(i)))
    for random in range(var3):
        #Seach 2 random nodes / Busqueda de dos Nodos 
        rv= dfe[dfe.i.eq(randint(min(i),max(i)))]
        rv2= dfe[dfe.i.eq(randint(min(i),max(i)))]
        rpnt = [int(rv['i']),int(rv['len'])]
        rpnt2 = [int(rv2['i']),int(rv2['len'])]
        #Plot line / Plot linea
        ax.plot([rpnt[0],rpnt2[0]],[rpnt[1],rpnt2[1]], 'k')
    
    #Plot text and axis / Texto y ejes
    ax.set_title(f"Nodes of: Backtracking {max(dfe['len'])} Queens on board (cont = {var3})")
    ax.set_ylabel('Queens on board')
    ax.set_xlabel('Iterations')
    ax.set_xlim(xmin = min(i)-0.5, xmax=max(i)+0.5)
    ax.set_ylim(ymin=min(lbt)-0.5, ymax=max(lbt)+0.5)        
    fig.tight_layout()
    #Save / Guardando Imagen
    Name = f"Imgs/BT_{max(dfe['len'])}QOB{var3}N.png"
    fig.savefig(Name)
    
    return Name,var0,var1,var2,var3


def generate_graph( FLAG = False, DELETE = False):
    #Libs / librerias
    from tweet0 import create_tweet_media
    import os
    
    skip = "\n"
    #Generate Graph and Data / Generando Grafo y data
    Name,var0,var1,var2,var3 = random_graph()
    text = f"Semilla: {var1} {skip}Archivo: {var2} {skip}Iteracion Inicial: {var0} {skip}Nodos: {var3}"
    #Tweet
    if(FLAG): create_tweet_media([Name],text, myData =True)
    #Delete Img / Borrar Imagen
    if(DELETE): os.remove(Name)

#Run de code / Correr código
if __name__ == "__main__":
    generate_graph(DELETE = True)