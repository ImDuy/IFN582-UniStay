from flask import Blueprint


auth_bp = Blueprint('auth', __name__)
# you can separate auth_bp into 3 blueprints login/logout/register if you want to
# remember to register the new blueprints in the app/__init__.py file if you do change the blueprint

from . import views 