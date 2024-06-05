#!/usr/bin/python3
"""
    This is a script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_test():
    """ func to print Hello HBNB !"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Func print HBNB in Web page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_C(text):
    """ Func print C with input in Web page """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_py(text):
    """ Func print Python with input in Web page """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def display_num(n):
    """ Function to display if n is a number """
    int(n)
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
