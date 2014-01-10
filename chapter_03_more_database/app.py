#############################
## The application start point
## Digital Diary chapter-3
## Codes are free to use in any form wished by the user; however;
## no warranty of any form implicit or explicit for the fitness of the code 
## to a specific situation is given.
#############################

## Our needed imports from Python and Flask
from db import get_entries, get_entry
from flask import Flask, session
from flask.globals import request
from flask.helpers import send_from_directory, url_for, flash
from flask.templating import render_template
from werkzeug.utils import redirect
import db
import os

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
    entries = get_entries()
    if entries == None:
        entries = []
        flash("Opps! Somwthing went wrong!")
    return render_template('index.html',
                           entries=list(entries))

@app.route("/view/<diary_id>")
def view_entry(diary_id=None):
    ''' Function names are following the Google Python style guide '''
    ## NOW we are using diary_id. Should we call it entry_id instead?
    ## Notice, since this time it is a single entry we are type casting to dict
    entry = get_entry(diary_id)
    return render_template('view_entry.html',
                           entry=dict(entry))

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
    return render_template('add_entry.html', user_name=user_name)

@app.route("/post_entry", methods=['POST'])
def post_entry():
    '''POST data from the form will come here. Notice that we have specified 
    methods (http VERB) which can access this route. If you are running this application
    locally, try hitting http://localhost:5000/post_entry and see what you get'''
    if request.method == 'POST':
        ## Adding the data here and redirecting with proper flash message
        ret = db.add_entry(user_name=request.form['user_name'],
                        title=request.form['entry_title'],
                 date=request.form['entry_date'], entry=request.form['entry'])
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

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) ## This particular way of lunching the app is Heroku ready.
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' ## This secrect key to sign the cookie so that even user can see the session cookies they can not change them
    app.run(host='0.0.0.0', port=port)
