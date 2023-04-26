# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:43:11 2023

@author: jksls
"""

import schedule 
import time
import facts as fc

schedule.every().day.at('13:50').do(fc.update)

while True:
    schedule.run_pending()
    time.sleep(1)