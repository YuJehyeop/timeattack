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
    # idx = request.form['idx_give']
    title = request.form['title_give']
    content = request.form['content_give']
    # reg_date = request.form['reg_date_give']
    doc = {
        # 'idx': idx,
        'title': title,
        'content': content,
        # 'reg_date': reg_date
    }
    db.memos.insert_one(doc)
    return jsonify({"result": "post완료"})


@app.route('/post', methods=['GET'])
def get_post():
    memos = list(db.memos.find({}, {'_id': False}))
    return jsonify({'all_memos': memos})
    return {"result": "GET완료"}


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx = request.form['idx_give']
    db.memos.delete_one({'idx': idx})
    return {"result": "삭제 완료"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)