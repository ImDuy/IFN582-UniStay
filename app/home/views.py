from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp

@home_bp.route('/')
def index():
    return render_template('index.html')