# /opt/conda/bin/python3
from flask import Flask, request, render_template, Blueprint
from flask_restful import Api, Resource, reqparse
from flask_migrate import Migrate
import json

import sqlalchemy
from models import User, House, HouseLease, HouseImage, db, Gender, User_Role
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os
import argparse
import sys

app = Flask(__name__, static_folder="../build", static_url_path='/')


def create_app():
    # app = Flask(__name__, static_folder="static/dist", template_folder="static")
    
    load_dotenv()
    dev = os.getenv('DEV')
    if dev.lower() == 'true':
        user = os.getenv('DB_USERNAME')
        password = os.getenv('DEV_PASSWORD')
        DBNAME = os.getenv('DB_NAME')
        app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@localhost:5432/{DBNAME}"
    else:
        # configuration
        USERNAME = os.getenv('DB_USERNAME')
        PASSWORD = os.getenv('DB_PASSWORD')
        DBNAME = os.getenv('DB_NAME')
        PUBLIC_IP_ADDRESS = os.getenv('DB_PUBLIC_IP_ADDRESS')
        PROJECT_ID = os.getenv('PROJECT_ID')
        INSTANCE_UNIX_SOCKET = os.getenv('INSTANCE_UNIX_SOCKET')
        
        uri = sqlalchemy.engine.url.URL(
            drivername="postgresql+psycopg2",
            username=USERNAME,
            password=PASSWORD,
            database=DBNAME,
            query={"host": INSTANCE_UNIX_SOCKET},
            host=None,
            port=None
        )
        
        app.config['SQLALCHEMY_DATABASE_URI'] = uri.render_as_string(hide_password=False)
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            create_database(app.config['SQLALCHEMY_DATABASE_URI'])
        db.create_all()
    return app


@app.route("/")
def index():
    return app.send_static_file('index.html')


'''

# Return JSON of all houses
@app.route('/houses')
def houses():
	houses = House.query.all()
	house_list = []
	for house in houses:
		house_list.append(house.to_dict())
	return json.dumps(house_list)

@app.route('/houses/<int:house_id>')
def house(house_id):
	house = House.query.filter_by(id=house_id).first()
	return json.dumps(house.to_dict())

@app.route('/houses', methods=['POST'])
def create_house():
	house = House(
		landlord_id=request.json['landlord_id'],
		address=request.json['address'],
		city=request.json['city'],
		state=request.json['state'],
		zip_code=request.json['zip_code'],
		google_maps_link=request.json['google_maps_link'],
		status=request.json['status'],
		beds=request.json['beds'],
		baths=request.json['baths'],
		sq_ft=request.json['sq_ft'],
		rent=request.json['rent'],
		other_information=request.json['other_information']
	)

	db.session.add(house)
	db.session.commit()
	return json.dumps(house.to_dict())

# Return JSON of all house leases
@app.route('/house_leases')
def house_leases():
	house_leases = HouseLease.query.all()
	lease_list = []
	for lease in house_leases:
		lease_list.append(lease.to_dict())
	return json.dumps(lease_list)

# Return JSON of all house images
@app.route('/house_images')
def house_images():
	house_images = HouseImage.query.all()
	image_list = []
	for image in house_images:
		image_list.append(image.to_dict())
	return json.dumps(image_list)
'''


class HomeAPI(Resource):
    def get(self):
        return render_template('home.html')


class SignupAPI(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, help='No username provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True, help='No password provided', location='json')
        self.reqparse.add_argument('email', type=str, required=True, help='No email provided', location='json')
        self.reqparse.add_argument('first_name', default='', type=str, required=False, help='No first name provided',
                                   location='json')
        self.reqparse.add_argument('last_name', default='', type=str, required=False, help='No last name provided',
                                   location='json')
        self.reqparse.add_argument('phone_number', default='', type=str, required=False,
                                   help='No phone number provided', location='json')
        self.reqparse.add_argument('city', default='', type=str, required=False, help='No city provided',
                                   location='json')
        self.reqparse.add_argument('state', default='', type=str, required=False, help='No state provided',
                                   location='json')
        self.reqparse.add_argument('zip_code', default='', type=str, required=False, help='No zip code provided',
                                   location='json')
        self.reqparse.add_argument('gender', default='NOT_PROVIDED', type=str, required=False,
                                   help='no gender provided, can be one of male, female, other', location='json')
        self.reqparse.add_argument('bio', default='', type=str, required=False, help='No bio provided', location='json')
        self.reqparse.add_argument('profile_picture', default='', type=str, required=False,
                                   help='No profile picture provided', location='json')
        self.reqparse.add_argument('age', default=0, type=int, required=False, help='No age provided', location='json')
        self.reqparse.add_argument('role', default='TENANT', type=str, required=False,
                                   help='No role provided, can be one of tenant, landlord, tenant_landlord',
                                   location='json')
        super(SignupAPI, self).__init__()
    
    def post(self):
        args = self.reqparse.parse_args()
        if User.query.filter_by(username=args['username']).first():
            return "Username already exists", 409
        if User.query.filter_by(email=args['email']).first():
            return "Email already exists", 409
        if args['gender'].upper() not in Gender.__members__:
            return "invalid gender provided, can be one of male, female, other", 400
        if args['role'].upper() not in User_Role.__members__:
            return "invalid role provided, can be one of tenant, landlord, tenant_landlord", 400
        user = User(args['username'], args['password'], args['email'], User_Role(args['role'].upper()), args['city'],
                    args['state'], Gender(args['gender'].upper()),
                    args['age'], args['phone_number'], args['profile_picture'], args['bio'])
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 201


class LoginAPI(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, help='No username provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True, help='No password provided', location='json')
        super(LoginAPI, self).__init__()
    
    def post(self):
        args = self.reqparse.parse_args()
        userFromDB = User.query.filter_by(username=args['username']).first()
        if userFromDB is None:
            return "No user found", 404
        if userFromDB.password != args['password']:
            return "Incorrect password", 401
        return userFromDB.to_dict(), 200


class UserAPI(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=False, help='No username provided', location='json')
        self.reqparse.add_argument('password', type=str, required=False, help='No password provided', location='json')
        self.reqparse.add_argument('email', type=str, required=False, help='No email provided', location='json')
        self.reqparse.add_argument('first_name', type=str, required=False, help='No first name provided',
                                   location='json')
        self.reqparse.add_argument('last_name', type=str, required=False, help='No last name provided', location='json')
        self.reqparse.add_argument('phone_number', type=str, required=False, help='No phone number provided',
                                   location='json')
        self.reqparse.add_argument('city', type=str, required=False, help='No city provided', location='json')
        self.reqparse.add_argument('state', type=str, required=False, help='No state provided', location='json')
        self.reqparse.add_argument('zip_code', type=str, required=False, help='No zip code provided', location='json')
        self.reqparse.add_argument('gender', type=str, required=False,
                                   help='no gender provided, can be one of male, female, other', location='json')
        self.reqparse.add_argument('bio', type=str, required=False, help='No bio provided', location='json')
        self.reqparse.add_argument('profile_picture', type=str, required=False, help='No profile picture provided',
                                   location='json')
        self.reqparse.add_argument('age', type=int, required=False, help='No age provided', location='json')
        self.reqparse.add_argument('role', type=str, required=False,
                                   help='No role provided, can be one of tenant, landlord, tenant_landlord',
                                   location='json')
        super(UserAPI, self).__init__()
    
    def get(self, id):
        userFiltered = User.query.filter_by(id=id).first()
        print(userFiltered)
        if userFiltered is None:
            return "No user found", 404
        return userFiltered.to_dict(), 200
    
    def put(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return "No user found", 404
        args = self.reqparse.parse_args()
        print(args)
        if 'username' in args and args['username'] is not None:
            userWithName = User.query.filter_by(username=args['username']).first()
            if userWithName is not None:
                return "Username already exists", 409
            user.username = args['username']
        if 'password' in args and args['password'] is not None:
            user.password = args['password']
        if 'email' in args and args['email'] is not None:
            userWithEmail = User.query.filter_by(email=args['email']).first()
            if userWithEmail is not None:
                return "Email already exists", 409
            user.email = args['email']
        if 'first_name' in args and args['first_name'] is not None:
            user.first_name = args['first_name']
        if 'last_name' in args and args['last_name'] is not None:
            user.last_name = args['last_name']
        if 'phone_number' in args and args['phone_number'] is not None:
            user.phone_number = args['phone_number']
        if 'city' in args and args['city'] is not None:
            user.city = args['city']
        if 'state' in args and args['state'] is not None:
            user.state = args['state']
        if 'zip_code' in args and args['zip_code'] is not None:
            user.zip_code = args['zip_code']
        if 'role' in args and args['role'] is not None:
            if args['role'].upper() not in User_Role.__members__:
                return "invalid role provided, can be one of tenant, landlord, tenant_landlord", 400
            user.role = User_Role(args['role'].upper())
        if 'gender' in args and args['gender'] is not None:
            if args['gender'].upper() not in Gender.__members__:
                return "invalid gender provided, can be one of male, female, other", 400
            user.gender = Gender(args['gender'].upper())
        if 'bio' in args and args['bio'] is not None:
            user.bio = args['bio']
        if 'profile_picture' in args and args['profile_picture'] is not None:
            user.profile_picture = args['profile_picture']
        if 'age' in args and args['age'] is not None:
            user.age = args['age']
        db.session.commit()
        user = User.query.filter_by(id=id).first()
        return user.to_dict(), 200


migrate = Migrate()
app = create_app()
api = Api(app)
api.add_resource(HomeAPI, '/')
api.add_resource(SignupAPI, '/api/v1/signup')
api.add_resource(LoginAPI, '/api/v1/login')
api.add_resource(UserAPI, '/api/v1/user/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
