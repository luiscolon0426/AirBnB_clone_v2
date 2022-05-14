#!/usr/bin/python3
''' comment '''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ return list of states in Database """
    state_li = storage.all(State).values()
    return render_template('7-states_list.html', states=state_li)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ close session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
