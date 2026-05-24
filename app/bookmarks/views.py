from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from app.constants import UserRole
from . import bookmarks_bp
from app.db import get_all_properties, get_properties_by_bookmark, delete_bookmarks



@bookmarks_bp.route('/')
def index():
    # query user's bookmarks list default using the userId and check the role if it's not tenant than redirect to homepage
    user_id = session.get('user_id')
    user_id = 3 # TEST@@@@@@@@@@@@@@@@@@@@@@@@
    if not user_id:
        #if user didn't log in redirect to login page
        return redirect(url_for('home.index'))
    
    user_role = session.get('role')
    user_role = UserRole.TENANT.value # TEST@@@@@@@@@@@@@@@@@@@@@@@@
    if user_role == UserRole.TENANT.value:
        # get tenant's bookmark list and get the properties in the list
        # properties = get_all_properties() # TEST@@@@@@@@@@@@@@@@@@@@@@@@
        Bookmarks = get_properties_by_bookmark(user_id)
        
        print('Bookmarks >', Bookmarks) # TEST@@@@@@@@@@@@@@@@@@@@@@@@
        
    else:
        return redirect(url_for('home.index'))
    return render_template('/pages/bookmarks.html', Bookmarks=Bookmarks)

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
