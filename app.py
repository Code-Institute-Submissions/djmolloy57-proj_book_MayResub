import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.books.find())
    return render_template("tasks.html", tasks=tasks)

@app.route("/Recommended_bk")
def Recommended_bk():
    return render_template("recommended_books.html")

@app.route("/add_or_delete_bk")
def add_or_delete_bk():
    return render_template("upload_delete_books.html")

#@app.route("/view_add_review/<name>")
#def view_add_review(name):
#    return render_template("view_add_review.html",task=name)
# used with <td><a class="waves-effect waves-light btn" href="{{ url_for('view_add_review') }">View/Add Reviews</a></td> in jinja for loop in tasks.html

@app.route('/view_add_review', methods=['GET', 'POST'])
def view_add_review():
    if request.method == 'GET':
        return render_template("view_add_review.html")

    if request.method == 'POST':
        book_name = request.form['book_name']
        return render_template("view_add_review.html", task=book_name)



#@app.route("/")
#def hello():
#    return "Hello World .. again!"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

