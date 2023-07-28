"""Create a new view for State objects that handles all default RESTFul API actions:

In the file api/v1/views/states.py
You must use to_dict() to retrieve an object into a valid JSON"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
@app_views.route('/states', methods=['GET'])
def get_states():
    """ Method to return all states """
    states = storage.all("State")
    states_list = []
    for state in states.values():
        states_list.append(state.to_dict())
    return jsonify(states_list)
