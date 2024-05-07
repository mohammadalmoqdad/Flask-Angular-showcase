from flask import request
from flask_restx import Resource, Namespace
from flask_jwt_extended import create_access_token
from api.schemas.user_schema import user_creation_model, user_model, login_model
from api.models.user import User
from api.models.base import db

user_ns = Namespace('users', description='Operations related to users')

user_ns.add_model('UserCreation', user_creation_model)
user_ns.add_model('User', user_model)
user_ns.add_model('Login', login_model)


@user_ns.route('/')
class User(Resource):
    @user_ns.marshal_list_with(user_model, envelope='data')
    def get(self):
        """Fetch all users"""
        users = User.query.all()
        return users

    @user_ns.expect(user_creation_model, validate=True)
    def post(self):
        """Create a new user"""
        data = user_ns.payload
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_ns.marshal(new_user, user_model), 201


@user_ns.route('/<uuid:user_id>')
@user_ns.param('user_id', 'The user identifier')
@user_ns.response(404, 'User not found')
class UserById(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        """Fetch a single user by ID"""
        user = User.query.get_or_404(user_id)
        return user


@user_ns.route('/login')
class UserLogin(Resource):
    @user_ns.expect(login_model, validate=True)
    def post(self):
        """Authenticate user and return JWT"""
        data = request.json
        user = User.query.filter_by(username=data['username']).first()

        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.id)
            return {'access_token': token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401
