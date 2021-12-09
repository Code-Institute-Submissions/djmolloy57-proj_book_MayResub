import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, Response)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import json
import sys
import logging

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

@app.route("/add_or_delete_bk" ,methods=['GET', 'POST'])
def add_or_delete_bk():

    if request.method == "POST":
       
        task = {
            "Category": request.form.get("Category"),
            "book_name": request.form.get("book_name"),
            "book_summary": request.form.get("book_summary"),
            "Author": request.form.get("Author"),
            "book_cover": request.form.get("book_cover"),
            "Number_of_Reviews": 0,
            "review": ""
        }
        added_new_rec = mongo.db.books.insert_one(task)
        if  added_new_rec:
            try:
        
                return Response(
                    response= json.dumps(
                        {"message":"added Book!!"}),
                    status=200,
                    mimetype="application/json"
            )

            except Exception as ex:
                print("*********")
                print(ex)
                print("******")
                return Response(
                    response= json.dumps(
                        {"message":"sorry cannot add record"}),
                    status=500,
                    mimetype="application/json"
            )
            return redirect(url_for("tasks"))
    
    return render_template('upload_delete_books.html')

  

#@app.route("/view_add_review/<name>")
#def view_add_review(name):
#    return render_template("view_add_review.html",task=name)
# used with <td><a class="waves-effect waves-light btn" href="{{ url_for('view_add_review') }">View/Add Reviews</a></td> in jinja for loop in tasks.html

@app.route('/view_add_review', methods=['GET', 'POST'])
def view_add_review():
    if request.method == 'GET':
        return render_template("view_add_review.html")

    if request.method == 'POST':
        book_id = request.form['book_id']
        book = list(mongo.db.books.find({"_id" : ObjectId(book_id)}))
        
        return render_template("view_add_review.html", bk=book)

@app.route("/write_review", methods=['GET','POST'])
def write_review():  
    if request.method == 'GET':
        return render_template("write_review.html")

    if request.method == 'POST':
        bookid = request.form['bookid']
       
        return render_template("write_review.html", bkid=bookid)

@app.route("/submit_review", methods=['GET','POST'])
def submit_review():
    if request.method == 'POST':
        bkid2 = 7590
        bkid = request.form['bkid']
        print('HHIIIIIIIIIIIIIII', file=sys.stderr)
        app.logger.warning('testing warning log')
        app.logger.error('testing error log')
        app.logger.info('testing info log')
        bookreview = request.form['writeReviewForm']
        review_add_id = mongo.db.books.find({"_id" : ObjectId(bkid)})
        if  review_add_id:
            try:
                #got the update review array using $push from site https://docs.mongodb.com/manual/reference/operator/update/push/
                dbResponse = mongo.db.books.update_one({"_id" : ObjectId(bkid)},{"$push" : {"review": bookreview}})
                return Response(
                    response= json.dumps(
                        {"message":"added review!!"}),
                    status=200,
                    mimetype="application/json"
            )

            except Exception as ex:
                print("*********")
                print(ex)
                print("******")
                return Response(
                    response= json.dumps(
                        {"message":"sorry cannot update record"}),
                    status=500,
                    mimetype="application/json"
            )
            return render_template("submit_review.html", bkid=review_add_id)
       

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

