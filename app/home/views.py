from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp
from app.db import get_all_properties, get_nearby, get_university, get_properties_by_university


@home_bp.route('/')
def index():
    properties = get_all_properties()
    university = get_university()
    nearby = get_nearby()
    nearby[0].distance
    print('value of nearby',nearby)
    return render_template ('/pages/index.html', 
        all_properties=get_all_properties(),
        uq_properties=get_properties_by_university("uq"),
        qut_properties=get_properties_by_university("qut"),
        griffith_properties=get_properties_by_university("griffith"),
        nearby = get_nearby()
)
        

@home_bp.route('/test-500')
def error():
    return render_template('/errors/500.html')