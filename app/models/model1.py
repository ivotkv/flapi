from ..db import db, CRUDable


class Model1(db.Model, CRUDable):
    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.UUID, unique=True)
    name = db.Column(db.String, unique=True)

    model2s = db.relationship("Model2", cascade="save-update, merge, delete")

    def read(self):
        fields = super().read()
        fields["model2s_count"] = len(self.model2s)
        return fields
