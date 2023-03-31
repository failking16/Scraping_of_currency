import datetime
import scrapy
import pandas as pd


class Scrapping2Spider(scrapy.Spider):
    
    name = "scrapping2"
    allowed_domains = ["finance.kapital.kz/"]
    start_urls = ["https://finance.kapital.kz/"]

    custom_settings={
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }

    def parse(self, response):
        
        rows = response.css('table.currencies-table tbody tr')
        day  = datetime.date.today()
        df   = pd.DataFrame(columns=( "Currency" , 'Sh.Curr' , "Value in "+str(day) , "Change in "+str(day) ))
        i=0
    
        for row in rows:
            
            data       = row.css('td span::text').getall()
            
            df.loc[len(df)] = [ data[0] , data[1] , data[2] , data[3] ]
            i+=1
            
            if(i==11):
                df.to_csv('scrapping\spiders\output.csv')
            
            #yield{
            #    "Currency"            : data[0],
            #    "Sh.Curr"             : data[1],
            #    "Value in "+str(day)  : data[2],
            #    "Change in "+str(day) : data[3],
            #}
        
