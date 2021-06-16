# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:29:25 2021

@author: HRV
"""

from shapely.geometry import LineString, Point, Polygon
import matplotlib.pyplot as plt
import itertools
from descartes.patch import PolygonPatch

#-----------------------------------------------------------------------------
#Funcion para pasar de puntos a lineas usando funcion de shapely
def list_to_lines(listP):
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
def inter_points(linesN, ax, PRINT = True, POINTS = False):
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
def paint_trig(lines, Name, PLOT0 = True, PRINT = True ):
    #Plot / Grafica
    fig, ax = plt.subplots(figsize= (8,8))
    #Conversion a lineas 
    linesN = list_to_lines(lines)
    
    #Ploteo de las lineas.  
    if(PLOT0):   
        for element in linesN:   
            plot_line(ax, element)
    
    #Todos los puntos de interseccion    
    i_points = inter_points(linesN,ax)
    
    #Paleta de colores parcial
    colors = ['#FF5733','r','c','y','m','g','b']   
    #Buscamos triangulos en base a los puntos de intersección y
    #a las líneas utilizadas
    if(len(i_points) >= 3):
        if(PRINT): print(f"------------Buscando triangulos-------------")
        i = 0
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
    fig.savefig(NameP)
    # / Cerrar imagen para evitar que se muestre
    #plt.close(fig)
                         
    if(PRINT):  print(f"Triangulos: {i}") 
    return NameP, i
#-----------------------------------------------------------

                     
# print(f"Triangulos: {i}")   
#lines = [([125, 111], [5, 3]), ([126, 111], [5, 3]), ([111, 124], [3, 4]), ([115, 125], [5, 5]), ([122, 121], [4, 3]), ([126, 122], [5, 4]), ([113, 124], [5, 4]), ([126, 125], [5, 5])]
#lines = [([437540, 437543], [7, 9]), ([437545, 437536], [10, 10]), ([437541, 437543], [8, 9]), ([437543, 437530], [9, 11]), ([437537, 437530], [10, 11]), ([437530, 437541], [11, 8])]
#lines = [([44, 35], [5, 4]), ([36, 40], [5, 2]), ([37, 29], [5, 5]), ([31, 38], [3, 6]), ([44, 31], [5, 3]), ([37, 34], [5, 5]), ([31, 33], [3, 5]), ([35, 29], [4, 5])]
#lines = [([31429, 31427], [6, 7]), ([31437, 31424], [7, 6]), ([31430, 31423], [6, 7]), ([31423, 31434], [7, 4]), ([31430, 31434], [6, 4]), ([31433, 31423], [3, 7]), ([31430, 31427], [6, 7]), ([31426, 31423], [8, 7]), ([31429, 31432], [6, 8]), ([31434, 31422], [4, 6]), ([31424, 31435], [6, 5]), ([31437, 31431], [7, 7]), ([31433, 31428], [3, 5]), ([31436, 31429], [6, 6]), ([31429, 31430], [6, 6]), ([31434, 31427], [4, 7]), ([31422, 31436], [6, 6]), ([31431, 31423], [7, 7])]
#lines = [([1718, 1725], [7, 6]), ([1732, 1728], [6, 5]), ([1731, 1729], [5, 6]), ([1731, 1724], [5, 5]), ([1727, 1719], [4, 2]), ([1722, 1733], [5, 7]), ([1719, 1731], [2, 5]), ([1733, 1722], [7, 5]), ([1721, 1724], [4, 5]), ([1729, 1732], [6, 6])]
#lines = [([721991, 721994], [9, 6]), ([721998, 721990], [10, 8]), ([721995, 721996], [7, 8]), ([721998, 721990], [10, 8]), ([721991, 721999], [9, 7]), ([721991, 721996], [9, 8]), ([721990, 721997], [8, 9]), ([721997, 721999], [9, 7]), ([721990, 721986], [8, 8]), ([721998, 721992], [10, 10]), ([721994, 721993], [6, 11]), ([721988, 721999], [9, 7]), ([721995, 721988], [7, 9]), ([721989, 721995], [10, 7]), ([721987, 721993], [9, 11]), ([721986, 721993], [8, 11]), ([721994, 721988], [6, 9])]
#[([1280, 1275], [8, 7]), ([1288, 1275], [6, 7]), ([1280, 1279], [8, 7]), ([1277, 1284], [5, 7]), ([1276, 1285], [8, 3])]
#Name = f"Imgs/BT_Random.png"
#Name2, polis = paint_trig(lines, Name )
if __name__ == "__main__":
    lines = [([31429, 31427], [6, 7]), ([31437, 31424], [7, 6]), ([31430, 31423], [6, 7]), ([31423, 31434], [7, 4]), ([31430, 31434], [6, 4]), ([31433, 31423], [3, 7]), ([31430, 31427], [6, 7]), ([31426, 31423], [8, 7]), ([31429, 31432], [6, 8]), ([31434, 31422], [4, 6]), ([31424, 31435], [6, 5]), ([31437, 31431], [7, 7]), ([31433, 31428], [3, 5]), ([31436, 31429], [6, 6]), ([31429, 31430], [6, 6]), ([31434, 31427], [4, 7]), ([31422, 31436], [6, 6]), ([31431, 31423], [7, 7])]
    Name = f"Imgs/TestP.png"
    Name2, polis = paint_trig(lines, Name )