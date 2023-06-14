import scrapy
from flask import jsonify

class CrawlGene(scrapy.Spider):
        name = "g1.globo"
        allowed_domains = ["g1.globo.com"]
        start_urls = ["https://g1.globo.com"]

        def parse(self, response):
            domain = "g1.globo.com"
            titulo = ".gui-color-hover a::text"
            noticia = ".feed-post-body"
            img = ".bstn-fd-picture-image ::attr(srcset)"
            link = ".feed-post-figure-link ::attr(href)"

            noticias = []

            for noticia_element in response.css(noticia):
                titulo = noticia_element.css(titulo).get().strip()
                imagem = noticia_element.css(img).get()
                link = noticia_element.css(link).get()

                noticia_dict = {'titulo': titulo, 'imagem': imagem, 'link': link}
                noticias.append(noticia_dict)

    
            return noticias
            
    
            

