from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


db = SQLAlchemy()

def create_uuid_extension(app):
    engine = db.get_engine(app, bind=None)  # Ensure you are using the correct engine
    sql_create_extension = text("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
    sql_commit = text("COMMIT;")

    with engine.connect() as connection:
        connection.execute(sql_create_extension)
        connection.execute(sql_commit)