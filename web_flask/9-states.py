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


@app.route('/states', strict_slashes=False)
def states_only():
    ''' makes an endpoint with all states in the database '''
    from models import storage
    from models.state import State

    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)

    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """makes an endpoint with the states listed in alphabetical order"""
    from models import storage
    from models.state import State
    from models.city import City

    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    state = {}
    for i in states:  # We're expecting a list of dictionaries
        if i.id == id:
            state = i

    if state is None:
        return render_template('9-state.html')

    cities = sorted(list(storage.all(City).values()), key=lambda x: x.name)

    return render_template('9-states.html',
                           state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
