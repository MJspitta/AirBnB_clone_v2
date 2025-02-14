#!/usr/bin/python3
""" script that starts a Flask web application """

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays main hbnb filters page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exception):
    """remove current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
