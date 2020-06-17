from ..db import db, CRUDable


class User(db.Model, CRUDable):
    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.UUID, unique=True)
    name = db.Column(db.String, unique=True)

    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=False)
    company = db.relationship("Company")
