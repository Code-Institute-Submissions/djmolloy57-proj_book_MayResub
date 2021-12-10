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

@app.route("/delete_bk")
def delete_bk():
    lists = list(mongo.db.books.find())
    return render_template("delete_book.html", lists=lists)

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

@app.route("/delete_book", methods=['POST'])
def delete_book():
    test1='inside start of delete book function'
    try:
        delbkid = request.form['book_id']
        dbResponse = mongo.db.books.delete_one({"_id" : ObjectId(delbkid)})
        #review_add_id = mongo.db.books.find({"_id" : ObjectId(bkid)})
        if dbResponse.deleted_count == 1:
            return Response(
                response= json.dumps(
                {"message":"book deleted"}),
                status=200,
                mimetype="application/json"
            )     
            return Response(
                response= json.dumps(
                {"message":"book not found"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        return Response( 
            response= json.dumps(
            {"message":"sorry cannot delete the book"}),
            status=500,
            mimetype="application/json"
        )
        return render_template("delete_book.html")
       

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

#@app.route('/check_selected' , methods=['GET','POST'])
#def check_selected():
#    global selected
#    post = request.args.get('post', 0, type=int)
    #getbkid = request.form['booksid']
#    return json.dumps({'selected post': str(post)})
    #return render_template("edited_review.html", poster=poster)   

@app.route("/check_selected", methods=['GET','POST'])
def check_selected():
    global selected
    getbkid = request.form['booksid']
    #if getbkid == 0:
    post = request.args.get('post', 0, type=int)
    return json.dumps({'selected post': str(post)});
    #return render_template("check_selected.html", poster=post)  


@app.route('/update/<id>' , methods=['GET', 'POST'])
def update(id):
    #friend_to_update = Friends.query.get_or_404(id)
    friend_to_update = id
    if request.method == "POST":
        #friend_to_update.name = request.form['name']
        try:
	    #db.session.commit()
            print(friend_to_update)
            return redirect('/friends')
        except:
            return "There was a problem updating that record"
    else:
        return render_template('update.html', friend_to_update=friend_to_update)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
