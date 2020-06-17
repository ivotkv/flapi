from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from .app import app

db = SQLAlchemy(app)
db.UUID = UUID
db.JSONB = JSONB
