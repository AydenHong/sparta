from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'월-E'})
star = db.movies.find_one({'title':'월-E'})['star']

all_movies = list(db.movies.find({}))

for a in all_movies:
    if float(a['star']) > float(movie['star']) :
        print(a['title'])