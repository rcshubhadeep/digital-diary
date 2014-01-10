Chapter 03
==========

Extending from Chapter 04, we carry on where we left at chapter 03. We are going to add a privacy settings to our entries as the are diary entries. And we will apply a kind of Access Control (Who can see which entry?) based on the privacy field and presently session registered. 

The pre-requisites:
------------------ 
* Python 2.x (this particular tutorial code is developed using 2.7.3)
* pip and virtualenv installed. (http://www.pip-installer.org/en/latest/installing.html, http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* Having access to a note-pad or similar text editor to edit/create files.(recommended Sublime Text2)
* Git versioning system. (http://git-scm.com/book/en/Getting-Started-Installing-Git)
* MongoDB. (This is the NoSQL DB that we are going to use in this project to sore and operate on the DB. Please visit http://docs.mongodb.org/manual/installation/ and http://www.mongodb.org/) 

Setup the environment:
---------------------
There is nothing to setup if you are successfull until chapter 03

Start Exploring the project:
---------------------------
No new module/directory/package is introduced here

Explaining __init__.py file:
---------------------------
If we look carefully then we will see that the index function has got some new codes. Earlier we used to scan through the whole DB and get every document present.
But now, we are filtering them based on the user name and the privacy settings before we send them to the view.

Conclusion:
----------
When you are done looking into the code files and editing them and can run the app (python app.py) you should visit [http://localhost:5000] (http://localhost:5000) and put in your name in the text box at the top and hit “Go!”. 
In the add entry page you will see that we have a checkbox bellow the entry text area and now when you submit the entry check that. After you are done you will be redirected to the index page and you will not see any chaanges there.
Now, enter a different name in the top left text box at index page and hit Go!. Add an entry and comeback you are only seeing your own entery now all the others are vanished!! Privacy secured.
