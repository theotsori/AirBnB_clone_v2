#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list():
    """Display HTML page: list of all State objects present in DBStorage"""
    path = '9-states.html'
    states = storage.all(State)
    return render_template(path, states=states, id=id)

@app.teardown_appcontext
def teardown_db(exception):
    """After each request remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
