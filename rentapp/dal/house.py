from datetime import datetime
from flask_login import current_user
from rentapp.model.house import House
from rentapp.model import db
from rentapp.message_code import *


def post_house(kwargs):
    room_number = kwargs.get('room_number', None)
    size = kwargs.get('size', None)
    current_time = datetime.now()
    user_id = current_user.id
    house = House(room_number=room_number, size=size, pub_date=current_time, user_id=user_id)
    db.session.add(house)
    db.session.commit(house)
    return house, SUCCESS
