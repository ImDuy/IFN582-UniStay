from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp
from app.db import get_all_properties, get_nearby, get_university


@home_bp.route('/')
def index():
    properties = get_all_properties()
    nearby = get_nearby()
    university = get_university
    return render_template('/pages/index.html')

@home_bp.route('/test-500')
def error():
    return render_template('/errors/500.html')