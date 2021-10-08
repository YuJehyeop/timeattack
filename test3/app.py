from datetime import datetime

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
    title = request.form.get('title')
    content = request.form.get('content')
    post_count = db.post.count()
    view_count = 0
    if post_count == 0:
        max_value = 1
    else:
        max_value = db.post.find_one(sort=[("idx", -1)])['idx'] + 1  # index값이 0부터 시작하므로 1씩 더해준다.

    post = {
        'idx': max_value,
        'title': title,
        'content': content,
        'reg_date': datetime.now(),
        'view_count': view_count
    }
    db.post.insert_one(post)
    return {"result": "success"}

@app.route('/post/view', methods=['POST'])
def like_star():
    name_receive = request.form['name']
    view = db.post.find_one({'title': name_receive})

    view_cnt = view['view_count']

    view_up = view_cnt + 1

    db.post.update_one({'title': name_receive}, {'$set': {'view_count': int(view_up)}})


@app.route('/post', methods=['GET'])
def get_post():
    posts = list(db.post.find({}, {'_id': False}).sort([("reg_date", -1)]))  # 최근 올린 글을 상위로 올려준다.
    for a in posts:
        a['reg_date'] = a['reg_date'].strftime('%Y.%m.%d %H:%M:%S')

    return jsonify({"posts": posts})

# @app.route('/post', methods=['MODIFY'])
# def delete_post():
#     title = request.args.get('title')
#     content = request.form.get('content')
#
#     db.post.update_one({'title': }, {'content': })
#     return {"result": "success"}


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx = request.args.get('idx')
    db.post.delete_one({'idx': int(idx)})
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)