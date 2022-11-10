#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def cities():
    return render_template('100-hbnb.html')


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
