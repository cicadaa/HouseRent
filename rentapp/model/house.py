from . import db

__all__ = ['House']


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordX = db.Column(db.Float, unique=False, nullable=True)
    coordY = db.Column(db.Float, unique=False, nullable=True)

    roomNumber = db.Column(db.Integer, unique=False, nullable=True)
    size = db.Column(db.Float, unique=False, nullable=True)

    pub_date = db.Column(db.DateTime, nullable=False)
    publisherId = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)
