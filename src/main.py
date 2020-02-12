"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Persons, Users, Jobs
import seeds
import Jobs

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
    return render_template('index.html')

        
@app.route('/account', methods=['POST'])
def handle_account():
    json = request.get_json()
    user = Persons(
        username = json['username'],
        email = json['email'],
        password = json['password']
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(json)


@app.route('/user', methods=['POST' ])
def handle_nada():
    return seeds.table()
    
    
@app.route('/login', methods=['POST'])
def handle_logins():
    json = request.get_json()
    if json['username'] == 'justusmays' and json['password'] == 'Curly23':
        return 'welcome back'
    else:
        return 'invalid information'


@app.route('/users/<id>', methods=['GET'])
def get_persons(id):
   
    # person = Users.query.get(3)
    # return jsonify(person.serialize())


    person = Users.query.get(int(id))
    if person is None:
        return 'Person not found'
    return jsonify(person.serialize())

@app.route('/userss', methods=['GET'])
def get_personss():

    persons = Users.query.filter(Users.email.ilike('%j%') )

    # users_dict = []
    # for person in persons:
    #     person_dict.append( person.serialize())

    # return jsonify( users_dict)

    return jsonify( [x.serialize() for x in persons])

# this only runs if `$ python src/main.py` is executed


@app.route('/numbers', methods=['POST','GET'])
def handle_numbers():
    for i in range(1,20):
        if i%2==0:
            print(i)
    
    return jsonify(i)
    
# @app.route('/job', methods=['POST'])
# def handle_jobs():
#     json = request.get_json()
#     user = Jobs(
#         name = json['name'],
#         position = json['position'],
#         location = json['location'],
#         salary = json['salary']
#     )
#     db.session.add(user)
#     db.session.commit()

#     return jsonify(json)

@app.route('/jobs', methods=['POST'])
def handle_jobs():
    return Jobs.table()


@app.route('/jobss', methods=['GET'])
def get_jobssss():
   
    job = Jobs.query.get(1)
    json = Jobs.serialize()
    return jsonify(json)


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
