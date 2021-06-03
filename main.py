# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:03:38 2021

@author: S. Hiram Rubio
Script principal
"""

#Run de code / Correr código
if __name__ == "__main__":
    #Libs / librerias
    from apscheduler.schedulers.blocking import BlockingScheduler
    from BTVis import generate_graph
    # / Generar gráfica
    generate_graph(FLAG = True, DELETE = False)
    #Scheduler / planificador
    #Creation and job initialization / Creacion e inicio de trabajo
    scheduler = BlockingScheduler()
    job = scheduler.add_job(lambda: generate_graph(DELETE = False), 'interval', hours=2.22)
    scheduler.start() 
    scheduler.print_jobs()
    if(False):  scheduler.shutdown()