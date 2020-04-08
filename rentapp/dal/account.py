from rentapp.model.user import User
from rentapp.model import db


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
