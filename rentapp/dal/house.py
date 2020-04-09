from datetime import datetime
from flask_login import current_user
from rentapp.model.house import House
from rentapp.model import db
from rentapp.message_code import *
from . import db_add, db_commit



def post_house(kwargs):
    room_number = kwargs.get('room_number', None)
    size = kwargs.get('size', None)
    current_time = datetime.now()
    user_id = current_user.id
    house = House(room_number=room_number, size=size, pub_date=current_time, user_id=user_id)
    db_add(house)
    return SUCCESS, house


def update_house(kwargs):
    room_number = kwargs.get('room_number', None)
    size = kwargs.get('size', None)
    current_time = datetime.now()
    user_id = current_user.id
    house = House(room_number=room_number, size=size, pub_date=current_time, user_id=user_id)
    db_commit()
    return SUCCESS, house


def delete_house(kwargs):
    id = kwargs.get('id', None)
    cur_user_id = current_user.id
    house = House.query.filter_by(id=id).first()
    user_id = house.user_id
    if cur_user_id == user_id:
        House.query.filter_by(id=id).delete()
        db.session.commit()
    return SUCCESS

