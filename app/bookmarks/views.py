from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from app.constants import UserRole
from . import bookmarks_bp
from app.db import get_bookmark_by_tenant, delete_bookmarks



@bookmarks_bp.route('/')
def index():
    # query user's bookmarks list default using the userId and check the role if it's not tenant than redirect to homepage
    user_id = session['user']['user_id']
    if not user_id:
        #if user didn't log in redirect to login page
        return redirect(url_for('home.index'))
    
    user_role = session['user']['user_role']
    print('user_role >', user_role)
    if user_role == UserRole.TENANT.value:
        # get tenant's bookmark list and get the properties in the list
        bookmarks = get_bookmark_by_tenant(user_id)
    else:
        return redirect(url_for('home.index'))
    return render_template('/pages/bookmarks.html', bookmarks=bookmarks)

# view button direct to detailpage
@bookmarks_bp.post('/')
def view_detail():
    return redirect(url_for('bookmarks.index')) # get propertyid and direct to detailpage




# redirect to bookmarks page when delete bookmarks
@bookmarks_bp.post('/')
def delete_bookmarks(property_id):
    
    
    return redirect(url_for('bookmarks.index'))
# todo show tenant note
# todo edit note
