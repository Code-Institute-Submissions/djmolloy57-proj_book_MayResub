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



# Deployment
Local git repository was initated in the begining of this project, gitpod and IDE  was used to write the code for this project and regular commits 
were done throughout the site development and were pushed to remote repository on https://github.com<br>
My project GitHub repository can be found here: https://github.com/djmolloy57/proj_book

# Feature would like:
  Recommended Book section. A search book bar

# Credits

## Media
    
   
## Acknowledgements

   * Nav menu and book upload page borrowed from Mini Project Task Manager.
    
   * Got helpful hints on solving issue from https://stackoverflow.com/
