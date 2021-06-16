# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 15:56:37 2021

@author: HRV
Test de apscheduler
"""


import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):    
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))

scheduler = BlockingScheduler()
# Run every minute job Method
scheduler.add_job(lambda: job("Avrss"), 'interval', minutes=1)
# In 2019-08-29 22:15:00 To 2019-08-29 22:17:00 Period, run every 1 minute 30 seconds job Method
scheduler.add_job(job, 'interval', minutes=1, seconds = 30, start_date='2021-03-01 16:00:00', end_date='2021-03-01 16:30:00', args=['job2'])

scheduler.start()
