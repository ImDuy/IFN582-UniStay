from flask import Blueprint, redirect, render_template, flash, url_for, session, request
from . import details_bp
from app import mysql
from app.wrappers import role_required
from app.constants import UserRole
from app.db import add_bookmark_by_id, bookmark_overlap, get_property, get_img_url, get_amenities, get_uni_nearby, enquiry, offer

@details_bp.route("/details/<int:property_id>")
def property_details(property_id):
    # Load property details
    property_data = get_property(property_id)
    if not property_data:
        flash("Property not found.", "danger")
        return redirect(url_for('home.index'))
    #Load img url from DB
    primary_image = get_img_url(property_id)
    #Load amenities
    amenities = get_amenities(property_id)
    #Compile property ID and university ID, then get distances
    uni_nearby = get_uni_nearby(property_id)
    return render_template('pages/details.html', property=property_data, image=primary_image, amenities=amenities, nearby=uni_nearby)

@details_bp.route("details/<int:property_id>/add_bookmark", methods=['POST'])
@role_required([UserRole.TENANT.value])
def add_bookmark(property_id):
    tenant_id = session['user']['user_id']
    check = bookmark_overlap(tenant_id, property_id)
    if check:
        flash('Already bookmarked!')
        return redirect(url_for('details.property_details', property_id=property_id))
    add_bookmark_by_id(tenant_id = tenant_id, property_id = property_id)
    flash('Added successful!')
    return redirect(url_for('details.property_details', property_id = property_id))

#Enquiry and offer
@details_bp.route("/details/<int:property_id>/enquiry", methods=['POST'])
@role_required([UserRole.TENANT.value])
def property_enquiry(property_id):
    tenant_id = session['user']['user_id']
    enquiry_message = request.form.get('message')
    check = enquiry(tenant_id, property_id, enquiry_message)
    if not check:
        flash("You have already made an enquiry for this property!", "warning")
    else:
        flash("Enquiry sent successfully!", "success")
    return redirect(url_for('details.property_details', property_id=property_id))

@details_bp.route("/details/<int:property_id>/offer", methods=['POST'])
@role_required([UserRole.TENANT.value])
def property_offer(property_id):
    tenant_id = session['user']['user_id']
    check = offer(tenant_id, property_id)
    if not check:
        flash("You have already made an offer for this property!", "warning")
    else:
        flash("Offer sent successfully!", "success")
    return redirect(url_for('details.property_details', property_id=property_id))
