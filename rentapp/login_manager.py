from flask_login import LoginManager
from .model.user import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
    except:
        user = None
    return user
