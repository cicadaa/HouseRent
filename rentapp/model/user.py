from . import db
from flask_login import UserMixin
from passlib.hash import bcrypt


class User(db.Model, UserMixin):
    __tablename__ = 'account'

    id = db.Column(db.Integer,
                   primary_key=True)

    contact = db.Column(db.Integer,
                        unique=False,
                        nullable=False)

    email = db.Column(db.String,
                      unique=True,
                      nullable=True)

    name = db.Column(db.String,
                     primary_key=False,
                     unique=False,
                     nullable=False)

    password_hash = db.Column(db.String(200),
                              primary_key=False,
                              unique=False,
                              nullable=False)

    houses = db.relationship('House',
                             backref='user',
                             lazy=True)

    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)

    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)

    last_update = db.Column(db.DateTime,
                            index=False,
                            unique=False,
                            nullable=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hash(password)
