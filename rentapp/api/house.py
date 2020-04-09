from flask_login import login_required
from flask_restful import reqparse
from rentapp.dal.house import post_house
from flask_restful import Resource


class House(Resource):

    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('room_number', type=int, required=True, help='room number required')
        parser.add_argument('size', type=int, required=True, help='size required')
        kwargs = parser.parse_args()
        house, code = post_house(kwargs)
        return {'houseid': house.id}
