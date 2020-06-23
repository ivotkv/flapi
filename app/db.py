from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.attributes import InstrumentedAttribute, flag_modified
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from .app import app

db = SQLAlchemy(app)
db.UUID = UUID
db.JSONB = JSONB
db.SQLAlchemyError = SQLAlchemyError
db.InstrumentedAttribute = InstrumentedAttribute
db.flag_modified = flag_modified
db.NoResultFound = NoResultFound
db.MultipleResultsFound = MultipleResultsFound
