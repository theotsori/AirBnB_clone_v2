#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """ Remove the current SQLAlchemy session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """ Display a list of all states """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=states_sorted)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """ Display a list of cities in a state """
    state = None
    for obj in storage.all(State).values():
        if obj.id == state_id:
            state = obj
            break
    if state is None:
        return render_template('9-not_found.html')
    cities = sorted(state.cities, key=lambda c: c.name)
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')