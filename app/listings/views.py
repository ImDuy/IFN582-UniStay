from flask import render_template, request, session, flash
from flask import redirect, url_for
from typing import List
from app.models import Property
from app.constants import UserRole
from app.db import get_properties_by_agent, get_all_properties
from . import listings_bp
from .forms import AddPropertyForm, EditPropertyForm


@listings_bp.route('/')
def index():
    # at this stage, it should be guaranteed that the user logged in as agent or admin (the home page should only show the option to navigate to listings page if the user is agent or admin)

    # get user id from session
    user_id = session.get('user_id') # need this id for query database
    properties: List[Property] = []
    # check if user logged in or not
    if not user_id:
        # if user hasn't logged in -> redirect to login page
        # return redirect(url_for('auth.login'))

        # for now just render the listings page for testing (will be replace with the above return)
        return render_template('/pages/listings.html', listings = properties)

    # check user role
    user_role = session.get('role') 
    if user_role == UserRole.TENANT:
        # if user is tenant, redirect to home page
        return redirect(url_for('home.index'))
    if user_role == UserRole.AGENT:
        # query in database to get all properties managed by this agent
        properties = get_properties_by_agent(user_id)
    elif user_role == UserRole.ADMIN:
        # query in database to get all properties existing in the application
        properties = get_all_properties()
    return render_template('/pages/listings.html', listings = properties)

@listings_bp.post('/')
def create_property_listing():
    # admin is not able to create property listing, so in the UI, the button of adding property should not display when the user logged in as admin

    # check user role to make sure only agent can perform the post action
    user_id = session.get('user_id') # need this id for query database
    user_role = session.get('user_role')
    if not user_id:
        return redirect(url_for('auth.login'))
    if user_role == UserRole.TENANT:
        # if user is tenant, redirect to home page
        return redirect(url_for('home.index'))
    if user_role == UserRole.AGENT:
        # only agent can perform the post action
        form = AddPropertyForm()    
        if form.validate_on_submit():
            # handle form stuff and query database to create new record
            flash('New property listing has beed added!')

    return redirect(url_for('listings.index'))

@listings_bp.post('/<int:property_id>/edit')
def edit_property_listing(property_id):
    # only admin and agent are allowed to perform edit action
    user_role = session.get('user_role')
    if not user_role:
        return redirect(url_for('auth.login'))
    if user_role == UserRole.TENANT:
        # if user is tenant, redirect to home page
        return redirect(url_for('home.index'))

    form = EditPropertyForm()
    if form.validate_on_submit():
        # handle form stuff and query database based on property_id to edit record
        flash('Edited successful!')

    return redirect(url_for('listings.index'))

@listings_bp.post('/<int:property_id>/delete')
def delete_property_listing(property_id):
    # only admin and agent are allowed to perform delete action
    user_role = session.get('user_role')
    if not user_role:
        return redirect(url_for('auth.login'))
    if user_role == UserRole.TENANT:
        # if user is tenant, redirect to home page
        return redirect(url_for('home.index'))

    # query database based on property_id to delete record
    flash('Deleted successful!')

    return redirect(url_for('listings.index'))

# need more routes for agent to view enquiries and update their status