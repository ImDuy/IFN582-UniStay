from flask import Blueprint, redirect, render_template, flash, url_for, session, request
from . import details_bp
from app import mysql
from app.wrappers import role_required
from app.constants import UserRole
from app.db import add_bookmark_by_id, add_enquiry, add_offer, bookmark_overlap, check_enquiry, check_has_bookmark, check_offer, get_property_by_id, get_uni_nearby
from .forms import EnquiryForm

@details_bp.route("/details/<int:property_id>")
def property_details(property_id):
    # Load property details
    prop = get_property_by_id(property_id)
    if not prop:
        flash("Property not found.", "danger")
        return redirect(url_for('home.index'))
    
    nearby_list = get_uni_nearby(property_id)
    enquiry_form = EnquiryForm()

    has_enquiry = False
    has_offer = False
    has_bookmark = False
    if session.get('user'):
        tenant_id = session['user']['user_id']
        has_enquiry = check_enquiry(tenant_id, property_id)
        has_offer = check_offer(tenant_id, property_id)
        has_bookmark = check_has_bookmark(tenant_id, property_id)
        
    return render_template('pages/details.html',
        property=prop,
        nearby_list=nearby_list,
        has_enquiry=has_enquiry,
        has_offer=has_offer,
        has_bookmark=has_bookmark,
        enquiry_form=enquiry_form
    )

@details_bp.route("/details/<int:property_id>/add_bookmark", methods=['POST'])
@role_required([UserRole.TENANT.value])
def add_bookmark(property_id):
    tenant_id = session['user']['user_id']
    check = bookmark_overlap(tenant_id, property_id)
    if check:
        flash('Already bookmarked!', 'danger')
        return redirect(url_for('details.property_details', property_id=property_id))
    add_bookmark_by_id(tenant_id = tenant_id, property_id = property_id)
    flash('Added successful!', 'success')
    return redirect(url_for('details.property_details', property_id = property_id))

#Enquiry and offer
@details_bp.route("/details/<int:property_id>/enquiry", methods=['POST'])
@role_required([UserRole.TENANT.value])
def property_enquiry(property_id):
    tenant_id = session['user']['user_id']
    if check_enquiry(tenant_id, property_id):
        flash("Already enquired!", "warning")
        return redirect(url_for('details.property_details', property_id=property_id))
    add_enquiry(tenant_id, property_id, request.form.get('message'))
    flash("Enquiry sent!", "success")
    return redirect(url_for('details.property_details', property_id=property_id))

@details_bp.route("/details/<int:property_id>/offer", methods=['POST'])
@role_required([UserRole.TENANT.value])
def property_offer(property_id):
    tenant_id = session['user']['user_id']
    if check_offer(tenant_id, property_id):
        flash("Already offered!", "warning")
        return redirect(url_for('details.property_details', property_id=property_id))
    add_offer(tenant_id, property_id)
    flash("Offer sent!", "success")
    return redirect(url_for('details.property_details', property_id=property_id))
