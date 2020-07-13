from flask import request, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..app import app
from ..db import db
from ..models import User, Company


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            try:
                return User.query.filter_by(uuid=session['login']).one().get_fields(), 200
            except db.NoResultFound:
                del session['login']
        return {}, 401

    else:
        if 'email' in request.form and 'password' in request.form:
            data = request.form
        elif isinstance(request.json, dict) and 'email' in request.json and 'password' in request.json:
            data = request.json
        else:
            return {}, 400

        try:
            user = User.query.filter_by(email=data['email'].lower().strip()).one()
            if check_password_hash(user.password, data['password']):
                session['login'] = user.uuid
                return user.get_fields(), 200
        except db.NoResultFound:
            session.pop('login', None)

        return {}, 401


@app.route('/auth/logout', methods=['GET', 'POST'])
def logout():
    session.pop('login', None)
    return {}, 200


@app.route('/auth/register', methods=['POST'])
def register():
    if 'email' in request.form and 'password' in request.form:
        data = request.form
    elif isinstance(request.json, dict) and 'email' in request.json and 'password' in request.json:
        data = request.json
    else:
        return {}, 400

    if User.query.filter_by(email=data['email'].lower().strip()).count() > 0:
        return {}, 409

    user = db.add(User(
        email=data['email'].lower().strip(),
        password=generate_password_hash(data['password']),
        first_name=data.get('first_name', '').strip(),
        last_name=data.get('last_name', '').strip()
    ))

    try:
        user.company = Company.query.filter_by(name='Floty').one()
    except db.NoResultFound:
        user.company = db.add(Company(name='Floty'))

    db.session.commit()

    session['login'] = user.uuid
    return user.get_fields(), 200
