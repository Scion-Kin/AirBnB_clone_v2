#!/usr/bin/python3
"""
starts a Flask web application
"""

import sys
import os
from flask import Flask, render_template

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '..')))
# This will add the parent directory name to sys.path
# This will help when this flask app is started from it's directory

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """routes a page with the states listed in alphabetical order"""
    from models import storage

    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    cities = sorted(list(storage.all("City").values()), key=lambda x: x.name)

    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
