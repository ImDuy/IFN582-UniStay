from flask import Blueprint, render_temlplate, flash, url_for
from . import details.bp

@details_bp.route("/details")
def details():
  return render_template('pages/details.html')
