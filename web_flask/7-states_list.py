#!/usr/bin/python3
''' A Flask app to render storage engine data '''


from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
@app.route('/states', strict_slashes=False)
def storage():

    return render_template('7-states_list.html', storage.all())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
