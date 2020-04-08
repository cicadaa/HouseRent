from flask_login import login_required, login_user
from flask_restful import reqparse
from rentapp.dal.account import signup
from flask_restful import Resource


class Login(Resource):
    @login_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help='email required')
        parser.add_argument('password', type=str, help='password required')
        


class Signup(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='username is required and should be a string')
        parser.add_argument('email', required=True, help='email is required and should be a string')
        parser.add_argument('contact', required=False, help='username is required and should be a string')
        parser.add_argument('password', required=True, help='password is required and should be a string')

        kwargs = parser.parse_args()
        code, user = signup(kwargs)
        if code != 200:
            return code
        return {"user_id": user.id}
