from ..db import db, CRUDable


class Model2(db.Model, CRUDable):
    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.UUID, unique=True)
    name = db.Column(db.String, unique=True)

    model1_id = db.Column(db.Integer, db.ForeignKey("model1.id"), nullable=False)
    model1 = db.relationship("Model1")
