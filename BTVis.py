# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19  2021

@author: S. Hiram Rubio
Codigo para generar plots aleatorio con 
base a la solucion con "Backtracking" en 
el problema de "n queens on board". Adicional
se cuenta con una funcion que busca trian- 
gulos en el plot y genera una segunda ima-
gen con estos resaltados. 

Code to generate random plots base on the
Backtracking solution of the problem:
    n queens on board. Additionally, there 
is a function that searches for triangles in 
the plot and generates a second image with 
these highlights.
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
    lines = []
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
        #Save line / guardo linea
        lines.append(([rpnt[0],rpnt2[0]],[rpnt[1],rpnt2[1]]))
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
    
    return Name,var0,var1,var2,var3,nodes,lines

#Funcion para pasar de puntos a lineas usando funcion de shapely
def list_to_lines(listP):
    #Libs / librerias
    from shapely.geometry import LineString
    
    Newlist = []
    for element in listP:
        x = LineString([(element[0][0],element[1][0]),(element[0][1],element[1][1])])
        Newlist.append(x)
    return Newlist 

#Funcion para plotear linea
def plot_line(ax, ln):
    x, y = ln.xy
    ax.plot(x, y, color='k', alpha=0.3, linewidth=2, solid_capstyle='round', zorder=0)
    
#Funcion para obtener los puntos de interseccion    
def inter_points(linesN, ax, PRINT = False, POINTS = False):
    #Libs / librerias
    import itertools
    from shapely.geometry import Point
    
    #Puntos de interseccion
    i_points = []
    #Genero todos los pares de líneas para buscar intercepciones.     
    for pair in itertools.combinations(linesN, 2):
        line1, line2 = pair[0], pair[1]
        #Genero punto de interseccion y reviso que sea nuevo
        int_pt = line1.intersection(line2)
        if(int_pt in i_points):
            None
        else:
            try:   
                point_of_intersection = Point(int_pt.x, int_pt.y)
                i_points.append(point_of_intersection)
                if(POINTS): ax.scatter(point_of_intersection.x,point_of_intersection.y, c = 'r', marker = 'o',edgecolor= 'k')
                if(PRINT):  print(f"Punto {len(i_points)}: {point_of_intersection}")
            except:
                None
    return i_points

#Funcion para buscar y pintar triangulos
def paint_trig(lines, Name, PRINT = False):
    #Libs / librerias
    from shapely.geometry import Polygon
    import matplotlib.pyplot as plt
    import itertools
    from descartes.patch import PolygonPatch
    #Plot / Grafica
    fig, ax = plt.subplots(figsize= (8,8))
    #Conversion a lineas 
    linesN = list_to_lines(lines)
    
    #Ploteo de las lineas.  
    for element in linesN:  plot_line(ax, element)
    
    #Todos los puntos de interseccion    
    i_points = inter_points(linesN,ax)
    
    #Paleta de colores parcial
    colors = ['#FF5733','r','c','y','m','g','b']   
    #Contador
    i = 0
    #Buscamos triangulos en base a los puntos de intersección y
    #a las líneas utilizadas
    if(len(i_points) >= 3):
        if(PRINT): print(f"------------Buscando triangulos-------------")
        #Poligonos usados
        Polyg = []
        #Hacemos todas las permutaciones de grupos de 3
        for group in itertools.permutations(i_points, 3):
            #Lineas usadas
            Polyg_l = []
            #Buscamos los pares de puntos
            for pair in itertools.combinations(group , 2):
                #Verificamos todas las lineas
                for line in linesN:
                    #Definimos tolerancia
                    d = 1e-14
                    #Buscamos lineas que tengan un intercepto y pasen cerca de otro punto. 
                    if( ( line.intersects(pair[0]) or (line.distance(pair[0]))<d) and (line.intersects(pair[1]) or (line.distance(pair[1])<d) )):
                       if (line not in Polyg_l):
                           Polyg_l.append(line)
            
            #Si las permutaciones son correctas, verificamos si el triangulo
            #esta contenido en otro ya dibujado, sino se agrega
            if(len(Polyg_l)==3):
                polygon = Polygon(group)
                if( (len(Polyg) == 0) or all( (e.contains(polygon) == False) for (e) in Polyg)):
                    patch = PolygonPatch(polygon, facecolor=colors[len(Polyg)%7], edgecolor='k', alpha=0.3, zorder=2)
                    ax.add_patch(patch)
                    Polyg.append(polygon)
                    i = i+1
                    
    #Plot text and axis / Texto y ejes
    ax.set_title(f"Found Triangles")
    ax.set_ylabel('Queens on board')
    ax.set_xlabel('Iterations')
    #ax.set_xlim(xmin = min(i)-0.5, xmax=max(i)+0.5)
    #ax.set_ylim(ymin=min(lbt)-0.5, ymax=max(lbt)+0.5)        
    fig.tight_layout()
    #Save / Guardando Imagen
    NameP = Name+"Trigs.png"
    if(i!= 0): fig.savefig(NameP)
    # / Cerrar imagen para evitar que se muestre
    #plt.close(fig)
    if(PRINT):  print(f"Triangulos: {i}") 
    return NameP, i


def generate_graph(var0 =-1, var1 = -1,var2=-1, var3=-1, FLAG = True, DELETE = True, PRINT = True):
    #Libs / librerias
    from tweet0 import create_tweet_media
    #from Test2 import paint_trig
    import os
    
    skip = "\n"
    #Generate Graph and Data / Generando Grafo y data
    Name,var0,var1,var2,var3,nodes,lines = random_graph(var0, var1, var2, var3)
    Name2, trigs = paint_trig(lines, Name )
    text = f"Semilla: {var1} {skip}Archivo: {var2} {skip}Iteración Inicial: {var0} {skip}Nodos: {var3} {skip}ID*: {nodes} {skip}Triangulos: {trigs}"
    #Print graph data / Mostrar data del Grafo
    if(PRINT): print(text)
    #Tweet
    if(FLAG): 
        if(trigs!=0):   create_tweet_media([Name, Name2],text, myData =True)
        else:           create_tweet_media([Name, Name2],text, myData =True)
    #Delete Img / Borrar Imagen
    if(DELETE): 
        os.remove(Name)
        os.remove(Name2)

#Test
if __name__ == "__main__":
    generate_graph(FLAG = False, DELETE = False)