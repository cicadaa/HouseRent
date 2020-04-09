from rentapp.model.user import User
from rentapp.model import db
from passlib.hash import bcrypt
from datetime import datetime
from rentapp.message_code import *

from flask import g, session, request
from flask_login import login_user, login_required, logout_user, current_user



def signup(kwargs):
    user_name = kwargs.get('name', None)
    email = kwargs.get('email', None)
    password = kwargs.get('password', None)
    contact = kwargs.get('contact', None)

    if not email:
        return NO_SUCH_EMAIL, None
    is_user = User.query.filter_by(email=email).first()
    if is_user:
        return ACCOUNT_ALREADY_EXIT, None

    user = User(name=user_name, email=email, contact=contact, password=password)
    db.session.add(user)
    db.session.commit()
    return SUCCESS, user


def login(kwargs):
    email = kwargs.get('email', None)
    password = kwargs.get('password', None)

    if not email or not password:
        return ACCOUNT_OR_PASSWORD_ERROR, None
    user = User.query.filter_by(email=email).first()
    if bcrypt.verify(password, user.password_hash):
        login_user(user)
        return SUCCESS, user


def logout():
    logout_user()
    return SUCCESS