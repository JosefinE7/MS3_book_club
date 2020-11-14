import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Routing and functions for all templates


@app.route("/")
def index():
    books = mongo.db.books.find()
    return render_template("index.html", books=books)


@app.route("/seach", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        books = list(mongo.db.books.find({"$text": {"$search": query}}))
        return render_template("index.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # Check if username already exists in db
    existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})

    if existing_user:
        flash("Username already exists!")
        return redirect(url_for("register"))

    register = {
        "username": request.form.get("username").lower(),
        "password": generate_password_hash(request.form.get("password"))
    }
    mongo.db.users.insert_one(register)

    # put the new user into 'session' cookie
    session["user"] = request.form.get("username").lower()
    flash("Registration Successful!")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", page_title="Log In")

    # check if username exists in db
    existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})

    if existing_user:
        # ensure hashed password matches user input
        if check_password_hash(
                existing_user["password"], request.form.get("password")):
            session["user"] = request.form.get("username").lower()
            flash("Welcome, {}".format(request.form.get("username")))
            return redirect(url_for("profile", username=session["user"]))
        else:
            # invalid password match
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    else:
        # username doesn't exist
        flash("Incorrect Username and/or Password")
        return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    # inserts new book into db
    if request.method == "POST":
        book = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_pages": request.form.get("book_pages"),
            "book_description": request.form.get("book_description"),
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book Add Successful!")
        return redirect(url_for("index"))

    genres = mongo.db.genres.find().sort("category_name", 1)
    return render_template("add_book.html", genres=genres)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_pages": request.form.get("book_pages"),
            "book_description": request.form.get("book_description"),
            "created_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Edit Successful!")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    genres = mongo.db.genres.find().sort("category_name", 1)
    return render_template("edit_book.html", book=book, genres=genres)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully deleted")
    return redirect(url_for("index"))


@app.route("/manage_genres")
def manage_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("manage_genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "GET":
        return render_template("add_genre.html")

    genre = {
        "genre_name": request.form.get("genre_name")
    }
    mongo.db.genres.insert_one(genre)
    flash("New Genre Added!")
    return redirect(url_for("manage_genres"))


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated!")
        return redirect(url_for("manage_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre, page_title="Edit Genre")


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Removed")
    return redirect(url_for("manage_genres"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
