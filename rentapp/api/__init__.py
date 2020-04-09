from flask_restful import Api
from .account import *
from .house import *


def init_map(app):
    api = Api(app)

    api.add_resource(Signup, '/signup')
    api.add_resource(Login, '/login')
    api.add_resource(House, '/house')
