#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    from models.state import State
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
