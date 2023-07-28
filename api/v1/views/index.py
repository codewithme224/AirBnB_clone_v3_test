from api.v1.views import app_views
from flask import jsonify

# create a route /status on the object app_views that returns a JSON: "status": "OK"
@app_views.route('/status', strict_slashes=False)
def status():
    """ Method to return status """
    return jsonify({"status": "OK"})


"""Create an endpoint that retrieves the number of each objects by type:

In api/v1/views/index.py
Route: /api/v1/stats
You must use the newly added count() method from storage"""

@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Method to return stats """
    from models import storage
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
