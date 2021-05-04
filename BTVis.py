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

def random_graph(var0 =-1, var1 = -1,var2=-1, var3=-1):
    #Libs / librerias
    import matplotlib.pyplot as plt
    import pandas as pd
    from random import seed, randint
    
    #Check and set vars / Chequeo y calculo de variables
    if(var1==-1):           var1 = randint(0,222222)
    if(var2==-1):           var2 = randint(0,4)
    if(var2>4 or var2<0):   var2 = randint(0,4)
    
    #seed random number generator / Semilla para número aleatorio
    seed(var1)
    #Files and Random read / Archivos y lectura random
    Files = ['BT04.csv','BT06.csv','BT08.csv','BT10.csv','BT12.csv']
    dfe = pd.read_csv("Data/"+Files[var2])
    
    #CSVData
    i = dfe['i']
    lbt = dfe['len']
    
    #Check and set vars 2/ Chequeo y calculo de variables 2
    if(var0==-1):                   var0 = randint(1,max(i)-15)
    if(var0<0 or var0>max(i)-15):   var0 = randint(1,max(i)-15)
    
    #Check for every case n>0 / Revisa si es un caso diferente del caso 0
    if(max(i)>16):
        #We Select a random range of 16 iterations 
        #Seleccion de rango aleatorio de 16 iteraciones
        i = i[var0:var0+16]
        lbt = lbt[var0:var0+16]
    else: var0 = 0
    
    #Check and set vars 3/ Chequeo y calculo de variables 3
    if(var3==-1):                   var3 = randint(1,2*int(-min(i)+max(i)))
    if(var3<0):                     var3 = randint(1,2*int(-min(i)+max(i)))
    
    #Plot / Grafica
    fig, ax = plt.subplots(figsize= (8,6))

    #Node ID*
    nodes = 0            
    #Random Nodes / Nodos aleatorios
    for random in range(var3):
        #Seach 2 random nodes / Busqueda de dos Nodos 
        rv= dfe[dfe.i.eq(randint(min(i),max(i)))] 
        #Ensure different points / Asegurar diferentes puntos
        rv2 = rv
        while(rv2.equals(rv)):
            rv2= dfe[dfe.i.eq(randint(min(i),max(i)))]
        rpnt = [int(rv['i']),int(rv['len'])]
        rpnt2 = [int(rv2['i']),int(rv2['len'])]
        #Node ID construction / Construccion del ID 
        nodes = nodes+ rpnt[0]+rpnt[1]+rpnt2[0]+rpnt2[1]
        #Plot line / Plot linea
        ax.plot([rpnt[0],rpnt2[0]],[rpnt[1],rpnt2[1]], 'k')
        #nodes / Nodos 
        ax.scatter([rpnt[0],rpnt2[0]],[rpnt[1],rpnt2[1]], c = '#707270', marker = 'o',edgecolor= 'k')
    
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
    # / Cerrar imagen para evitar que se muestre
    plt.close(fig)
    
    return Name,var0,var1,var2,var3,nodes


def generate_graph(var0 =-1, var1 = -1,var2=-1, var3=-1, FLAG = True, DELETE = True, PRINT = True):
    #Libs / librerias
    from tweet0 import create_tweet_media
    import os
    
    skip = "\n"
    #Generate Graph and Data / Generando Grafo y data
    Name,var0,var1,var2,var3,nodes = random_graph(var0, var1, var2, var3)
    text = f"Semilla: {var1} {skip}Archivo: {var2} {skip}Iteración Inicial: {var0} {skip}Nodos: {var3} {skip}ID*: {nodes}"
    #Print graph data / Mostrar data del Grafo
    if(PRINT): print(text)
    #Tweet
    if(FLAG): create_tweet_media([Name],text, myData =True)
    #Delete Img / Borrar Imagen
    if(DELETE): os.remove(Name)

#Run de code / Correr código
if __name__ == "__main__":
    #Libs / librerias
    from apscheduler.schedulers.blocking import BlockingScheduler
    generate_graph(FLAG = True, DELETE = False)
    #Scheduler / planificador
    #Creation and job initialization / Creacion e inicio de trabajo
    scheduler = BlockingScheduler()
    job = scheduler.add_job(lambda: generate_graph(DELETE = False), 'interval', hours=2.22)
    scheduler.start() 
    scheduler.print_jobs()
    if(False):  scheduler.shutdown()