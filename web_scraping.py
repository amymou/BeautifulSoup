#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:50:04 2019

@author: Amy
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(),'html.parser')

#divs = soup.find('div',{'class':'featured'})
#print(divs)
"""this strips away the tags leaving us with only text
   try using this as the last step
"""
#featured_header = soup.find('div', {'class':'featured'}).h2
#print(featured_header.get_text())

#for button in soup.find(class_='button button--primary'):
#    print(button)

for link in soup.find_all('a'):
    print(link.get('href'))
    