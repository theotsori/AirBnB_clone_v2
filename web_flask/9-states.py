#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays a HTML page with a list of all State objects."""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id):
    """
    Displays a HTML page with a list of all City objects linked to a State
    object.
    """
    state = storage.get('State', id)
    if state is None:
        return render_template('9-not_found.html')
    else:
        return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
