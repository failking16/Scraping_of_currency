# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:50:23 2023

@author: jksls
"""

import subprocess

def update():
    cmd = ['scrapy','crawl','scrapping2']
    subprocess.run(cmd)