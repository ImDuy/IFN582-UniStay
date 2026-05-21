from flask import Blueprint, render_template
from . import auth_login_bp, auth_register_bp

@auth_login_bp.route("/auth/login")
def login():
    return render_template('pages/login.html')

@auth_register_bp.route("/auth/register")
def register():
    return render_template('pages/register.html')