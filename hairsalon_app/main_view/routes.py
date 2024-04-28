from flask import Blueprint, flash, redirect, render_template, url_for


main_bp = Blueprint('main_bp', __name__, template_folder='templates')

#db = Database()

@main_bp.route('/')
@main_bp.route('/home/')
def home():
    return render_template('home.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/member-home')
def member_home():
    return render_template('home_member.html')


@main_bp.route('/adminsuper-home/')
def adminsuper_home():
    return render_template('home_adminsuper.html')

@main_bp.route('/adminappoint-home/')
def adminappoint_home():
    return render_template('home_adminappoint.html')
@main_bp.route('/adminuser-home/')
def adminuser_home():
    return render_template('home_adminuser.html')




