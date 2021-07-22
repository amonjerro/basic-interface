from flask import Flask, request
from pymongo import MongoClient
import os

app = Flask(__name__)
uri = os.environ['uri']
client = MongoClient(uri)


@app.route('/post',methods=['POST'])
def insert():
    params = request.form
    db = client['database']
    col = db['tweets']
    col.insert(params)
    return True,200

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello!',200

if __name__ == '__main__':
    app.run('0.0.0.0', PORT=PORT)