from flask import session, redirect, flash, url_for
from functools import wraps

# Decorator to check if the user logged in
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in before moving on.', 'error')
            return redirect(url_for('auth_login.login'))
        if not session['user'].get('user_role') or not session['user'].get('user_id'):
            raise Exception("Something wrong occur!\nUser already logged in but missing user id or user role")
        return func(*args, **kwargs)
    return wrapper

# Decorator to check user role. Accepts a list of roles as parameter
def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if session['user']['user_role'] not in allowed_roles:
                flash('You do not have permission to view this page.', 'error')
                return redirect(url_for('home.index'))
            return func(*args, **kwargs)
        return wrapper
    return decorator
