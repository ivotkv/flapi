from functools import lru_cache

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm.properties import ColumnProperty

from .app import app

db = SQLAlchemy(app)
db.UUID = UUID


class CRUDable(object):
    @classmethod
    def create(cls, fields):
        instance = cls()
        db.session.add(instance)
        instance.set_fields(fields)
        return instance

    def read(self):
        return self.get_fields()

    def update(self, fields):
        self.set_fields(fields)

    def delete(self):
        db.session.delete(self)

    @classmethod
    @lru_cache()
    def get_field_names(cls):
        fields = set()
        for field in dir(cls):
            value = getattr(cls, field)
            if (
                isinstance(value, InstrumentedAttribute)
                and isinstance(value.property, ColumnProperty)
            ):
                fields.add(field)
        return fields

    def get_fields(self):
        return {field: getattr(self, field) for field in self.get_field_names()}

    def set_fields(self, fields):
        field_names = self.get_field_names()
        for field, value in fields.items():
            if field in field_names:
                setattr(self, field, value)


class Model1(db.Model, CRUDable):
    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.UUID, unique=True)
    name = db.Column(db.String, unique=True)

    model2s = db.relationship("Model2", cascade="save-update, merge, delete")

    def read(self):
        fields = super().read()
        fields["model2s_count"] = len(self.model2s)
        return fields


class Model2(db.Model, CRUDable):
    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.UUID, unique=True)
    name = db.Column(db.String, unique=True)

    model1_id = db.Column(db.Integer, db.ForeignKey("model1.id"), nullable=False)
    model1 = db.relationship("Model1")
