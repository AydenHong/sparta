from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework_bootstrap.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
    # rank_give로 클라이언트가 준 rank을 가져오기 & 숫자변환
    title_receive = request.form['title_give']
    movie = db.movies.find_one({'title':title_receive},{'_id':0})
    movie_star = movie['star']


    # 해당 순위의 영화를 받은 score로 업데이트 해주기
    db.movies.update_many({'star': movie_star}, {'$set': {'star': 0}})

    # 다했으면 성공여부만 보냄
    return jsonify({'result': 'success'})

@app.route('/test', methods=['GET'])
def test_get():
    # rank_give로 클라이언트가 준 rank을 가져오기
    title_receive = request.args.get('title_give')

    # rank의 값이 받은 rank와 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    movie = db.movies.find_one({'title':title_receive}, {'_id': 0})
    star = movie['star']

    movies = list(db.movies.find({'star':star}, {'_id': 0}))

    titles = []

    for m in movies:
        titles.append(m['title'])

    # info라는 키 값으로 영화정보 내려주기
    return jsonify({'movies': titles})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)