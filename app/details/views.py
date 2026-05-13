from flask import Blueprint, render_template, flash, url_for
from . import details_bp

@details_bp.route("/details")
def details():
  return render_template('pages/details.html')
