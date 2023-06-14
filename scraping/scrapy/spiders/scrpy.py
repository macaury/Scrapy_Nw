import tqdm
import requests
import scrapy

from scrapy import Selector



class scrape_news(scrapy.Spider):

    name = 'meuspider'
    start_urls = ['http://example.com']

    def parse(self, response):

            domain  = "g1.globo.com"
            url = "https://g1.globo.com"
            titulo  =  ".gui-color-hover a::text"
            noticia =  ".feed-post-body"
            img    =  ".bstn-fd-picture-image ::attr(srcset)"
            link    =  ".feed-post-figure-link ::attr(href)"



        # for domain, url in zip(domains, urls):
            response = requests.get(url)
            selector = Selector(text=response.text)
            
                #path_json_journal = "./journals/journal.json"

                #with open(path_json_journal, encoding='utf-8') as arquivo_json:
                    #dats = json.load(arquivo_json)
            data = domain
            noticia_rep = noticia
            titulo_rep = titulo
            img_rep = img
            link_rep = link
        
            count = 0
            noticias = []
        
            for noticia in selector.css(noticia_rep):
                titulo = noticia.css(titulo_rep).get().strip()
                imagem = noticia.css(img_rep).get()
                link = noticia.css(link_rep).get()

                noticia_dict = {'titulo': titulo, 'imagem': imagem, 'link': link}
                noticias.append(noticia_dict)

            print (noticias)

            return noticias
