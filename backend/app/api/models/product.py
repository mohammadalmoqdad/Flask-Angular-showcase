from api.models.base import db
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
