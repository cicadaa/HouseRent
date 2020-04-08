from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# from flask_admin.model import
from flask import Markup

from .model.house import *
from .model.user import *
from .model import db


class MyModelView(ModelView):
    column_exclude_list = ['password_hash']

    def account_formatter(view, context, model, name):
        account_val = "%s" % model.account.name
        return Markup(account_val)

    column_formatters = {
        'account': account_formatter
    }


admin = Admin(name='rentApp', template_mode='bootstrap3')
admin.add_view(MyModelView(House, db.session))
admin.add_view(MyModelView(User, db.session))





