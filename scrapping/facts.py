# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 00:16:08 2023

@author: jksls
"""

import pandas as pd
import numpy as np
import datetime
import subprocess


def last_value():
    
    df          = pd.read_csv('Scraped.csv')
    last_column = len(df.columns)-1
    
    x   = np.array(df.iloc[:,last_column-1])
    y   = np.array(df.iloc[:,last_column])
    day = datetime.date.today()
    
    kf = pd.DataFrame({
        'Currency':np.array(df.iloc[:,1]),
        'Value in '+str(day):x,
        'Change in '+str(day):y
        })
    
    return kf


#This definition finds the last value of the currencies
    

def comparison(x,y):
    
    df          = pd.read_csv('Scraped.csv')
    columns     = (df.shape[1]-2)/2
    column_list = df.columns.tolist()

    x1 = (int(x)-2*int(x)-1)*2
    y1 = (int(y)-2*int(y)-1)*2
    
    if( int(x)>int(columns) or int(y) > int(columns) ):
        
        z='it is not possible to compare not enough data. Max data -> ' + str(columns)
        return z
    
    else:
        
        kf = pd.DataFrame({
            
            'Currency'      : np.array(df.iloc[:,1]),
            column_list[x1] : np.array(df.iloc[:,int(x1)]),
            column_list[y1] : np.array(df.iloc[:,int(y1)])
            
            })
        
        return kf
    
    
#This defintion is used to see the difference of the currencies on the diferent dates
    
    
def demonstrate():
    
    df          = pd.read_csv('Scraped.csv')
    column_list = df.columns.tolist()
        
    kf          = pd.DataFrame({column_list[1]:np.array(df.iloc[:,1])})
    
    return kf


#This function demosntates the short name of currencies


def the_history(curr):

    df          = pd.read_csv('Scraped.csv')
    df          = df.drop(df.columns[0],axis=1)
    x           = np.array(df.iloc[:,0])
    index       = np.where(x=='USD')[0][0]
    row         = df.iloc[index]
    return row
            
    
#This function shows all stored data about the chosen currency.
    

def update():
    
    cmd = [ 'scrapy' , 'crawl' , 'scrapping2' ] # I can also use cmd = ['scrapy','crawl','...','-o','... . csv']
    subprocess.run(cmd)
    
    df = pd.read_csv('scrapping\spiders\output.csv')
    cf = pd.read_csv('Scraped.csv')
    
    cf = cf.drop('Unnamed: 0',axis=1)   
    
    #last_column = len(df.columns)-1
    X   = np.array(df.iloc[:,3])
    y   = np.array(df.iloc[:,4])
    day = datetime.date.today()
    
    cf['Value in '+str(day)]  = X
    cf['Change in '+str(day)] = y
        
    cf.to_csv('Scraped.csv')
    
    df.drop(index=df.index,columns=None,inplace=True)
    df = df.rename(columns=lambda x: '')
    df.to_csv('scrapping\spiders\output.csv',index=False)
    
    
    #This fucntion is aimed to update main table, that contains whole data from the site 
    #and it is called 'Scraped'
    
    
    #from datetime import timedelta
    #from scrapy.crawler import CrawlerProcess
    #import scrapy
    #from scrapping.scrapping.spiders.scrapping2 import Scrapping2Spider

    #The commented above libraries could be used to run scrapy program, but it has one problem 
    #and it is related with rerunning the process, what means that we can use these libraries
    #and the First part commented code(1) from the 'update' function, when we will scrapy porject
    #once in a session
    
    
    # define the output file name
    #output_file = "output.csv"
    
    # create a new crawler process
    #process = CrawlerProcess(settings={
    #    "FEEDS": {
    #        output_file: {"format": "csv"}
    #    }
    #})
    
    # start the spider
    #process.crawl(Scrapping2Spider)
    
    # start the process
    #process.start()
    
    #First part of commented code(1) that can be used when u r using scrapy crawling process
    #only once in a session.