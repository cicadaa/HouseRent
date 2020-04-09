from rentapp.model import db


def db_add(item):
    db.session.add(item)
    db.session.commit()


def db_commit():
    db.session.commit()
