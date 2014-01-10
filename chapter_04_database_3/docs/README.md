Chapter 03
==========

Extending from Chapter 04, we intorduce some more advanced DB related operations and dynami HTML generation here.

The pre-requisites:
------------------ 
* Python 2.x (this particular tutorial code is developed using 2.7.3)
* pip and virtualenv installed. (http://www.pip-installer.org/en/latest/installing.html, http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* Having access to a note-pad or similar text editor to edit/create files.(recommended Sublime Text2)
* Git versioning system. (http://git-scm.com/book/en/Getting-Started-Installing-Git)
* MongoDB. (This is the NoSQL DB that we are going to use in this project to sore and operate on the DB. Please visit http://docs.mongodb.org/manual/installation/ and http://www.mongodb.org/) 

Setup the environment:
---------------------
There is nothing to setup if you are successfull until chapter 02

Start Exploring the project:
---------------------------
No new module/directory/package is introduced here

Explaining __init__.py file:
---------------------------
We have already explained the basics of DB and session in the last chapter, here, I would like to concentrate on one single fact
If we see line our same old index() method now we will see that the method has changed. It is now callin a function from db package
called get_entries. This function gives us the list of all entries from the DB. We collect it and send it to the template for it to render those entries.

Explaining index.html file:
--------------------------
If we see this file then we will notice all the static HTML code for hardcoded entries are gone. And we will notice that we are
writing some kind of for loop inside the template. Everything in between

	{% for entry in entries %}
	{% endfor %}
	
is going to be repeated the number of times this loop willl run. That is how, with one single block of HTML we can generate the HTML
for all the entries in the system. This is the beauty and power of templating. We can insert logical blocks inside HTML which the template engine takes care of before it sends the template to the browser as a pure HTML file.

Conclusion:
----------
When you are done looking into the code files and editing them and can run the app (python app.py) you should visit [http://localhost:5000] (http://localhost:5000) and put in your name in the text box at the top and hit “Go!”. 
You will be redirected to the index page once you hit submit in the add entry page. And BOOM! you can see your newly created entry along with all the other entries in the system.
