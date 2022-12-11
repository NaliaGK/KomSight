import newspaper
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

from bs4 import BeautifulSoup
import requests 

#get the link
def get_link(x):
    req = requests.get(x)
    soup = BeautifulSoup(req.text, 'lxml')
    a = soup.find_all('a',{'class':'paging__link paging__link--show'})
    link = []
    for x in a:
        link = x.get('href')
    return link

#get the article
def news(link):
    url_i = newspaper.Article(url="%s" % (link), language='id',keep_article_html = True)
    url_i.download()
    url_i.parse()
    return url_i.text, url_i.title

# def title(link):
#     url_i = newspaper.Article(url="%s" % (link), language='id',keep_article_html = True)
#     url_i.download()
#     url_i.parse()
#     return url_i.title

def getter(link):
    #place to put the link   
    # link = input('link :')      

    #grab the input link
    all_page_news = get_link(link)
    #place for article

    #grab article based on pages
    if len(all_page_news) == 0:
        article, title = news(link)
    else:
        article, title = news(all_page_news)

    #CLEAN
    #----baca juga----
    article = re.sub(r'[bB][Aa][cC][Aa] [jJ][uU][gG][aA][ ]*: .*', '', str(article))
    article = re.sub(r'\n[(]BACA JUGA: .*\n', '', str(article))

    #----any links----
    article = re.sub(r'https*\S+', ' ', str(article))

    # #---credits----
    # article = re.sub(r'[(]*Penulis[ ]*:[ ].*', '', str(x))
    # article = re.sub(r'[(]*Video Editor[ ]*:[ ].*', '', str(x))
    # article = re.sub(r'[(]*Penulis Naskah[ ]*:[ ].*', '', str(x))
    # article = re.sub(r'[(]*Narator[ ]*:[ ].*', '', str(x))
    # article = re.sub(r'[(]*Produser[ ]*:[ ].*', '', str(x))
    # article = re.sub(r'[(]*Music[ ]*:[ ].*', '', str(x))

    #---kompas---
    article = re.sub(r'.*\.[ ]*TV[ ]*[-–—][ ]*', '', str(article))
    article = re.sub(r'[\w ]*, K[Oo][mM][pP][Aa][sS]\.[ ]*com[ ]*[-–—][ ]*', '', str(article))
    article = re.sub(r'[\w ]*, K[Oo][mM][pP][Aa][sS][ ]*[-–—][ ]*', '', str(article))
    article = re.sub(r'K[Oo][mM][pP][Aa][sS]\.[ ]*com[ ]*[-–—][ ]*', '', str(article))
    article = re.sub(r'K[Oo][mM][pP][Aa][sS][ ]*[-–—][ ]*', '', str(article))
    article = re.sub(r'KompasProperti - ', '', str(article))
    article = re.sub(r'KOMPAS\/[A-Z ]+\b', '', str(article))

    #---slashes---
    article =  re.sub(r'\(\/\/\)', '', str(article))

    #---others----
    article = re.sub(r'TRIBUNTRAVEL.COM - ', '', str(article))
    article = re.sub(r'Sonora.ID - ', '', str(article))
    article = re.sub(r'OhayoJepang - ', '', str(article))

    #---time zone---
    article =  re.sub(r'.+ [\d]*:[\d]* WIB[ Penulis:]*[\n]*', '', str(article))
    article =  re.sub(r'Kompas.com.+ WIB ', '', str(article))
    article =  re.sub(r'ADVERTISEMENT [A-Z ]*', '', str(article))

    #---delete all white spaces---
    article =  re.sub(r'\n+', ' ', str(article))

    article = re.sub(r'Simak \w* selengkapnya .*', '', str(article))
    article = re.sub(r'Simak selengkapnya .*', '', str(article))
    article = re.sub(r'[ ]*Sumber[ ]*:.*', '', str(article))
    title = re.sub(r' Halaman all', '', str(title))
    return article, title

