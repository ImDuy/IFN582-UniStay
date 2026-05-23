from flask import render_template, redirect, url_for, flash, session
from . import auth_login_bp, auth_register_bp
from .forms import LoginForm, RegisterForm

@auth_login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        pass
    return render_template('pages/login.html', form=form)

@auth_login_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        pass
    return render_template('pages/register.html', form=form)

# @auth_bp.route('/logout')
# def logout():
#     session.clear()
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('home.index'))