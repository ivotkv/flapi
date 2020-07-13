from datetime import datetime
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import UUID, JSON, JSONB
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.attributes import InstrumentedAttribute, flag_modified
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy_json import mutable_json_type

from .app import app


def add(entity):
    db.session.add(entity)
    return entity


db = SQLAlchemy(app, session_options={'autoflush': False})
migrate = Migrate(app, db)

db.add = add
db.now = datetime.now
db.uuid4 = lambda: str(uuid4())
db.UUID = UUID()
db.JSON = mutable_json_type(dbtype=JSON, nested=True)
db.JSONB = mutable_json_type(dbtype=JSONB, nested=True)
db.SQLAlchemyError = SQLAlchemyError
db.InstrumentedAttribute = InstrumentedAttribute
db.flag_modified = flag_modified
db.NoResultFound = NoResultFound
db.MultipleResultsFound = MultipleResultsFound
