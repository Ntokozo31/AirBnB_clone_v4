#!/usr/bin/python3
""" Starts a Flash Web Application """
import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.route('/1-hbnb')
def hbnb():
    cache_id = uuid.uuid4()
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    return render_template('1-hbnb.html', cache_id=cache_id, states=states, amenities=amenities, places=places)
