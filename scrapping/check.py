# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:31:11 2023

@author: jksls
"""

import pandas as pd
import numpy as np
df          = pd.read_csv('Scraped.csv')
column_list = df.columns.tolist()
    
kf          = pd.DataFrame({column_list[1]:np.array(df.iloc[:,1])})
    
print(kf)