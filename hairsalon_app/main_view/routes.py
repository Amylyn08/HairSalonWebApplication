from flask import Blueprint, flash, redirect, render_template, url_for
from hairsalon_app.services.routes import get_services

main_bp = Blueprint('main_bp', __name__, template_folder='templates',static_folder='static', static_url_path='/main_view/static')

@main_bp.route('/')
@main_bp.route('/home/')
def home():
    list_services = get_services()
    return render_template('home.html',services=list_services)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/member-home')
def member_home():
    list_services = get_services()
    return render_template('home_member.html',services=list_services)


@main_bp.route('/adminsuper-home/')
def adminsuper_home():
    return render_template('home_adminsuper.html')

@main_bp.route('/adminappoint-home/')
def adminappoint_home():
    return render_template('home_adminappoint.html')
@main_bp.route('/adminuser-home/')
def adminuser_home():
    return render_template('home_adminuser.html')




