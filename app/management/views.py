from flask import render_template, request, session, flash
from flask import redirect, url_for
from typing import List
from app.management.forms import AccountForm, PropertyEnquiryForm, PropertyForm, PropertyOfferForm
from app.models import Property
from app.constants import UserRole
from app.db import add_property, add_user, delete_property, delete_user, get_all_properties, get_properties_by_agent, get_property_by_id, get_users_except_admin, update_enquiries_by_property, update_offers_by_property, update_property
from app.wrappers import login_required, role_required
from . import management_bp

# this build get route context function is reused in post route
# the reason we created this function is to reuse the logic of passing data to template and keep the form errors in the post route when validation fails
def build_get_route_context():
    pass

@management_bp.route('/')
@login_required
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def index():
    properties: List[Property] = []
    # check the user's role to render the associated content.
    user_role = session['user']['user_role']
    if user_role == UserRole.ADMIN.value:
        properties = get_all_properties()
        user_accounts = get_users_except_admin()
        return render_template('/pages/management.html', listings = properties, user_accounts= user_accounts, user_role = user_role, UserRole = UserRole)
    
    # if the user is agent --------
    properties = get_properties_by_agent(session['user']['user_id'])
    # create forms for updating offer/enquiry status
    enquiry_forms = {}
    offer_forms = {}
    for property in properties:
        # populate enquiry data to enquiry forms
        enquiry_form = PropertyEnquiryForm()
        for enquiry in property.enquiries:
            # populate data to nested form
            entry = enquiry_form.enquiries.append_entry()
            entry.form.tenant_id.data = enquiry.sender.id
            entry.form.status.data = enquiry.status.value
        enquiry_forms[property.id] = enquiry_form

        # populate offer data to offer forms
        offer_form = PropertyOfferForm()
        for offer in property.offers:
            # populate data to nested form
            entry = offer_form.offers.append_entry()
            entry.form.tenant_id.data = offer.sender.id
            entry.form.status.data = offer.status.value
        offer_forms[property.id] = offer_form
    return render_template('/pages/management.html', listings = properties, user_role = user_role, UserRole = UserRole, 
                           total_new_enquiries = Property.get_total_new_enquiries(properties), total_pending_offers = Property.get_total_pending_offers(properties), 
                           enquiry_forms = enquiry_forms, offer_forms = offer_forms)
    
# routes for creating, editing, and deleting property listings
@management_bp.route('/create-listing',  methods=['POST', 'GET'])
@login_required
@role_required([UserRole.AGENT.value])
def create_property_listing():
    form = PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            add_property(form, session['user']['user_id'])
            flash('New property listing has been added!')
            return redirect(url_for('management.index'))
    return render_template('/pages/property_form.html', form= form)

@management_bp.route('/listings/<string:property_id>/edit', methods=['POST', 'GET'])
@login_required
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def edit_property_listing(property_id):
    form = PropertyForm()
    property = get_property_by_id(property_id)

    if request.method == 'POST':
        if form.validate_on_submit():
            update_property(property_id=property_id, form=form)
            flash('Edited successful!')
            return redirect(url_for('management.index'))
    else: # --- for GET, populate the data to the form
        form = PropertyForm(obj= property)
        
    return render_template('/pages/property_form.html', form=form, property = property)

@management_bp.post('/listings/<string:property_id>/delete')
@login_required
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def delete_property_listing(property_id):
    delete_property(property_id)
    flash('Deleted successful!')
    return redirect(url_for('management.index'))

# routes for updating enquiries and offers status
@management_bp.post('/listings/<string:property_id>/update-enquiries')
@login_required
@role_required([UserRole.AGENT.value])
def update_property_enquiries(property_id):
    form = PropertyEnquiryForm()
    if form.validate_on_submit():
        update_enquiries_by_property(property_id=property_id, form=form)
        flash('Updated successful!')
    return redirect(url_for('management.index'))
@management_bp.post('/listings/<string:property_id>/update-offers')
@login_required
@role_required([UserRole.AGENT.value])
def update_property_offers(property_id):
    form = PropertyOfferForm()
    if form.validate_on_submit():
        update_offers_by_property(property_id=property_id, form=form)
        flash('Updated successful!')
    return redirect(url_for('management.index'))

# routes for creating and deleting user accounts
@management_bp.route('/create-account',  methods=['POST', 'GET'])
@login_required
@role_required([UserRole.ADMIN.value])
def create_user_account():
    form = AccountForm()
    if form.validate_on_submit():
        add_user(form)
        flash('New user account has been added!')
        return redirect(url_for('management.index'))
    return render_template('/pages/account_form.html', form=form)

@management_bp.post('accounts/<string:account_id>/delete')
@login_required
@role_required([UserRole.ADMIN.value])
def delete_user_account(account_id):
    delete_user(account_id)
    flash('Deleted successful!')
    return redirect(url_for('management.index'))