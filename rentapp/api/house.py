from flask_login import login_required
from flask_restful import reqparse
from rentapp.dal.house import post_house, update_house, delete_house
from flask_restful import Resource


class House(Resource):

    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('room_number', type=int, required=True, help='room number is required')
        parser.add_argument('size', type=int, required=True, help='size is required')
        parser.add_argument('show', type=int, required=True, help='show is to be defined')

        kwargs = parser.parse_args()
        code, house = post_house(kwargs)
        return {'houseid': house.id}

    @login_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('room_number', type=int, required=False)
        parser.add_argument('size', type=int, required=False)
        parser.add_argument('show', type=bool, required=False)

        kwargs = parser.parse_args()
        code, house = update_house(kwargs)
        return {'houseid': house.id}

    @login_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        kwargs = parser.parse_args()
        code = delete_house(kwargs)
        return {'status': code}