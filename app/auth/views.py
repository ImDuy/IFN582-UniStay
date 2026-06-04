from flask import render_template, redirect, url_for, flash, session, request
from app.utilities import hash_password
from . import auth_login_bp, auth_register_bp, auth_logout_bp
from .forms import LoginForm, RegisterForm
from app.db import get_user_by_email, user_exists_by_email, add_user
from app.wrappers import guest_required
import datetime


@auth_login_bp.route('/login', methods=['GET', 'POST'])
@guest_required
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        user = get_user_by_email(email)

        if user:
            user_id = user['id']
            stored_password = user['password']
            role = user['role']

            if stored_password == hash_password(form.password.data):
                session.clear()
                session['user'] = {'user_id': user_id,
                    'user_role': role}
                flash('Login successful.', 'success')
                return redirect(url_for('home.index'))

        flash('Invalid email or password.', 'danger')

    return render_template('pages/login.html', form=form)


@auth_register_bp.route('/register', methods=['GET', 'POST'])
@guest_required
def register():
    form = RegisterForm()
    selected_role = request.args.get('role', 'tenant')

    if form.validate_on_submit():
        email = form.email.data.strip().lower()

        existing_user = user_exists_by_email(email)
        if existing_user:
            flash('Email already exists.', 'danger')
            return render_template('pages/register.html', form=form, selected_role=selected_role)

        add_user(password=hash_password(form.password.data),
            first_name=form.first_name.data.strip(),
            last_name=form.last_name.data.strip(),
            email=email,
            phone=form.phone.data.strip(),
            avatar_url=None,
            role=form.role.data,
            date=datetime.datetime.now())

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth_login.login'))

    return render_template('pages/register.html', form=form, selected_role=selected_role)


@auth_logout_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home.index'))