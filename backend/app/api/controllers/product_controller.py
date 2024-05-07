from flask_restx import Resource, Namespace
from api.schemas.product_schema import product_model
from api.models.product import Product
from api.models.base import db

product_ns = Namespace(
    'products', description='Operations related to products')
product_ns.add_model("Product", product_model)


@product_ns.route('/')
class ProductResource(Resource):
    @product_ns.marshal_list_with(product_model, envelope='data')
    def get(self):
        """Fetch all products"""
        products = Product.query.all()
        return products

    @product_ns.expect(product_model, validate=True)
    def post(self):
        """Create a new product"""
        data = product_ns.payload
        new_product = Product(
            name=data['name'], description=data['description'])
        db.session.add(new_product)
        db.session.commit()
        return new_product, 201


@product_ns.route('/<uuid:product_id>')
@product_ns.param('product_id', 'The product identifier')
@product_ns.response(404, 'Product not found')
class ProductById(Resource):
    @product_ns.marshal_with(product_model)
    def get(self, product_id):
        """Fetch a single product by ID"""
        product = Product.query.get_or_404(product_id)
        return product

    @product_ns.expect(product_model, validate=True)
    @product_ns.response(200, 'Product updated successfully')
    def put(self, product_id):
        """Update a product by ID"""
        product = Product.query.get_or_404(product_id)
        data = product_ns.payload
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        db.session.commit()
        return product, 200
