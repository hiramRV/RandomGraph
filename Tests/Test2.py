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
def plot_line(ax, ln,color):
    x, y = ln.xy
    ax.plot(x, y, color=color, alpha=0.3, linewidth=2, solid_capstyle='round', zorder=0)

#Funcion para obtener la pendiente de una linea    
def m_line(line):
    y = line.xy[1]
    dy = y[0]-y[1]
    x = line.xy[0]
    dx = x[0]-x[1]
    if(dx==0.0):
        return dx/dy    
    else:
        return dy/dx
    
#Funcion para obtener los puntos de interseccion    
def inter_points(linesN, ax, PRINT = True, POINTS = True):
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
def paint_trig2(lines, Name, PLOT0 = True, PLOT1 = False, PRINT = False):
    #Plot / Grafica
    fig, ax = plt.subplots(figsize= (10,8))
    #Conversion a lineas 
    global linesN
    linesN = list_to_lines(lines)  
    if(PLOT0):   
        for element in linesN:   
            plot_line(ax, element,color='k')
    
    #Todos los puntos de interseccion    
    i_points = inter_points(linesN,ax)
    #Paleta de colores parcial
    from random import randint
    varC = randint(0,4)
    if(varC==0):    colors = ['#FF5733','#C7005D','#13F3D5','#FAE317','#E017FD','#83EC0A','#0677F9'] 
    if(varC==1):    colors = ['#4CAF50','#00E676','#00C853','#E8F5E9'] 
    if(varC==2):    colors = ['#FFF9C4','#FFF176','#FFEB3B','#FBC02D','#F57F17','#FFFF00']
    if(varC==3):    colors = ['#00B8D4','#00E5FF','#18FFFF','#84FFFF','#00838F']
    if(varC==4):    colors = ['#F8BBD0','#F48FB1','#FCE4EC','#F06292','#D81B60','#C2185B','#880E4F']
    
    #Contador
    i = 0
    global Polyg
    #Buscamos triangulos en base a los puntos de intersección y
    #a las líneas utilizadas
    if(len(i_points) >= 3):
        if(PRINT): print(f"------------Buscando triangulos-------------")
        #Poligonos usados
        Polyg = []
        global Polyg_l
        #Hacemos todas las permutaciones de grupos de 3
        for group in itertools.combinations(i_points, 3):
            #Lineas usadas
            Polyg_l = []
            global pair
            #Buscamos los pares de puntos
            for pair in itertools.combinations(group , 2):
                #Booleano
                Valid = False
                #Creamos una linea
                lineInter0 = LineString((pair[0],pair[1]))
                lineInter1 = LineString((pair[1],pair[0]))
                
                if (lineInter0 in linesN) and (Valid ==False): 
                    if(PLOT1): plot_line(ax, lineInter0, color='g')
                    lineInter = lineInter0
                    Valid = True
                    if (lineInter not in Polyg_l): Polyg_l.append(lineInter)
                    if(PRINT): print("Caso1")
                    
                if (lineInter1 in linesN) and (Valid ==False): 
                    if(PLOT1): plot_line(ax, lineInter1, color='y')
                    lineInter = lineInter1
                    Valid = True
                    if (lineInter not in Polyg_l): Polyg_l.append(lineInter)
                    if(PRINT): print("Caso2")


                if(Valid ==False):    
                    #Si las lineas no se contienen perfectamente, buscamos de forma alternativa con
                    #la pendiente y la funcion touches
                    for line in linesN:
                        #Definimos tolerancia
                        d = 1e-10
                        if(line.touches(lineInter0)) and (Valid ==False):
                            m1 = m_line(line)
                            m2 = m_line(lineInter0)
                            if( abs(m1-m2) <d) and ( (m1>0 and m2>0) or (m1<0 and m2<0)) : 
                                if(PRINT): print(f"Caso3 {m1}, {m2}")
                                lineInter = lineInter0
                                Valid= True
                                if(PLOT1): plot_line(ax, lineInter, color='r')
                                if (lineInter not in Polyg_l): Polyg_l.append(lineInter)
                                
                        elif(line.contains(lineInter0)) and (Valid ==False):
                            lineInter = lineInter0
                            if(PRINT): print(f"Caso3.2")
                            Valid= True
                            if(PLOT1): plot_line(ax, lineInter, color='r')
                            if (lineInter not in Polyg_l): Polyg_l.append(lineInter)
                                
                            
                        elif(line.touches(lineInter1)) and (Valid ==False):
                            m1 = m_line(line)
                            m2 = m_line(lineInter1)
                            if ( abs(m1-m2) <d) and ( (m1>0 and m2>0) or (m1<0 and m2<0)): 
                                if(PRINT): print(f"Caso4 {m1}, {m2}")
                                lineInter = lineInter1
                                # print("Valid****")
                                Valid= True
                                if(PLOT1): plot_line(ax, lineInter, color='r')
                                if (lineInter not in Polyg_l): Polyg_l.append(lineInter)
                                
                        elif(line.contains(lineInter1)) and (Valid ==False):
                            if(PRINT): print(f"Caso4.2")
                            lineInter = lineInter1
                            Valid= True
                            if(PLOT1): plot_line(ax, lineInter, color='r')
                            if (lineInter not in Polyg_l): Polyg_l.append(lineInter)
                                
            #Si las permutaciones son correctas, verificamos si el triangulo
            #esta contenido en otro ya dibujado, sino se agreg
            if(len(Polyg_l)==3):
                if( abs(m_line(Polyg_l[0]) - m_line(Polyg_l[1]))<1e-5 or abs(m_line(Polyg_l[0]) - m_line(Polyg_l[2]))<1e-5): 
                    if(PRINT): print("\nLineas paralelas")
                    if(PRINT): print(m_line(Polyg_l[0]))
                    if(PRINT): print(m_line(Polyg_l[1]))
                    if(PRINT): print(m_line(Polyg_l[2]))
                    pass
                else:
                    polygon = Polygon(group)
                    if( (len(Polyg) == 0) or all( (e.contains(polygon) == False) for (e) in Polyg)) and (True):
                        patch = PolygonPatch(polygon, facecolor=colors[len(Polyg)%len(colors)], edgecolor='k', alpha=0.3, zorder=2)
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
                         
    if(True):  print(f"Triangulos: {i}") 
    return NameP, i
#-----------------------------------------------------------

if __name__ == "__main__":
    # lines = [([295161, 295169], [8, 8]), ([295164, 295162], [6, 9]), ([295167, 295164], [9, 6])]
    lines = [([732867, 732860], [8, 12]), ([732865, 732859], [9, 11]), ([732864, 732869], [8, 9]), ([732864, 732867], [8, 8]), ([732869, 732862], [9, 6]), ([732859, 732871], [11, 10]), ([732857, 732861], [9, 9]), ([732867, 732871], [8, 10]), ([732868, 732858], [8, 10]), ([732869, 732866], [9, 9]), ([732868, 732870], [8, 9])]
    # lines = [([115749, 115742], [9, 8]), ([115754, 115748], [6, 9]), ([115756, 115752], [8, 10]), ([115743, 115753], [9, 5]), ([115752, 115749], [10, 9]), ([115754, 115748], [6, 9]), ([115744, 115751], [10, 9]), ([115742, 115747], [8, 8]), ([115754, 115747], [6, 8])]
    # lines = [([31429, 31427], [6, 7]), ([31437, 31424], [7, 6]), ([31430, 31423], [6, 7]), ([31423, 31434], [7, 4]), ([31430, 31434], [6, 4]), ([31433, 31423], [3, 7]), ([31430, 31427], [6, 7]), ([31426, 31423], [8, 7]), ([31429, 31432], [6, 8]), ([31434, 31422], [4, 6]), ([31424, 31435], [6, 5]), ([31437, 31431], [7, 7]), ([31433, 31428], [3, 5]), ([31436, 31429], [6, 6]), ([31429, 31430], [6, 6]), ([31434, 31427], [4, 7]), ([31422, 31436], [6, 6]), ([31431, 31423], [7, 7])]
    # lines = [([576997, 576989], [10, 9]), ([576992, 576997], [5, 10]), ([576996, 576998], [9, 11]), ([576995, 577002], [8, 7]), ([576995, 576996], [8, 9]), ([576995, 576997], [8, 10]), ([576993, 576992], [6, 5]), ([576993, 577001], [6, 8]), ([577003, 576993], [8, 6]), ([576996, 577002], [9, 7]), ([576998, 576996], [11, 9]), ([576996, 577001], [9, 8]), ([576993, 576998], [6, 11]), ([577003, 576990], [8, 10]), ([576998, 576993], [11, 6]), ([576991, 576992], [4, 5]), ([576990, 576989], [10, 9]), ([577002, 576995], [7, 8]), ([576997, 577004], [10, 9])]
    Name = f"TestP"
    Name2, polis = paint_trig2(lines, Name )