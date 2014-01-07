#############################
## The application start point
## Digital Diary chapter-0
## Codes are free to use in any form wished by the user; however;
## no warranty of any form implicit or explicit for the fitness of the code 
## to a specific situation is given.
#############################

## Our needed imports from Python and Flask
from flask import Flask
import os

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)
## DO not send DEBUG=TRUE for a production level application. It shows the default web debug console for Flask

# Route Definitions
@app.route("/")
def index():
    ''' Our root/index route. This will print a simple Hello Flask! at 
    browser. To see, point to http://localhost:5000'''
    return "Hello Flask!"

@app.route("/hello/<name>")
def view_entry(name=None):
    ''' Function names are following the Google Python style guide '''
    ## Notice how we are passing a dynamic variable as a part of the URL/Route
    ## to see the output of this route point your browser to http://localhost:5000/hello/yourname
    ## replace the "yourname" part with anything you want and observe what happens.
    ## Also try visiting a url like - http://localhost:5000/hello (without the last part)
    return "Flask greets you - " + name + "!!"

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) ## This particular way of lunching the app is Heroku ready.
    app.run(host='0.0.0.0', port=port)