Chapter 00
==========
We start here with the most basic flask project prossible. It does not interact with a DB and even it does not serve any HTML file, but, that said, going through this will teach us many important concept of Flask web framework. 

The pre-requisites:
------------------ 
* Python 2.x (this particular tutorial code is developed using 2.7.3)
* pip and virtualenv installed. (http://www.pip-installer.org/en/latest/installing.html, http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* Having access to a note-pad or similar text editor to edit/create files.(recommended Sublime Text2)
* Git versioning system. (http://git-scm.com/book/en/Getting-Started-Installing-Git)

Setup the environment:
---------------------
We will start by setting up a virtual environment for our development process. We will do that so that we do not mess with the system wide python install. 
	
	
	$ mkdir tutorials
	$ cd tutorials
	$ virtualenv venv 
	At this stage the virtualenv will print its statuts until it is finished. Let it finish.
	$ . ./venv/bin/activate
	(venv)$ pip install Flask gunicorn
	

This will install Flask and gunicorn (a WSGI http server. Flask comes with a development mode server but that is not game to be used in production. Though our tutorial will not be dealing with gunicorn's specific thing but this much of information is needed.)


	(venv)$ git clone https://github.com/rcshubhadeep/digital-diary.git
	(venv)$ ls
	

You should see the directory called digital-diary now.

 
	(venv)$ cd digital-diary/chapter_00_hello_world
	(venv)digital-diary/chapter_00_hello_world$ pip install -r requirements.txt
	
	 
These two lines are not absolutely compulsory but better to check that we have all the dependencies installed.
Congratulations!! you just cloned the code for the whole tutorial and mostly you are set up to rock!!

Start Exploring the project:
---------------------------
The directory digital-diary is divided into many small steps (“chapters”, we call them) and each chapter is a contained in itself project of Flask. This document will only explore the chapter_00_basic's content and directory structure. However, since this directory structure and file structure is followed over all the subsequent chapters we will not explain all those that we will explain here in the other documents. 

The Directory Structure:
-----------------------
Unfortunately when we are writing this document there is no standard way of generating a typical boilerplate code/dir for Flask unlike Django or Pyramid. So, everybody has the right to reorganize the dirs the way they want. What is followed here is based on the best practices and conventional standard. 
* app.py This is the main entry point for the application. Open up this file in the the text editor you are using and read the comments to understand it better
* Procfile In true sense this file has nothing to do with Flask. It is here to make this project ready to be deployed over Heroku. This actually lets the gunicorn take over the application instead of Flask's default server.
* requirements.txt This is again, not very necessary from a Flask prespective. This lists all the packages we need to run this particular project. Mostly because of Heroku.




Explaining app.py:
-----------------
Open up the file in a text editor and let us travel from the begning of the file.
The first few lines of the file looks like


	from flask import Flask
	from flask.globals import request
	from flask.helpers import send_from_directory, url_for
	from flask.templating import render_template
	from werkzeug.utils import redirect
	import os
	

This is where we are importing all the necessary modules from Flask and also the os package
 

	app = Flask(__name__)
	app.config.update(
	    DEBUG = True,
	)
	

This is where we are creating a Flask application object by calling Flask(__name__) The first argument is the name of the application’s module or package. This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.(http://flask.pocoo.org/docs/api/#flask.Flas

Few words about Route:
---------------------
A route is the way to tell Flask that which part of the code should be executed when we hit a URL. for an example in the app.py file 
you can see that the index method is decorated with a decorator @app.route("/") and this decorator tell Flask that when somebody hits
http://localhost:5000 call the index method.

Conclusion:
----------
When you read through the whole code and understand it and can run the application (python app.py) you should try to visit
http://localhost:5000 and see the result and also http://localhost:5000/hello/yourname (replace the yourname with anything you want)
Also, try to visit the same URL without the last yourname part and see what happens.
