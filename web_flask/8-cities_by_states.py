#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of all State objects sorted by name,
    along with a list of City objects linked to the State sorted by name.
    """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=states_sorted)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
