Chapter 05
==========

Extending from Chapter 04, we are going to introduce the concept of basic Ajax communication
here in this chapter. We will add a searchbox in the index page and we will ask people to search
by user name and after that without reloading the page with the search result we will populate the 
result with data that we got from the server by calling a particular route with Ajax.
(To know more about Ajax, please visit - http://www.w3schools.com/ajax/) 

The pre-requisites:
------------------ 
* Python 2.x (this particular tutorial code is developed using 2.7.3)
* pip and virtualenv installed. (http://www.pip-installer.org/en/latest/installing.html, http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* Having access to a note-pad or similar text editor to edit/create files.(recommended Sublime Text2)
* Git versioning system. (http://git-scm.com/book/en/Getting-Started-Installing-Git)
* MongoDB. (This is the NoSQL DB that we are going to use in this project to sore and operate on the DB. Please visit http://docs.mongodb.org/manual/installation/ and http://www.mongodb.org/) 

Setup the environment:
---------------------
There is nothing to setup if you are successfull until chapter 04

Start Exploring the project:
---------------------------
No new module/directory/package is introduced here

Explaining app.py file:
----------------------
If we look into the file we will see that a new route has been introduced. This is called /search.
So, we will hit the route from our front end javascript as http://localhost:5000/search . We supply the corresponding
method with the user name on which we want to search and it calls the search_by_username function from the db package
which gives us a mongoDB cursor as the result and we iterate over that to make a list of documents and finally we use 
json.dumps method to transfer this structure into a valid json string and send it back as response. 

Explaining templates/index.html
-------------------------------
If we see this file we will notice that a whole new section of code has come here. We have put it under a script tag.
It uses normal vanilla jQuery and very simple in its approach. You can read the comments to understand the parts of it.
The main mechanism is to call the search route with the user name in each click of the search button and then getting back the reply and preparing the table rows dynamically and replace the already present table with that.
 
Conclusion:
----------
When you are done looking into the code files and editing them and can run the app (python app.py) you should visit [http://localhost:5000] (http://localhost:5000)
you will see a search box beside the home and add entry link. Try putting a user name there which does exist in the records and see the result.
Also try with a username that does not exist. 