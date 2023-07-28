from flask import Blueprint
from api.v1.views.index import *
from api.v1.views import states


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Retrieves the list of all State objects: GET /api/v1/states
app_views.add_url_rule('/states', view_func=states.get_states, methods=['GET'])


"""Retrieves a State object: GET /api/v1/states/<state_id>

If the state_id is not linked to any State object, raise a 404 error"""

app_views.add_url_rule('/states/<state_id>', view_func=states.get_state,
                        methods=['GET'])
# If the state_id is not linked to any State object, raise a 404 error
app_views.add_url_rule('/states/<state_id>', view_func=states.delete_state,
                        methods=['DELETE'])


"""Creates a State: POST /api/v1/states

You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key name, raise a 400 error with the message Missing name
Returns the new State with the status code 201"""

app_views.add_url_rule('/states', view_func=states.create_state,
                        methods=['POST'])


