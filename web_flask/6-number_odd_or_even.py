#!/usr/bin/python3
"""
This module defines a Flask web application with two routes
"""
from flask import Flask, render_template, escape, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Define a route that displays 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Defines a route that displays 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Defines route to c and custom text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays 'Python' followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Number page """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Number_template page """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Route to display HTML page only if n is an integer """
    if n % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
