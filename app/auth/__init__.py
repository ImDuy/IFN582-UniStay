from flask import Blueprint


auth_login_bp = Blueprint('auth_login', __name__)
# you can separate auth_bp into 3 blueprints login/logout/register if you want to
# remember to register the new blueprints in the app/__init__.py file if you do change the blueprint
auth_register_bp = Blueprint('auth_register', __name__)
auth_logout_bp = Blueprint('auth_logout', __name__)

from . import views 