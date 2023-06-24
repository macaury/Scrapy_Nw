from flask import Flask,render_template
from Journal import default

app = Flask(__name__ , template_folder='template')


@app.route("/main")
def scrape():
   tots = "olaaa"

   return tots
   

from requests import get 
import json

@app.route("/teste")
def Scra_New():

   url = "https://g1.globo.com/"

   dados = default(url)


   return  dados
   #return render_template('home.html')


if __name__ == '__main__':
    app.run()