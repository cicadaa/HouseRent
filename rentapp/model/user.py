from . import db

from flask_login import UserMixin
from passlib.hash import bcrypt
from datetime import datetime


class User(db.Model, UserMixin):

    __tablename__ = 'account'

    id = db.Column(db.Integer,
                   primary_key=True)

    contact = db.Column(db.Integer,
                        unique=False,
                        nullable=True)

    email = db.Column(db.String,
                      unique=True,
                      nullable=True)

    name = db.Column(db.String,
                     primary_key=False,
                     unique=False,
                     nullable=True)

    password_hash = db.Column(db.String(200),
                              primary_key=False,
                              unique=False,
                              nullable=False)

    houses = db.relationship('House',
                             backref='account',
                             lazy=True)

    created_on = db.Column(db.DateTime,
                           default=datetime.now)

    last_login = db.Column(db.DateTime,
                           onupdate=datetime.now)

    last_update = db.Column(db.DateTime,
                            onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hash(password)

    def __repr__(self):
        return '<User %r>' % self.name
