"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Persons

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    

    if request.method =='POST':

        json = request.get_json()

        print(json['name'])
        print(json['age'])

        return jsonify(json['age'])

    if request.method == 'GET':
        return 'You used a GET method'

@app.route('/practice', methods=['POST','GET'])
def handle_pract():
    return "Just a practice"

        
@app.route('/account', methods=['POST'])
def handle_account():
    json = request.get_json()
    user = Persons(
        # username = json['username'],
        email = json['email'],
        password = json['password']
    )
    db.session.add(user)
    db.session.commit()

    return "user added"

@app.route('/user', methods=['POST' ])
def handle_nada():
    
    json = request.get_json()
    return json
    
@app.route('/login', methods=['POST'])
def handle_logins():
    json = request.get_json()
    if json['username'] == 'justusmays' and json['password'] == 'Curly23':
        return 'welcome back'
    else:
        return 'invalid information'


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
