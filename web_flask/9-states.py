#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display HTML page: list of all State objects present in DBStorage"""
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id):
    """Display HTML page: list of City objects linked to the State"""
    state = storage.get("State", id)
    if state is None:
        return render_template('9-not_found.html')
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """After each request remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
