from flask import Blueprint, render_temlplate, flash, url_for
from . import details.bp

@details_bp.route("/details/<property_id>")
def propety_details(property_id):

  return render_template('pages/details.html', property_id=property_id)
