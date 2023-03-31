# Scraping_of_currency

Languages : Python

Libraries : Pandas, Numpy, Scrapy, Subprocess


Scrapy is the library that can be used for web scrapping (taking values from sites)


Main Scripts of this project : Main_code.py , facts.py , Scrapping2.py

Main DataBases               : Scraped.csv , output.csv


Scritps explanation : 


Main_code.py : this script is a main code, that is the intermediate part between various function and user. 

facts.py     : this script is set of definitions every part of which is responsible for someparts (their names demonstrates it and every definition has its explanation 
in form of comments)

Scrapping.py : is the script that extracts data from finance.kapital.kz. 


DataBase explanation : 


Scraped.csv : is a database that is used to store data for future analyse. 

output.csv  : is a database that is used to store data, that were scraped from the site and then this data will be transfered into Scraped.csv file


This script updates and saves the table for analyse of currencies related to Tenge.
