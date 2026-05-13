from flask import Blueprint


details_bp = Blueprint('details', __name__)


from . import views