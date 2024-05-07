from flask import jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(IntegrityError)
    def handle_integrity_error(error):
        return jsonify({
            'message': 'A database error occurred.',
            'details': str(error.orig) if hasattr(error, 'orig') else 'No detail'
        }), 400

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return jsonify({
            'message': str(error.description),
            'code': error.code
        }), error.code

    @app.errorhandler(Exception)
    def handle_general_exception(error):
        return jsonify({
            'message': 'An unexpected error occurred.',
            'details': str(error)
        }), 500
