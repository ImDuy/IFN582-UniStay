import hashlib
from flask import render_template, redirect, url_for, flash, session, request
from . import auth_login_bp, auth_register_bp
from .forms import LoginForm, RegisterForm
from app import mysql

def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

@auth_login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT id, username, password, role FROM user WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()
        cursor.close()

        print("USER:", user)

        if user:
            user_id = user['id']
            username = user['username']
            stored_password = user['password']
            role = user['role']

            print("STORED:", stored_password)
            print("ENTERED HASH:", hash_password(form.password.data))
            print("ROLE:", role)

            if stored_password == hash_password(form.password.data):
                session.clear()
                session['user'] = {
                    'user_id': user_id,
                    'user_role': role,
                    'username': username
                }
                flash('Login successful.', 'success')
                return redirect(url_for('home.index'))

        flash('Invalid email or password.', 'danger')

    return render_template('pages/login.html', form=form)


@auth_register_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    selected_role = request.args.get('role', 'tenant')

    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id FROM user WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            flash('Email already exists.', 'danger')
            return render_template('pages/register.html', form=form, selected_role=selected_role)

        cursor.execute(
            """
            INSERT INTO user (username, password, firstName, lastName, email, phone, avatarUrl, role)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                form.username.data.strip(),
                hash_password(form.password.data),
                form.first_name.data.strip(),
                form.last_name.data.strip(),
                email,
                form.phone.data.strip(),
                None,
                form.role.data.lower()
            )
        )
        mysql.connection.commit()
        cursor.close()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth_login.login'))

    return render_template('pages/register.html', form=form, selected_role=selected_role)