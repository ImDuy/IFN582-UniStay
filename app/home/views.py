from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp

@home_bp.route('/')
def index():
    return render_template('/pages/index.html')

@home_bp.route('/test-500')
def error():
    return render_template('/errors/500.html')