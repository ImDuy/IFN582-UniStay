from flask import Blueprint, redirect, render_template, flash, url_for, session
from . import details_bp
from app import mysql
from app.wrappers import role_required
from app.constants import UserRole
from app.db import add_bookmark_by_id


@details_bp.route("/details/<int:property_id>")
def property_details(property_id):
    # Load property details
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM property WHERE id = %s", (property_id,))
    property_data = cursor.fetchone()
    if not property_data:
        flash("Property not found.", "danger")
        return redirect(url_for('home.index'))
    
    #Load img url from DB
    cursor.execute("SELECT url FROM propertyimage WHERE propertyId = %s and isPrimary = 1", (property_id,))
    primary_image = cursor.fetchone()
    
    #Load amenities
    cursor.execute("SELECT amenity FROM propertyamenity WHERE propertyId = %s", (property_id,))
    amenities = cursor.fetchall()
    
    #Compile property ID and university ID, then get distances
    uni_nearby ="""
    SELECT a.name, b.distance
    FROM nearby as b
    LEFT JOIN university as a ON b.universityId = a.id
    WHERE b.propertyId = %s
    """
    cursor.execute(uni_nearby, (property_id,))
    nearby_universities = cursor.fetchall()
    cursor.close()

    return render_template('pages/details.html', property=property_data, image=primary_image, amenities=amenities, nearby=nearby_universities)

@details_bp.route("details/<int:property_id>/add_bookmark", methods=['POST'])
@role_required([UserRole.TENANT.value])
def add_bookmark(property_id):
    tenant_id = session['user']['user_id']
    add_bookmark_by_id(tenant_id = tenant_id, property_id = property_id)
    flash('Added successful!')
    return redirect(url_for('details.property_details', property_id = property_id))



#Enquiry and offer
@details_bp.route("/details/<int:property_id>/enquiry", methods=['GET', 'POST'])
def property_enquiry(property_id):
    if True:
        flash("Please log in to submit an enquiry.", "warning")
        return redirect(url_for('auth_login.login'))
    
@details_bp.route("/details/<int:property_id>/offer", methods=['GET', 'POST'])
def property_offer(property_id):
    if True:
        flash("Please log in to make an offer.", "warning")
        return redirect(url_for('auth_login.login'))
