from flask import Flask, render_template
from Journal import G1,ISTOE

app = Flask(__name__ , template_folder='template')
app.debug = True  

@app.route("/main")
def scrape():
   tots = "olaaa"

   return tots
   

from requests import get 
import json

@app.route("/teste")
def Scra_New():


   dados = ISTOE() 
   
   #dados = G1()

   

   return  dados
   #return render_template('home.html',dados)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)