from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager

from api.models.base import db, create_uuid_extension
from api.controllers.user_controller import user_ns
from api.controllers.product_controller import product_ns
from api.errors.error_handlers import register_error_handlers
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_error_handlers(app)
    db.init_app(app)

    jwt = JWTManager(app)

    api = Api(app, title='Product API', version='1.0',
              description='A simple API for managing products and users')

    api.add_namespace(product_ns, path='/api/products')
    api.add_namespace(user_ns, path='/api/users')

    with app.app_context():
        create_uuid_extension(app)
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
