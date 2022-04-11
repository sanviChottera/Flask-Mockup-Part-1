from flask import Flask, jsonify
import csv

all_movies = []
with open("movies.csv" , encoding='utf-8' )as f:
    r = csv.reader(f)
    data = list(r)
    all_movies = data[1:]

like_movies = []
unliked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome"

@app.route("/get-movies")
def get_movie():
    return jsonify({
        "data":all_movies[0], "status":"success"
    })


@app.route("/liked-movies", methods = ["POST"] )
def like_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    like_movies.append(movie)
    return jsonify({
         "status":"success"
    }),200

@app.route("/unliked-movies", methods = ["POST"] )
def unliked_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
         "status":"success"
    }),200

@app.route("/did-not-watch", methods = ["POST"] )
def did_not_watch_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
         "status":"success"
    }),200

if __name__ == "__main__":
    app.run(debug = True)