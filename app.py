from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStocks

def home():
   return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']  # 'title_give'로 가져온값 읽어줘봐
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.dbStocks.find({}, {'_id': False}))
    return jsonify({'all_articles':articles})