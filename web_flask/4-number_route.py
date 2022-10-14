#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, abort
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    return 'Python %s' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
