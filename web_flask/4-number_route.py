#!/usr/bin/python3
''' Script that starts a Flask Web Aplication '''

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def rerout():
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    return('C {}'.format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)
