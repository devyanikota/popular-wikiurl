import requests
from bs4 import BeautifulSoup

link = raw_input("Enter the wikipedia link : ")
response = requests.get(link)
a = []

for link in BeautifulSoup(response.text, 'html.parser').find_all('a'):
    if link.has_attr('href'):
        sublink = link['href']
        print sublink
        if (sublink.startswith('/wiki/Wikipedia')):
            pass
        elif (sublink.startswith('/wiki')):
            new_link = (
                "https://en.wikipedia.org/wiki/Special:WhatLinksHere/"
                + sublink.split('/')[2]
                 )
            resp = requests.get(new_link)
            prev = 0
            for slink in BeautifulSoup(
              resp.text, 'html.parser').find_all('a'):
                count = 0
                if slink.has_attr('href'):
                    count += 1
                if count > prev:
                    l = slink
                else:
                    continue
            prev = count
print l
