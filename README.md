# Book Review
This project purpose is to demonstrate the use of a document based database MongoDb and to perform 
Create, Read, Update and Delete (CRUD) operations on it within the Python Flask framework.<br>
The Books Review is a website where visitors can find Books of different genre's and categories such as biographies, fantasy, historical, thrillers, horror,and sport. They can also find reviews for Books and aswell add/edit reviews. Books can also be added and removed from the site


## Table of Contents
> - [Description](#description)
> - [Ux](#ux)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Testing](#testing)
> - [Deployment](#deployment)
> - [Credits](#credits)
> - [Acknowledgments](#Acknowledgements)

# Description
The Book Review website offers the visitors the facility to look at books of different genres. The visitor can select a book of interest on the site, the site will provide a book summary and details such as Author and book reviews, they can also filter the book list by selecting book category to return as booking listing by genre.  
The website is intended to be accessible on all type of devices:<br> mobile phone, tablet, laptop and desktop.

# UX
### Navbar:
A fixed navbar is used in the website for ease of navigation, in mobile view switches to a burger menu upon clicking displays navbar options. A visiting user to the site can intuitively access the different features of the site.

### Category Dropdown:
A user can view all uploaded books listing by Category Genre to suit specific user tastes.

### Strategy
The object of the website is to inform visitor of different Books, allow them to view book summary and reviews 

### Business Goals
*  External user goals: <br>
   The site’s user are visitors looking to find information on books of different interests. 
   They can view book summary and reviews so they can make an informed decision about purchasing books for themselves or for a gift for loved ones or friends. 

* Site owner's goal: <br>
   To offer a site which is intuitive, easy to use for users. Where visitors can effortlessly find books of interest type with 
    minimum effort.

## User Stories
* As a First Time Visitor: <br>
    “I  would like find a books and read other visitors book reviews ”

“I  would like to find book based on book review recommendations”

## Scope
This website incorporate Minimal Viable Product (MVP) elements.

   * Fullfills the needs of both the external user (visitors to the site) and business owner with features such as book review,

   * Website not cluttered with too much information. Book Information is clearly presented. Site is easy to navigate.

## Structure
The website comprises of three site pages. The page provides the visitor with Book listing showing book category, number of reviews on each book.
A button is provided for the listed book to view and add review. 


## Skeleton
In the main the wireframes more or less match my final project.
See links to relevent section of the wireframes below:

* home
    * Link: <a href="wireframes/wireframe_home_page.png" target="_blank" >Wireframe Home Page</a>
   
* Add Book
    * Link: <a href="wireframes/wireframe_add_book.png" target="_blank" >Wireframe Add Book Page</a>
    

* Delete Book
    * Link: <a href="wireframes/wireframes_delete_book.png" target="_blank">Wireframe Delete Book Page</a>
    
* View/Add Review 
    * Link: <a href="wireframes/wireframes_view_add_review.png" target="_blank">Wireframe View/Add Review Page</a>


##  Images
The images such as book covers also blended in well with the sites colour scheme.

## Colours
I choose sky blue as background colour for the site. For the navigation bar I choose a mild read colour. I feel this offers an easy on the eye
contrast.

## Typography
I used Google fonts to enhance some text sections of the site. I decided on Roboto with backup sans-serif for text headings on the home page.

# Features
  
  The site requires minimum input from the user<br>
    * Visitor/user on entering main site see list books showing book details such as book name, Author, category, how many reviews 
      have been added for the book and a button next to it to view and add review.<br>
    * Within the view and add review page, a book summary is provide and a list of submitted book reviews. There an a button to 
    submit a book review.<br>
    * A user can edit their reviews<br>
    * Other site features to upload Book details and delete existing books.<br>
    * In mobile view there a text prompt to swipe right for book listing so user can see full listing. This text prompt
      appears where a book category has more than one book<br>


# Technologies Used
The website is implemented using the Jinja template engine which allows for the use of 
Jinja templating logic along with the Flask framework in Python.

### Technologies:
* HTML
    * For basic website page structure / markup

* CSS3
    * CSS3 for styling the website pages aligning elements with padding, margins and I used Float for positioning elements 


* MaterializeCSS– to separate main pags of site into even grid sections. This allowed greater consistency in layout when interacting with site. 

* jquery
    * jQuery for MaterializeCSS initialization


* python/Flask
     * provides site logic, connect front end site to mongodb to allow site to view Books stored on mongo Database, add reviews and books.
       Delete Books.

* mongodb
     * To provide storage storage of Books details such as Book name, Category type, Book cover picture urls and Reviews 

* Font Googleapis
    *To provide Materialize icon for Add Book form fields
    
* Google Font
    * to make Paragraph Heading on Home page look clearer I used Roboto font-family referencing https://fonts.google.com/ CDN<br>
      in the style css.

Flask Modules used:

* render_template: This method is used for delivering the required page from the templates folder and the respective 
  template inheritance and Jinja templating logic.

* redirect: This method is used to redirect users to a different URL than the one requested as an aid to site navigation.

* url_for: This is used to generate a URL to a given endpoint and calls the respective Python function to be executed.

Flask PyPI import packages used:

* dnspython: This module is a DNS toolkit for Python. It is used for server queries and dynamic updates.

* flask-pymongo: This module is used as the interface with MongoDb for performing database CRUD operations


# Database Schema:
In this project in my MongoDB database is a simple setup of one Book document with the following fields:

| Field         | Data Type     |   Form Validation Type   | Required Field|
| ------------- |-------------  |:-------------------------|-------------:
| _id           | ObjectId      | Auto generated           | Yes
| book_name     | String        | Text                     | Yes
| Author        | String        | Text                     | Yes
| Number_of_Reviews     | Int32     | Text                | No
| book_cover     | String     | url              | Yes
| book_summary     |  String     | Text                | Yes
| Review     |  String Array     | Text                | No


# Testing
# Testing
Unit Testing:

* The python unittest module was used to derive to test the different app.py routes for app site.
* The following site Features were tested with unittest module in test_website.py:
1. Testing 200 ok response for the feature page
2. Testing you unique site page html tag to ensure correct page is returned in test to validate site route.

Test were run on site pages and features: 
  * /get_task -  Home page
  * /add_or_delete_bk - Add Book page
  * /delete_bk - Delete Book page
  * /get_biography - Biography Book listing page
  * /get_fantasy - Fantasy Book listing page
  * /get_history - History Book listing page

Test - Add Book:
* All Fields on the Add Book form are required and form will not submit the form information until
all the field are completed and the field input is the correct format.
Example:
* The Book Summary field has a mininmum length and user will receive a prompt if the input is less than the length.
* The Book Cover requires the input type to be a url and will prompt user if input is anything other than a url.
* The Book Category dropdown needs to be selected and will prompt user if no category is selected.


Manual Testing
CSS was tested by using Google Chrome Developer Tools to alter elements on the page.

This project was tested for display responsiveness using the following screen sizes.
1.	Large screen 
o	Desktop Chrome
o	Desktop Firefox

2.	Medium screen 
o	iPad Pro Safari
o	Desktop Chrome

3.	Small screen 
o	Phone Samsung 7
o	iPhone 6


Test Site validation:
* The site pages and code been validated using the following online validators - No errors were found.

1. W3C Validation Service
2. pep8online
3. jshint 



# Bugs and troubleshooting

1.	Materialize
Materialize styling library was more limited than other other frameworks such as Bootstrap.

2 Resizing of the navbar header was not reflected correctly for certain screen sizes . I had to implement a custom media query as a workaround

3 MongoDb altering/amending array content for the book collection Review field for the edit Review on book page proved timeconsumming - resolved issue by looking for nuggets of information in 3rd party mongodb site.

4. The Book cover field was original a text field causing caused issues as anything could be entered in this field it should only allow url type entries. Since this was not done originally any none url field enter caused console 404 error on loading the website GET https://djm-flask-book-review-test. get_tasks:178  herokuapp.com/Eiusmod%20pariatur%20Co 404 (NOT FOUND). This was due to a non url entry Book cover field.  The Book Cover field was changed to input type url and this error no longer occurred.

5. Add Book page Category field was originally a text field but this caused issues as anything could be entered in this field
   I wanted to make sure only a select type of categories could be entered. I create a select dropdown where only a select amount of topic could entered. 



# Deployment
Local git repository was initated in the begining of this project, gitpod and IDE  was used to write the code for this project and regular commits 
were done throughout the site development and were pushed to remote repository on https://github.com<br>
My project GitHub repository can be found here: https://github.com/djmolloy57/proj_book

Deployment procedure to implement new functionality
1.	Go to project repository above and create a new upstream branch or raise an issue, this will also create an upstream branch.
2.	Open this branch or issue in code editor. For this project GitPod was used.
3.	Add and commit code to this branch until satisfied code can be merged with the main branch.
4.	Send a pull request to GitHub requesting the branch can be merged.
5.	If there are no conflicts raised this branch or issue can then be closed by performing a merge onto the main branch. A merge can also be performed from GitPod.
6.	This GitHub repository master branch is automatically connected to Heroku through Heroku settings so any merges to the GitHub master branch are automatically deployed and built in Heroku.

Deployment procedure to clone this project
1.	Go to project repository above and click 'Code' button
2.	Copy the url 
3.	In your code editor have the following installed:
o	Git
o	pip3
o	dnspython
o	flask
o	flask-pymongo
o	flask-wtf
o	flask cloudinary
These are installed from the Python Package Index (PyPI) repository.
4.	Install the cloned repository by running the code snippet copied above.
5.	Create a requirements.txt file by running:
    pip3 freeze --local > requirements.txt

Connect to MongoDb
1.	In MongoDb click on the connect button on the cluster you wish to connect to and copy the connection string provided.
2.	Create an env.py file to contain the MONGO_URI connection string. Correct the 'dbname' and 'password' values in the connection string to the correct values.
3.	Add this env.py file to .gitignore.
4.	This program can now be run locally by running the command: 
    o	python3 run.py

To connect to Heroku
1.	Create a Procfile to initiate the Heroku web dyno. echo web: python3 run.py > Procfile
2.	In your Heroku App go to Settings and Reveal Config Vars.
3.	Configure the variables as: 
KEY	VALUE
IP	0.0.0.0
PORT	5000
MONGO_URI	mongodb+srv://root:Rifoll30@projmyfirstcluster.bldqs.mongodb.net/MyFirstDB?retryWrites=true&w=majority
SECRET_KEY	<secret_key>
To deploy to Heroku from GitHub master branch
1.	In your Heroku App go to Deploy tab.
2.	Choose the deployment method, choose GitHub.
3.	Enter the repository name and GitHub password.
4.	Click deploy from master branch.
5.	This setting can be automated so any new merges to the GitHub master branch will automatically redeploy and   build on Heroku Apps.

# Feature would like:
  Recommended Book section. A search book bar

# Credits

## Media
    
   
## Acknowledgements

   * Nav menu and book upload page borrowed from Mini Project Task Manager.
    
   * Got helpful hints on solving issue from https://stackoverflow.com/
