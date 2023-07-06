from requests import get 
from bs4 import BeautifulSoup

import json

def default(url):
    
    page = get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    
    
    #logo
    logo_group = soup.find('h1' , attrs={'class': 'logo'})
    logo = logo_group.find('svg')
    #print(logo)
    
    #titulo da noticias  - ok - text
    title_news_name = soup.findAll('a', attrs={'class':'gui-color-hover'})
    testee = soup.findAll('div',attrs={'class':'feed-post'})

    print(testee)

    cont = 0
    for p in testee:
        #link_news = p['href'] #pegando link da noticia
        #print(link_news) # printa o link
        #print(p.text,'\n') # printa o titulo 
        cont += 1
    
    
    #img -- pega o link 
    img_group = soup.findAll('img' , attrs={'class': 'bstn-fd-picture-image'})
    #for pathSource in img_group:
    #    imgSrc = img_group['src']
    #    print(imgSrc)

    print('\n\n', cont , 'posts coletados','\n\n')

    return "title_news_name"