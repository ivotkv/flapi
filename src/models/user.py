from ..db import db
from ..crud import CRUDable


class User(db.Model, CRUDable):
    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.UUID, unique=True, nullable=False, default=db.uuid4)

    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=False)
    company = db.relationship("Company")
