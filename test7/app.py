from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    content = request.form.get('content')
    post = {
        'content': content
    }
    db.post.insert_one(post)
    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    posts = list(db.post.find({}, {'_id': False}))  # 최근 올린 글을 상위로 올려준다.
    return jsonify({"posts": posts})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
