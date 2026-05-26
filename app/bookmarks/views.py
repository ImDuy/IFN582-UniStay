from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from app.constants import UserRole
from . import bookmarks_bp
from app.db import get_bookmark_by_tenant, delete_bookmark_by_id
from app.wrappers import role_required


@bookmarks_bp.route('/')
@role_required([UserRole.TENANT.value])
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
        print('bookmarks', bookmarks)
    else:
        return redirect(url_for('home.index'))
    return render_template('/pages/bookmarks.html', bookmarks=bookmarks)

# redirect to bookmarks page when delete bookmarks
@bookmarks_bp.post('/<string:bookmark_id>/delete')
@role_required([UserRole.TENANT.value])
def delete_bookmark(bookmark_id):
    delete_bookmark_by_id(bookmark_id)
    flash('Deleted successful!')
    return redirect(url_for('bookmarks.index'))
# todo show tenant note
# todo edit note
