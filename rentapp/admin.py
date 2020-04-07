from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .model.house import *
from .model.user import *
from .model import db

admin = Admin(name='rentApp', template_mode='bootstrap3')
admin.add_view(ModelView(House, db.session))
admin.add_view(ModelView(User, db.session))
