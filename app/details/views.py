from flask import Blueprint, render_temlplate, flash, url_for

@bp.route("/details")
def details():
  return render_template('details.html', properties = properties)
