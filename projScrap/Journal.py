from requests import get 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

import json


chrome_options = Options()
chrome_options.add_argument("--headless") 
p = "/venv/chromedriver/"
driver = webdriver.Chrome(p +'\chromedriver.exe', options=chrome_options)


def default(url):
    

    page = get(url)


    soup = BeautifulSoup(page.content, 'html5lib')
    
    main = soup.findAll('div', attrs={'class':'.feed-post-body'})

    #titulo da noticias  - ok - text
    title_news_name = soup.findAll('a', attrs={'class':'gui-color-hover'})
    
    #img -- pega o link 
    img_group = soup.findAll('picture' , attrs={'class': 'bstn-fd-cover-picture'})
    
    
    link_group_news = soup.find('div' , attrs={'class': 'feed-media-wrapper'})


    links_news = link_group_news.findAll('a' , attrs={'class': 'feed-post-figure-link'})


    ## faz com que o browser não abra durante o processo
    ## caminho para o seu webdriver



    for a in link_group_news :
        print(": ",a.text , '\n')        


    #print(links_news)  

    # Usar .contents para pegar as tags <a> filhas
    #for title_news_name in group_titles:
    #    titles = title_news_name.contents[0]
    #    print(titles) 
    # 
    
    cont = 0
    for i in title_news_name :
        #print(cont,": ",i.text , '\n')        
        cont += 1




    #print("nomeee /n/n/n/n/n", title_news_name)
    return "title_news_name"
