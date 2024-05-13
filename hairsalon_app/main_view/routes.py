from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required
from hairsalon_app.qdb.database import db


main_bp = Blueprint('main_bp', __name__, template_folder='templates',static_folder='static', static_url_path='/main_view/static')

@main_bp.route('/')
@main_bp.route('/home/')
def home():
    list_services = db.services_cond()
    return render_template('home.html',services=list_services)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/member-home')
@login_required 
def member_home():
    list_services = db.services_cond()
    return render_template('home_member.html',services=list_services)

@main_bp.route('/api/')
def api_docs():
    return render_template('api_docs.html')




