#############################
## The application start point
## Digital Diary chapter-1
## Codes are free to use in any form wished; however;
## no warranty of any form implicit or explicit for the fitness of the code 
## in a specific situation is not given.
#############################

from flask import Flask
from flask.helpers import send_from_directory
from flask.templating import render_template
import os

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)


# Route Definitions
@app.route('/favicon.ico')
def favicon():
    ''' The favicon.ico file sent over the network using send_from_directory'''
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    ''' Something went wrong '''
    return render_template('404.html'), 404

@app.route("/")
def index():
    ''' Our root/index route and corresponding templates'''
    return render_template('index.html')

@app.route("/view/<diary_id>")
def view_entry(diary_id=None):
    ''' Function names are following the Google Python style guide '''
    ## Not using the diary ID here as of yet. Will come later
    return render_template('view_entry.html')

@app.route("/add/")
def add_entry():
    return 'The addition of diary entry'

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)