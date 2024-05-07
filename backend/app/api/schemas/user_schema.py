from flask_restx import fields, Model

user_creation_model = Model('UserCreation', {
    'username': fields.String(required=True, description='Username of the User'),
    'email': fields.String(required=True, description='Email of the User'),
    'password': fields.String(required=True, description='Password of the User')
})

user_model = Model('User', {
    'id': fields.String(description='The user ID', readOnly=True),
    'username': fields.String(required=True, description='Username of the User'),
    'email': fields.String(required=True, description='Email of the User')
})

login_model = Model('Login', {
    'username': fields.String(required=True, description='Username of the user'),
    'password': fields.String(required=True, description='Password of the user')
})
