from flask import Flask, jsonify
from Journal import ISTOE
from flask_cors import CORS
import os


app = Flask(__name__)
#CORS(app, origins="http://172.10.1.67:4000")
app.debug = True

@app.route("/" ,methods = ['GET'])
def Scra_New():   
    data = ISTOE()

    return data

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4000))
    app.run(debug=True,host='0.0.0.0',port=port ,debug=True)
