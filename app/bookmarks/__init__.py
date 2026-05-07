from flask import Blueprint


bookmarks_bp = Blueprint('bookmarks', __name__)


from . import views 