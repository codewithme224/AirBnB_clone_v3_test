from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

# create a variable app, instance of Flask
app = Flask(__name__)
app.register_blueprint(app_views)
@app.route('/') 


def hello_world():
    """ Method to return Hello HBNB """
    return 'Hello HBNB!'
@app.teardown_appcontext
def teardown_appcontext(self):
    """ Method to handle teardown """
    storage.close()



@app.errorhandler(404)
def page_not_found(e):
    """ Method to handle 404 error """
    return jsonify({"error": "Not found"}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

