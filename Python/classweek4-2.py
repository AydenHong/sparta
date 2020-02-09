from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
samemovie = (movie['star'])

all_movies = list(db.movies.find({'star': samemovie}))

# db.movies.update_many({'star': samemovie},{'$set': {'star': 0}})

for a in all_movies:
    db.movies.update_one({'star': samemovie}, {'$set': {'star': 0}})
    print(a['star'])