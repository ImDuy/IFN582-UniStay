from flask import Blueprint, render_temlplate, flash, url_for
from . import details.bp

@bp.route("/details")
def details():
  return render_template('details.html', properties = properties)
