Chapter 06
==========

Extending from Chapter 05, We will be introducing update and delete operation here. As we have already made us
familiar with Ajax in the previous chapter we will use Ajax here to do that.

The pre-requisites:
------------------ 
* Python 2.x (this particular tutorial code is developed using 2.7.3)
* pip and virtualenv installed. (http://www.pip-installer.org/en/latest/installing.html, http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* Having access to a note-pad or similar text editor to edit/create files.(recommended Sublime Text2)
* Git versioning system. (http://git-scm.com/book/en/Getting-Started-Installing-Git)
* MongoDB. (This is the NoSQL DB that we are going to use in this project to sore and operate on the DB. Please visit http://docs.mongodb.org/manual/installation/ and http://www.mongodb.org/) 

Setup the environment:
---------------------
There is nothing to setup if you are successfull until chapter 05

Start Exploring the project:
---------------------------
No new module/directory/package is introduced here

Explaining app.py file:
----------------------
We have introduced two new JSON/AJAX route in the new version. See them at line 148 and 156 respectively.
They just return the status of the operation to the calling client. 

Explaining templates/view_entry.html
-------------------------------
Previously we have been using this file to just view things now we are adding the capability to edit and delete
into this also
* We have used a HTML5 specific attribute contenteditable="true" in the entry p tag. This makes the p tag editable automatically
* We have created a javascript block in the same file and using jQuery we are sending the request to the server and updating the view accordingly.
* We used both AJAX get (for delete) and AJAX post (for edit) in the process. Please see this file for details. 
Conclusion:
----------
When you are done looking into the code files and editing them and can run the app (python app.py) you should visit [http://localhost:5000] (http://localhost:5000)
Then click on any entry and go to the view page and then place your cursor over the entry text and click. You will
be able to edit the entry and then click Save to save the edit. And following the similar manner you can delete using the delete button.
