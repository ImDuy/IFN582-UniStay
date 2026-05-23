from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp
from app.db import get_all_properties, get_nearby, get_properties_by_university, search_properties


@home_bp.route('/')
def index():
    q = request.args.get('q', '').strip()
    if q:
        all_properties = search_properties(q)
    else:
        all_properties = get_all_properties()

    return render_template ('/pages/index.html', 
        all_properties=all_properties,
        uq_properties=get_properties_by_university("uq"),
        qut_properties=get_properties_by_university("qut"),
        griffith_properties=get_properties_by_university("griffith"),
        nearby = get_nearby()
)


@home_bp.route('/test-500')
def error():
    return render_template('/errors/500.html')