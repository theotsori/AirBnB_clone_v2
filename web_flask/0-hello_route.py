#!/usr/bin/python3
"""
This module defines a Flask web application with a single route.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Defines a route that displays 'Hello HBNB!'."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
