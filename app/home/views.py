from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for
from . import home_bp
from app.db import get_all_properties, get_nearby, get_properties_by_university, search_properties
from app import mysql

@home_bp.route('/')
def index():
    q = request.args.get('q', '').strip()
    cur = mysql.connection.cursor()

    if q:
        cur.execute("SELECT * FROM property WHERE title LIKE %s OR address LIKE %s",
                    (f'%{q}%',f'%{q}%')
        )
    else:
        cur.execute("SELECT * FROM property")
    all_properties = cur.fetchall()

    cur.execute("""
        SELECT p.* FROM property p
        JOIN nearby n ON p.id = n.propertyId
        JOIN university u ON n.universityId = u.id
        WHERE u.name = 'University of Queensland'
    """)
    uq_properties = cur.fetchall()

    cur.execute("""
        SELECT p.* FROM property p
        JOIN nearby n ON p.id = n.propertyId
        JOIN university u ON n.universityId = u.id
        WHERE u.name = 'QUT'
    """)
    qut_properties = cur.fetchall()

    cur.execute("""
        SELECT p.* FROM property p
        JOIN nearby n ON p.id = n.propertyId
        JOIN university u ON n.universityId = u.id
        WHERE u.name = 'Griffith University'
    """)
    griffith_properties = cur.fetchall()

    cur.execute("SELECT * FROM nearby")
    nearby = cur.fetchall()

    cur.close()

    return render_template('/pages/index.html',
        all_properties=all_properties,
        uq_properties=uq_properties,
        qut_properties=qut_properties,
        griffith_properties=griffith_properties,
        nearby = nearby
    )


@home_bp.route('/test-500')
def error():
    return render_template('/errors/500.html')