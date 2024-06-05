#!/usr/bin/python3
"""
    This is a script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
"""

from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """ Display html page with its DB """
    
    return render_template("7-states_list.html",
                           states=storage.all(State)
                           )


#Alpha932003**#

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
