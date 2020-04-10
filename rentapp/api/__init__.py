from flask_restful import Api
from .account import *
from .house import *


def init_map(app):
    api = Api(app)

    api.add_resource(Signup, '/signup')
    api.add_resource(Login, '/login')
    api.add_resource(House, '/house')

    @app.after_request
    def after_request(resp):
        set_cross(resp)
        return resp


def set_cross(resp):
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods",
                     "POST,GET,OPTIONS,DELETE,PUT")
    resp.headers.add("Access-Control-Allow-Headers",
                     "Content-Type, Authorization, Accept, X-Requested-With, If-Modified-Since, Frontend-Version")
    resp.headers.add("Access-Control-Expose-Headers", "Frontend-Version")
    resp.headers.add("Access-Control-Allow-Credentials", "true")
    # resp.headers.add("Frontend-Version", get_last_frontend_version())
    # resp.headers.add("Maintain", config.MAINTAIN)
