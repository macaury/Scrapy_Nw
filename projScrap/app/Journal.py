
from requests import get

from bs4 import BeautifulSoup

from flask import jsonify

import json

def G1():
    cont = 0
    
    url = "https://g1.globo.com/"

    page = get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    logo_group = soup.find('h1' , attrs={'class': 'logo'})
    logo = logo_group.find('svg')
    print('\n\n',logo,'\nlogo\n')

    # Encontra todas as divs com a classe "_evt"
    divs_evt = soup.find('div', class_='_evt')

    # Itera sobre as divs "_evt"
    for div_evt in divs_evt:

    #procura a classe bastian-page 1
        divs_bastian_page = div_evt.find('div', class_='bastian-page', attrs={'data-index': '1'})
        
        # Itera sobre as divs "bastian-page" encontradas
        for div in divs_bastian_page:
            post_new = div.find_all('div', class_='bastian-feed-item')
            
            data = []

            for post in post_new:
                imgSrc = post.find('img')['src']
                div_text = post.find('h2').get_text()
                link = post.find('a')['href']
                
                # Cria um dicionário com os dados do post
                post_data = {
                    'img': imgSrc,
                    'div_text': div_text,
                    'link': link
                }

                # Adiciona o dicionário à lista de dados
                data.append(post_data )
                cont += 1

            # Converte a lista de dicionários em uma string JSON
            json_data = json.dumps(data,ensure_ascii=False)

    print('\n\n','scrape finalizado',cont,'\n\n')

    return jsonify("rodando \n",json_data)



############

def ISTOE():
    url = "https://istoe.com.br/"

    page = get(url)
    soup = BeautifulSoup(page.content, 'html5lib')

    div_main = soup.findAll('article', class_='destaque-principal', attrs={'name': 'ArticleThreeImage'})

    count = 0
    data = []

    for J in div_main:
        pathImg = J.find('img')['data-src']
        titulo = J.find('h1').get_text()
        pathLink = J.find('a')['href']

        post_data = {
            'img': pathImg,
            'div_text': titulo,
            'link': pathLink
        }
        data.append(post_data)
        count += 1

        if count == 8:
            break

    # Converte a lista de dicionários em uma string JSON
    json_data = json.dumps(data,ensure_ascii=False)

    print('\n\n', count, ' posts coletados\n\n')

    return (json_data)