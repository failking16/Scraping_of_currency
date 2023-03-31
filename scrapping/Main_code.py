# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:17:57 2023

@author: jksls
"""

import facts as fc

fc.update()

print('What do you want?\n 1. Current values \n 2. Comparison \n 3. History of all values')
x=int(input())
y=0

if(x==1):
    
    print(fc.last_value())
    
elif(x==2):
    
    x1=int(input('insert first date - '))
    y1=int(input('second date - '))
    print(fc.comparison(x1,y1))
    
elif(x==3):
    
    print(fc.demonstrate())
    x2 = input('What kind of currenct have you chosen? ---> ')
    print(fc.the_history(x2))
    
else: print('There is no such option, restart the program')