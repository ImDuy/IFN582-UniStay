from flask import render_template, session, flash
from flask import redirect, url_for
from typing import List
from app.listings.forms import PropertyEnquiryForm, PropertyForm, PropertyOfferForm
from app.models import Property
from app.constants import UserRole
from app.db import add_property, delete_property, get_properties_by_agent, get_all_properties, update_enquiries_by_property, update_offers_by_property, update_property
from app.wrappers import login_required, role_required
from . import listings_bp


@listings_bp.route('/')
@login_required
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def index():
    # at this stage, it should be guaranteed that the user logged in as agent or admin (the home page should only show the option to navigate to listings page if the user is agent or admin)

    properties: List[Property] = []
    # check the user's role to render the corresponding properties.
    user_role = session['user']['user_role']
    if user_role == UserRole.AGENT.value:
        # query in database to get all properties managed by this agent
        properties = get_properties_by_agent(session['user']['user_id'])
    elif user_role == UserRole.ADMIN.value:
        # query in database to get all properties existing in the application
        properties = get_all_properties()

    edit_forms = {}
    enquiry_forms = {}
    offer_forms = {}
    for property in properties:
        # populate property data to edit forms
        edit_form = PropertyForm(obj=property) 
        edit_forms[property.id] = edit_form
        
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

    return render_template('/pages/listings.html', 
                           listings = properties, total_new_enquiries = Property.get_total_new_enquiries(properties), total_pending_offers = Property.get_total_pending_offers(properties),
                           edit_forms=edit_forms, add_form=PropertyForm(), enquiry_forms=enquiry_forms, offer_forms=offer_forms)

@listings_bp.post('/')
@login_required
@role_required([UserRole.AGENT.value])
def create_property_listing():
    # admin is not able to create property listing, so in the UI, the button of adding property should not display when the user logged in as admin
    form = PropertyForm()
    if form.validate_on_submit():
        add_property(form, session['user']['user_id'])
        flash('New property listing has beed added!')
    return redirect(url_for('listings.index'))

@listings_bp.post('/<string:property_id>/edit')
@login_required
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def edit_property_listing(property_id):
    form = PropertyForm()
    if form.validate_on_submit():
        update_property(property_id=property_id, form=form)
        flash('Edited successful!')
    return redirect(url_for('listings.index'))

@listings_bp.post('/<string:property_id>/delete')
@login_required
@role_required([UserRole.AGENT.value, UserRole.ADMIN.value])
def delete_property_listing(property_id):
    delete_property(property_id)
    flash('Deleted successful!')
    return redirect(url_for('listings.index'))

# routes for updating enquiries and offers status
@listings_bp.post('/<string:property_id>/update-enquiries')
@login_required
@role_required([UserRole.AGENT.value])
def update_property_enquiries(property_id):
    form = PropertyEnquiryForm()
    if form.validate_on_submit():
        print('update')
        update_enquiries_by_property(property_id=property_id, form=form)
        flash('Updated successful!')
    return redirect(url_for('listings.index'))
@listings_bp.post('/<string:property_id>/update-offers')
@login_required
@role_required([UserRole.AGENT.value])
def update_property_offers(property_id):
    form = PropertyOfferForm()
    if form.validate_on_submit():
        print('update')
        update_offers_by_property(property_id=property_id, form=form)
        flash('Updated successful!')
    return redirect(url_for('listings.index'))