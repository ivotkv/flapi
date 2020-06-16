from flask import request
from flask_restful import Api, Resource
from sqlalchemy.orm.exc import NoResultFound

import app.models as models
from .app import app
from .db import db

api = Api(app)


class DatabaseResource(Resource):
    @property
    def model(self):
        return getattr(models, self.__class__.__name__)

    def get(self, id=None):
        if id is None:
            query = self.model.query
            field_names = self.model.get_field_names()
            for key, value in request.args.items():
                if key in field_names:
                    col_type = type(getattr(self.model, key).property.columns[0].type)
                    if col_type is db.Integer and value.isdigit():
                        query = query.filter(getattr(self.model, key) == int(value))
            return [i.read() for i in query.all()]
        else:
            try:
                return self.model.query.filter_by(id=id).one().read()
            except NoResultFound:
                return {}, 404

    def post(self):
        entity = self.model.create(request.json)
        db.session.commit()
        return entity.read()

    def delete(self, id):
        try:
            self.model.query.filter_by(id=id).one().delete()
            db.session.commit()
            return {}, 204
        except NoResultFound:
            return {}, 404

    def put(self, id):
        try:
            entity = self.model.query.filter_by(id=id).one()
            entity.update(request.json)
            db.session.commit()
            return entity.read()
        except NoResultFound:
            return {}, 404


for model_name in (
    name
    for name in dir(models)
    if (
        isinstance(getattr(models, name), type)
        and issubclass(getattr(models, name), db.Model)
    )
):
    api.add_resource(
        type(model_name, (DatabaseResource,), {}),
        "/{0}".format(model_name.lower()),
        "/{0}/<int:id>".format(model_name.lower()),
    )
