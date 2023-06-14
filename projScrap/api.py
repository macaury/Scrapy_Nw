from flask import Flask


from rasp import run



app = Flask(__name__)
@app.route("/main")
def scrape():
   tots = run()

   return tots
   


