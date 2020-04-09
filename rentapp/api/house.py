from flask_login import login_required
from flask_restful import reqparse
from rentapp.dal.house import post_house, update_house, delete_house
from flask_restful import Resource


class House(Resource):

    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('room_number', type=int, required=True, help='room number required')
        parser.add_argument('size', type=int, required=True, help='size required')
        kwargs = parser.parse_args()
        code, house = post_house(kwargs)
        return {'houseid': house.id}

    @login_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('room_number', type=int, required=True, help='room number required')
        parser.add_argument('size', type=int, required=True, help='size required')
        kwargs = parser.parse_args()
        code, house = update_house(kwargs)
        return {'houseid': house.id}

    @login_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id required')
        kwargs = parser.parse_args()
        code = delete_house(kwargs)
        return {'status': code}