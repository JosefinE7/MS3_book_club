import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Routing for index.html, about.html, contact.html and careers.html


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html", page_title="Profile")


@app.route("/add_book")
def add_book():
    return render_template("add_book.html", page_title="Add Book")


@app.route("/manage_genres")
def manage_genres():
    return render_template("manage_genres.html", page_title="Manage Genres")


@app.route("/get_books")
def get_books():
    books = mongo.db.books.find()
    return render_template("get_books.html", books=books)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
