from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbStock


## HTML 화면 보여주기
@app.route('/')
def home():
   return render_template('index.html')
#
# # # POST API 기본 코드
# # @app.route('/test', methods=['POST'])
# # def test_post():
# #    title_receive = request.form['title_give']  # 'title_give'로 가져온값 읽어줘봐
# #    print(title_receive)
# #    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
#
# GET(Read) API 기본코드
@app.route('/test', methods=['GET'])
def test_get():
    markets = list(db.codes.find({}, {'_id': False}))
    # for market in markets:
    #     print(market)
    return jsonify({'all_markets': markets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)