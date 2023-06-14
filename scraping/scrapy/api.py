from flask import Flask
import importlib

from spiders.scrpy import scrape_news


app = Flask(__name__)

@app.route("/scrapy")
def Hello():
    noticia = scrape_news()
    return noticia