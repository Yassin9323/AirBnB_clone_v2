#!/usr/bin/python3

"""
    This is a script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_cities():
    return render_template(
        "7-states_list.html",
        states=storage.all(State)
    )


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
