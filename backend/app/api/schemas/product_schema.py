from flask_restx import fields, Model

product_model = Model('Product', {
    'id': fields.String(readOnly=True, description='The unique identifier for the product', example='uuid-example'),
    'name': fields.String(required=True, description='The name of the product'),
    'description': fields.String(description='The description of the product')
})
