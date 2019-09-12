#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:03:10 2019

@author: Amy
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

import  re

site_links = []

def internal_links(linkURL):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'.
                   format(linkURL))
    
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup.find('a', href=re.compile('(.html)$'))

if  __name__ =='__main__':
    urls = internal_links('index.html')
    
    while len(urls) > 0:
        if page not in site_links:
            site_links.append(page)
            print(page)
            print('\n================\n')
            urls = internal_links(page)