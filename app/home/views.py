from flask import render_template, request, session, flash
from flask import redirect, url_for

@home.route('/')
def index():
    return render_template('index.html')