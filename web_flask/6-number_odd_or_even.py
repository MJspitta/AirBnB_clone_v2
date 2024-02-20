#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ displays c followed by value of text """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ displays python followed by value of text """
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display n is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """ displays html if n is an int """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ displays html page if number """
    if isinstance(n, int):
        odd_even = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html',
                               n=n, odd_even=odd_even)
    else:
        return "Invalid input. Please provide an integer."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
