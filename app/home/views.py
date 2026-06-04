from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp
from app.db import get_all_properties_db, get_filtered_properties_db, get_universities_db, get_image_map_db, get_nearby_db
from app.constants import Defaults
@home_bp.route('/')
def index():
    q = request.args.get('q', '').strip()
    uni = request.args.get('uni', 'all')
    property_type = request.args.get('type', 'all')
    dist = request.args.get('dist', 'any')
    price_min = request.args.get('price_min', None)
    price_max = request.args.get('price_max', None)
    amenities = request.args.getlist('amenity')
    is_filtered = bool(q or (uni and uni != 'all') or (property_type and property_type != 'all') or (dist and dist != 'any') or amenities)
    return render_template('/pages/index.html',
        all_properties = get_filtered_properties_db(q, uni, property_type, dist, price_min, price_max, amenities),
        universities = get_universities_db(),
        image_map = get_image_map_db(),
        nearby_map = get_nearby_db(),
        is_filtered = is_filtered,
        default_image=Defaults.IMAGE.value
    )


@home_bp.route('/test-500')
def error():
    return render_template('/errors/500.html')