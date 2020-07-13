from ..db import db
from ..crud import CRUDable


class Company(db.Model, CRUDable):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, unique=True)

    users = db.relationship('User', cascade='save-update, merge, delete')

    def read(self):
        fields = super().read()
        fields['users_count'] = len(self.users)
        return fields
