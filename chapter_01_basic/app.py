#############################
## The application start point
## Digital Diary chapter-1
## Codes are free to use in any form wished by the user; however;
## no warranty of any form implicit or explicit for the fitness of the code 
## to a specific situation is given.
#############################

## Our needed imports from Python and Flask
from flask import Flask
from flask.globals import request
from flask.helpers import send_from_directory, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
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
    ''' Our root/index route and corresponding templates. It is so far serving a static
    HTML as the dynamic things are yet to come in the next chapters.'''
    return render_template('index.html')

@app.route("/view/<diary_id>")
def view_entry(diary_id=None):
    ''' Function names are following the Google Python style guide '''
    ## Not using the diary ID here as of yet. Will come later
    return render_template('view_entry.html')

@app.route("/add/")
def add_entry():
    ''' This is to serve the add entry template. We did not make this
    as the point where the post data  will also come once the form is submitted'''
    return render_template('add_entry.html')

@app.route("/post_entry", methods=['POST'])
def post_entry():
    '''POST data from the form will come here. Notice that we have specified 
    methods (http VERB) which can access this route. If you are running this application
    locally, try hitting http://localhost:5000/post_entry and see what you get'''
    if request.method == 'POST':
        ## Eventually we will add the entry to DB here and then redirect.
        return redirect(url_for('index'))

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) ## This particular way of lunching the app is Heroku ready.
    app.run(host='0.0.0.0', port=port)