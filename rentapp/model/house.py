from . import db
from datetime import datetime

__all__ = ['House']


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordX = db.Column(db.Float, unique=False, nullable=True)
    coordY = db.Column(db.Float, unique=False, nullable=True)

    room_number = db.Column(db.Integer, unique=False, nullable=True)
    size = db.Column(db.Float, unique=False, nullable=True)

    pub_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                        nullable=False)
    show = db.Column(db.Boolean, default=True, nullable=True)
