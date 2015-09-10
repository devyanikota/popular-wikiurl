from flask import Flask
from flask import request
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route('/')
def pop_wiki_link():
    link = request.args.get('link')
    response = requests.get(link)
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
                maxcount, count = 0, 0
                for slink in BeautifulSoup(
                  resp.text, 'html.parser').find_all('a'):
                    if slink.has_attr('href'):
                        count += 1
                    if count > maxcount:
                        l = slink
                        maxcount = count
                    else:
                        pass
    return l

if __name__ == '__main__':
    app.debug = True
    app.run()
