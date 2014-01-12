#############################
## The application start point
## Digital Diary chapter-4
## Codes are free to use in any form wished by the user; however;
## no warranty of any form implicit or explicit for the fitness of the code 
## to a specific situation is given.
#############################

## Our needed imports from Python and Flask
from db import get_entries, get_entry, search_by_username
from flask import Flask, session, jsonify
from flask.globals import request
from flask.helpers import send_from_directory, url_for, flash
from flask.templating import render_template
from werkzeug.utils import redirect
import db
import json
import os
from bson import json_util

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)
## DO not send DEBUG=TRUE for a production level application. It shows the default web debug console for Flask

# Route Definitions
@app.route('/favicon.ico')
def favicon():
    ''' The favicon.ico file sent over the network using send_from_directory'''
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    ''' Something went wrong. Normal 404 page.
    Notice that the status returned with the template '''
    return render_template('404.html'), 404

@app.route("/")
def index():
    ''' Our root/index route and corresponding templates. Notice the new codes here. 
    We are searching and getting all the entries from the DB and displaying them.
    One more thing to notice is that we are typecasting the default pymongo return to
    list before we pass it to the template.'''
    try:
        if session['name'] != '':
            user_name = session['name']
    except:
        user_name = 'default'
        session['name'] = 'default'
    entries = get_entries()
    if entries == None:
        entries = []
        flash("Opps! Somwthing went wrong!")
    init_entries = list(entries)
    final_entries = []
    for entry in init_entries:
        if entry['user'] == user_name: ## If it is our current user's entry
            final_entries.append(entry) ## The the entry whatever the private settings is
        else:
            if 'is_private' in entry and entry['is_private'] == False: ## Not our current user? Check for privacy settings
                final_entries.append(entry)
                
    return render_template('index.html',
                           entries=final_entries,
                           home_page=True) ## No need to typecast it again as a list. it is already a list

@app.route("/view/<diary_id>")
def view_entry(diary_id=None):
    ''' Function names are following the Google Python style guide '''
    ## NOW we are using diary_id. Should we call it entry_id instead?
    ## Notice, since this time it is a single entry we are type casting to dict
    ## ****Also make a note of that, we are not checking the privacy settings when we
    ## retrive single entry based on the ID. as we assume that no entry which is 
    ## private and created by another user than the current user, will not be shown
    ## in the index page itself. So, it is out of question for somebody who does not own
    ## an entry to navigate to this view page to view that entry if that entry is private.*****
    entry = get_entry(diary_id)
    return render_template('view_entry.html',
                           entry=dict(entry),
                           home_page=False)

@app.route("/add/")
def add_entry():
    ''' This is to serve the add entry template. We did not make this
    as the point where the post data  will also come once the form is submitted'''
    user_name = ''
    try:
        if session['name'] != '':
            user_name = session['name']
    except:
        user_name = 'default'
        session['name'] = 'default'
    return render_template('add_entry.html', user_name=user_name,
                           home_page=False)

@app.route("/post_entry", methods=['POST'])
def post_entry():
    '''POST data from the form will come here. Notice that we have specified 
    methods (http VERB) which can access this route. If you are running this application
    locally, try hitting http://localhost:5000/post_entry and see what you get'''
    if request.method == 'POST':
        ## Adding the data here and redirecting with proper flash message
        is_private = False
        if 'private' in request.form and request.form['private'] == 'Y':
            ## Python evaluates the if condition from Left to Right. 
            is_private = True
        ret = db.add_entry(user_name=request.form['user_name'],
                        title=request.form['entry_title'],
                 date=request.form['entry_date'], entry=request.form['entry'],
                 private=is_private)
        if ret == True:
            flash('Entry successfully added -- ' + session['name'])
            return redirect(url_for('index'))
        else:
            flash("Opps! Somwthing went wrong!")
            return redirect(url_for('index'))       

@app.route("/post_name", methods=['POST'])
def post_name():
    '''This is our place to enter the name in the DB.'''
    if request.method == 'POST':
        name = request.form['person_name']
        session['name'] = name
        return redirect(url_for('add_entry'))

@app.route("/search")
def search_json():
    '''This is a JSON route. This kin of routes are normally called from a Ajax call.
    Instead of returning a template it returns a json string to the calling client
    (here our browser.). Notice the return statement carefully.
    Also notice the comment above it'''
    ## In production systems it can be sometimes required that you authenticate here
    ## as a valid client to the system. But that is a pretty advanced concept and
    ## can be discussed later.
    final_resp = []
    usr = request.args.get('username')
    ret_val = search_by_username(usr)
    for document in ret_val:
        final_resp.append(document)
    ## This function bellow transforms a list of dicts or a single dict into a valid JSON string
    ## The second parameter is given from pymongo's bson.json_util module
    ## It helps this function to treat the datetime and ObjectId objects properly.
    return json.dumps(final_resp, default=json_util.default) 

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) ## This particular way of lunching the app is Heroku ready.
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' ## This secrect key to sign the cookie so that even user can see the session cookies they can not change them
    app.run(host='0.0.0.0', port=port)
