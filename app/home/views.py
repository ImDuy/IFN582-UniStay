from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp
from app.db import get_all_properties_db, get_universities_db, get_image_map_db, get_nearby_db

@home_bp.route('/')
def index():
    q = request.args.get('q', '').strip()
    return render_template('/pages/index.html',
        all_properties = get_all_properties_db(q),
        universities = get_universities_db(),
        image_map = get_image_map_db(),
        nearby_map = get_nearby_db()
    )


@home_bp.route('/test-500')
def error():
    return render_template('/errors/500.html')