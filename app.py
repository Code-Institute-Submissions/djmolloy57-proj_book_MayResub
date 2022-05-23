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
    ''' this route function is on Site load or clicking on Navbar Home
        button which will return all database Book document record as book list
    '''
    tasks = list(mongo.db.books.find())
    return render_template("tasks.html", tasks=tasks)

@app.route("/get_biography")
def get_biography():
    ''' this route function 
        looks up Biography data set in DB
        returns the Biography book list
    '''
    result_bio = mongo.db.books.find({
    "Category" : { "$eq" : "Biography"}})
    return render_template("book_by_category.html", result_1=result_bio)


@app.route("/get_history")
def get_history():
    ''' this route function is triggered in by History in 
        Category Dropdown on main page looks up History data 
        set in DB returns the Fantasy book list
    '''
    result_hist = mongo.db.books.find({
    "Category" : { "$eq" : "History"}})
    return render_template("book_by_category.html", result_1=result_hist)

@app.route("/get_fantasy")
def get_fantasy():
    ''' this route function is triggered in by Fantasy in 
        Category Dropdown on main page looks up Fantasy data 
        set in DB returns the Fantasy book list
    '''
    result_fantasy = mongo.db.books.find({
    "Category" : { "$eq" : "Fantasy"}})
    return render_template("book_by_category.html", result_1=result_fantasy)

@app.route("/get_thriller")
def get_thriller():
    ''' this route function is triggered in by Thriller in 
        Category Dropdown on main page looks up Thriller data 
        set in DB returns the Thriller book list
    '''
    result_thriller = mongo.db.books.find({
    "Category" : { "$eq" : "Thriller"}})
    #if len(list(result_thriller))==0:
    #   result_thriller=" "
    return render_template("book_by_category.html", result_1=result_thriller)


@app.route("/delete_bk")
def delete_bk():
    ''' this route function which is triggered by menu Delete button
        returns the the delete book page
    '''
    lists = list(mongo.db.books.find())
    return render_template("delete_book.html", lists=lists)

    

@app.route("/add_or_delete_bk" ,methods=['GET', 'POST'])
def add_or_delete_bk():
    ''' this route function is triggered by the add book button 
        which gathers form data Add Book and insert it into the 
        Database document
        returns site main page
    '''

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
        
                flash("Book has been added")


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
            return redirect("/")
          
    
    return render_template('upload_delete_books.html')

  
@app.route('/view_add_review', methods=['GET', 'POST'])
def view_add_review():
    ''' this route function is trigger by click View/Add Review button
        returns the view/add review page
    '''
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
    ''' this route function is trigged by Delete Book Button 
        it retrieve the site page book id and looks up the id 
        in the Mongo DB document to delete
        returns the the delete book page
    '''
 
    try:
        delbkid = request.form['book_id']
        dbResponse = mongo.db.books.delete_one({"_id" : ObjectId(delbkid)})
        if dbResponse.deleted_count == 1:
            lists = list(mongo.db.books.find())
            return render_template("delete_book.html", lists=lists)
           
        
    except Exception as ex:
        print(ex)
        return Response( 
            response= json.dumps(
            {"message":"sorry cannot delete the book"}),
            status=500,
            mimetype="application/json"
        )
    


@app.route("/submit_review", methods=['GET','POST'])
def submit_review():
    ''' this route function 
        get the book id and the writeReviewForm field which is assigned
        to bookreview variable.
        and looks up the id in the Book Document in the DB
        and for that book id that bookvariable content to the Document
        review string array
        returns to main page
    '''
    if request.method == 'POST':

        bkid = request.form['bkid']
        bookreview = request.form['writeReviewForm']
        review_add_id = mongo.db.books.find({"_id" : ObjectId(bkid)})
        if  review_add_id:
            try:
                #got the update review array using $push from site https://docs.mongodb.com/manual/reference/operator/update/push/
                dbResponse = mongo.db.books.update_one({"_id" : ObjectId(bkid)},{"$push" : {"review": bookreview}})
               
                #flash("Review has been added")

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
 
            return redirect('/')



 
@app.route("/check_selected", methods=['GET','POST'])
def check_selected():
    global selected
    getbkid = request.form['booksid']
    #if getbkid == 0:
    post = request.args.get('post', 0, type=int)
    return json.dumps({'selected post': str(post)});

 
@app.route('/update/<id>/<review>' , methods=['GET', 'POST'])
def update(id,review):
    ''' this route function takes in two parameter
        book id and the amended review  
        looks up the id for particular book in the Mongo DB document and update
        the particular string array review to the new ammended review.
        return to main page

        
    '''

    review_bk_id = id
    review_bk_update = review
    review_bk_update1 = request.form.get("review")
    if request.method == "POST":
     
        review_bkid = mongo.db.books.find({"_id" : ObjectId(review_bk_id)})
        
        if review_bkid:
        
            try:
                
                print(review_bk_id)
                print(review_bk_update1)
                             
                mongo.db.books.update_one({'_id': ObjectId(id), 'review': review},{"$set": {"review.$": review_bk_update1}})
         
                #return redirect('/view_add_review')
                return redirect('/')
     
               
            except:
                return "There was a problem updating that record"
    else:
        return render_template('update.html', review_bk_id=review_bk_id, review_bk_update=review_bk_update)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
