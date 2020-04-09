from rentapp.model.user import User
from rentapp.message_code import *
from . import db_add, db_commit

from passlib.hash import bcrypt
from datetime import datetime
from flask_login import login_user, logout_user


def signup(kwargs):
    user_name = kwargs.get('name', None)
    email = kwargs.get('email', None)
    password = kwargs.get('password', None)
    contact = kwargs.get('contact', None)
    created_on = datetime.now()
    if not email:
        return NO_SUCH_EMAIL, None
    is_user = User.query.filter_by(email=email).first()
    if is_user:
        return ACCOUNT_ALREADY_EXIT, None

    user = User(name=user_name, email=email, contact=contact, password=password, created_on=created_on)

    db_add(user)

    return SUCCESS, user


def login(kwargs):
    email = kwargs.get('email', None)
    password = kwargs.get('password', None)

    if not email or not password:
        return ACCOUNT_OR_PASSWORD_ERROR, None
    user = User.query.filter_by(email=email).first()

    if bcrypt.verify(password, user.password_hash):
        login_user(user)
        user.last_login = datetime.now()
        db_commit()
        return SUCCESS, user


def logout():
    logout_user()
    return SUCCESS

