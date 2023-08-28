from flask import Flask, jsonify
from scrape.Journal import ISTOE
from flask_cors import CORS




app = Flask(__name__)
CORS(app, origins="http://172.10.1.67:4000")
app.debug = True

@app.route("/")
def Scra_New():   
    data = ISTOE()

    # Retorna a resposta como JSON
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
