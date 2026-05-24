from flask import render_template, request, session, flash
from flask import redirect, url_for
from typing import List
from app.listings.forms import PropertyForm
from app.models import Property
from app.constants import UserRole
from app.db import add_property, delete_property, get_properties_by_agent, get_all_properties, update_property
from app.wrappers import role_required
from . import listings_bp


@listings_bp.route('/')
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def index():
    # at this stage, it should be guaranteed that the user logged in as agent or admin (the home page should only show the option to navigate to listings page if the user is agent or admin)

    # user_id = session.get('user_id') # need this id for query database
    properties: List[Property] = []
    form = PropertyForm() # form to render on modal
    # check if user logged in or not
    # if not user_id:
    #     # if user hasn't logged in -> redirect to login page
    #     # return redirect(url_for('auth.login'))

    #     # for now just render the listings page for testing (will be replace with the above return)
    #     return render_template('/pages/listings.html', listings = get_all_properties(), form=form, PropertyForm = PropertyForm)

    # check the user's role to render the corresponding properties.
    user_role = session['user']['user_role']
    if user_role == UserRole.AGENT.value:
        # query in database to get all properties managed by this agent
        properties = get_properties_by_agent(session['user']['user_id'])
    elif user_role == UserRole.ADMIN.value:
        # query in database to get all properties existing in the application
        properties = get_all_properties()

    return render_template('/pages/listings.html', listings = properties, form=form, PropertyForm = PropertyForm)

@listings_bp.post('/')
@role_required([UserRole.AGENT.value])
def create_property_listing():
    # admin is not able to create property listing, so in the UI, the button of adding property should not display when the user logged in as admin

    # check user role to make sure only agent can perform the post action
    # user_id = session.get('user_id') # need this id for query database
    # user_role = session.get('user_role')
    # if not user_id:
    #     return redirect(url_for('auth.login'))
    # if user_role == UserRole.TENANT.value:
    #     # if user is tenant, redirect to home page
    #     return redirect(url_for('home.index'))
    # if user_role == UserRole.AGENT.value:
    #     # only agent can perform the post action
    #     form = PropertyForm()    
    #     if form.validate_on_submit():
    #         # handle form stuff and query database to create new record
    #         flash('New property listing has beed added!')

    form = PropertyForm()
    
    
    if form.validate_on_submit():
        add_property(form, session['user']['user_id'])
        flash('New property listing has beed added!')

    return redirect(url_for('listings.index'))

@listings_bp.post('/<string:property_id>/edit')
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def edit_property_listing(property_id):
    # only admin and agent are allowed to perform edit action
    # user_role = session.get('user_role')
    # if not user_role:
    #     return redirect(url_for('auth.login'))
    # if user_role == UserRole.TENANT.value:
    #     # if user is tenant, redirect to home page
    #     return redirect(url_for('home.index'))
    
    form = PropertyForm()
    if form.validate_on_submit():
        # handle form stuff and query database based on property_id to edit record
        update_property(property_id=property_id, form=form)
        flash('Edited successful!')

    return redirect(url_for('listings.index'))

@listings_bp.route('/<string:property_id>/delete')
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def delete_property_listing(property_id):
    # only admin and agent are allowed to perform delete action
    # user_role = session.get('user_role')
    # if not user_role:
    #     return redirect(url_for('auth.login'))
    # if user_role == UserRole.TENANT.value:
    #     # if user is tenant, redirect to home page
    #     return redirect(url_for('home.index'))

    # query database based on property_id to delete record
    delete_property(property_id=property_id)
    flash('Deleted successful!')

    return redirect(url_for('listings.index'))

# need more routes for agent to view enquiries and update their status