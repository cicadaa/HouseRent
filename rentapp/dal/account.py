from rentapp.model.user import User
from rentapp.model import db
from passlib.hash import bcrypt
from flask import g, session, request
from flask_login import login_user, login_required, logout_user, current_user



def signup(kwargs):
    user_name = kwargs.get('name', None)
    email = kwargs.get('email', None)
    password = kwargs.get('password', None)
    contact = kwargs.get('contact', None)
    if not email:
        return 404, None
    is_user = User.query.filter_by(email=email).first()
    if is_user:
        return 404, None
    user = User(name=user_name, email=email, contact=contact, password=password)
    db.session.add(user)
    db.session.commit()
    return 200, user


def login(kwargs):
    email = kwargs.get('email', None)
    password = kwargs.get('password', None)

    if not email or not password:
        return 404, None
    user = User.query.filter_by(email=email).first()
    if bcrypt.verify(password, user.password_hash):
        login_user(user)
        return 200, user


@login_required
def logout():
    logout_user()
    return 200