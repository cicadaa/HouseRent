from flask_login import login_required
from flask_restful import reqparse
from rentapp.dal.account import signup, login, logout
from flask_restful import Resource
from rentapp.message_code import *


class Login(Resource):
    @login_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='email required')
        parser.add_argument('password', type=str, required=True, help='password required')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='email required and should be a string')
        parser.add_argument('password', type=str, required=True, help='password is required and should be a string')
        kwargs = parser.parse_args()
        code, user = login(kwargs)
        if code != SUCCESS:
            return code
        return {"user_id": 'login succeed:)'}

    @login_required
    def put(self):
        logout()
        return {"user_id": 'logout succeed:('}


class Signup(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='username is required and should be a string')
        parser.add_argument('email', required=True, help='email is required and should be a string')
        parser.add_argument('contact', required=False)
        parser.add_argument('password', required=True, help='password is required and should be a string')

        kwargs = parser.parse_args()
        code, user = signup(kwargs)
        if code != SUCCESS:
            return code
        return {'user': user.name}
