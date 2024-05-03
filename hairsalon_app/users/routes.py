#Name : Iana Feniuc
#Section : 01
from flask import Blueprint, abort, current_app, flash, make_response, url_for, redirect, render_template
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from hairsalon_app.qdb.database import Database
from flask_bcrypt import Bcrypt
import secrets
import os
from PIL import Image

from hairsalon_app.users.Member import Member
from hairsalon_app.users.User import User
from hairsalon_app.users.forms import LoginForm, NewUserForm, UpdatePasswordForm, UpdateImageForm
#Create an instance of Database
db = Database()
login_manager = LoginManager()

#Create a blueprint
users_bp = Blueprint("users_bp",__name__,template_folder='templates', static_folder='static', static_url_path='/users/static')

#List of users
users_clients= []
users_professionals =[]

#Generates all the 
@users_bp.route("/allUsers/")
def user_list_client():
    """Function for listing all the users."""
    users_clients = db.get_users()
    return render_template('Users.html', clients =users_clients)

@users_bp.route('/adminsuper-pannel/')
def adminsuper_pannel():
    client_list = db.get_list_clients()
    pro_list = db.get_list_pros()
    app_list = db.get_all_appointments()

    return render_template('adminsuper_panel.html', clients=client_list, employees=pro_list, appointments=app_list)

@users_bp.route('/adminuser-pannel/')
def adminuser_pannel():
    client_list = db.get_list_clients()
    pro_list = db.get_list_pros()
    return render_template('adminuser_panel.html', clients=client_list, employees=pro_list)

@users_bp.route('/adminappoint-pannel/')
def adminappoint_pannel():
    app_list = db.get_all_appointments()
    return render_template('adminappoint_panel.html', appointments=app_list)

@users_bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = NewUserForm()
    if form.password.data != form.confirm_password.data: 
        flash('Passwords do not match!', 'error')
    elif form.validate_on_submit():
        # Check if this user already exists
        if form.user_image.data:
            file_name = save_file(form_file=form.user_image.data)
        else:
            file_name = 'default.png'
        member_exists = db.get_member(username=form.username.data)
        if not member_exists:
            b = Bcrypt()
            hashed_pass = b.generate_password_hash(form.password.data).decode('utf-8')
            if form.pay_rate.data is not None and form.specialty.data is not None:
                db.add_new_pro(username=form.username.data, 
                                        full_name=form.full_name.data,
                                        email=form.email.data,
                                        user_image=file_name,
                                        password=hashed_pass, 
                                        phone=form.phone_number.data,
                                        address=form.address.data,
                                        age=form.age.data, 
                                        speciality=form.specialty.data,
                                        payrate=form.pay_rate.data)
            else:
                db.add_new_client(username=form.username.data, 
                                    full_name=form.full_name.data,
                                    email=form.email.data,
                                    user_image=file_name,
                                    password=hashed_pass, 
                                    phone=form.phone_number.data,
                                    address=form.address.data,
                                    age=form.age.data)
            flash('Successful registration! Please Login to continue...', 'success')
            return redirect(url_for('users_bp.login'))
        else:
            flash('This account already exists.', 'error')
    return render_template('register.html', form=form)  #redirect to login page???

@users_bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_exists = db.get_member(username=form.username.data)
        if user_exists:
            if user_exists.is_active[0] == 1:
                flash('Your account has been deactivated by the admin. Please contact us.', 'error')
                return redirect(url_for('main_bp.home'))
            b = Bcrypt()
            password_hashed = user_exists.password
            if b.check_password_hash(password_hashed, form.password.data):
                user = User(username=user_exists.username, user_id=user_exists.user_id,user_type=user_exists.user_type)
                login_user(user)
                if user_exists.status == 1:
                    flash('Your account has been flagged. You are actions are being monitored.', 'info')
                flash(f'Success: Logged in as {form.username.data}', 'success')
                return redirect(url_for('main_bp.member_home'))
        flash ('Invalid password or username. Retry', 'error')        
    return render_template('login.html', form=form)

#route to profile
@users_bp.route('/profile/<username>/')
@login_required
def profile(username):
    user = db.get_member(username=username)
    return render_template('Profile.html', users=user)

@users_bp.route('/profile/edit/<username>/', methods=['GET', 'POST'])
def edit_password(username):
    form = UpdatePasswordForm()
    user = db.get_member(username=username)
    if form.validate_on_submit():
        b = Bcrypt()
        #hashed_old_pass = b.generate_password_hash(form.old_password.data).decode('utf-8')
        if b.check_password_hash(user.password, form.old_password.data):
            b = Bcrypt()
            hashed_new_pass = b.generate_password_hash(form.new_password.data).decode('utf-8')
            db.update_password(username=user.username,new_password= hashed_new_pass)
            flash('Successful update!','success')
            redirect(url_for('users_bp.profile', username=user.username))
        else:
            flash('Please input the information correctly!','error')
    return render_template('update_profile.html', form=form, users=user)

@users_bp.route('/profile/editimage/<username>/', methods=['GET', 'POST'])
def edit_image(username):
    form = UpdateImageForm()
    user = db.get_member(username=username)
    if form.validate_on_submit():
        file_name = save_file(form_file=form.user_image.data)
        db.update_image(username=user.username, user_image=file_name)
        flash('Successful update!','success')
        redirect(url_for('users_bp.profile', username=user.username))
    else:
        flash('Please input the information correctly!','error')
    return render_template('image_update.html', form=form, users=user)
        

#route for and function for logout.
@users_bp.route('/logout/', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully", "success")
    return redirect(url_for('main_bp.home'))

@users_bp.route('/toggle_active/<string:username>/', methods=['GET','POST'])
def toggle_active_user(username):
    active = db.get_active(username=username)
    if active == 0:
        active = 1
        flash(f'User {username} has been deactivated', 'success')
    else:
        active = 0
        flash(f'User {username} has been activated', 'success')
    
    db.set_active(username=username, active=active)
    return redirect(url_for('users_bp.adminsuper_pannel'))

@users_bp.route('/toggle_flag/<string:username>/', methods=['GET','POST'])
def toggle_flag(username):
    flag = db.get_flag(username=username)
    if flag == 0:
        flag = 1
        flash(f'User {username} has been flagged', 'success')
    else:
        flag = 0
        flash(f'User {username} has been unflagged', 'success')
    db.set_flag(username=username, status=flag)
    return make_response({}, 204)


def save_file(form_file):
    random_file_name  = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_file.filename)
    new_filename = random_file_name+f_ext

    new_file_path = os.path.join(current_app.root_path, 'static/images/user-pics', new_filename)

    i = Image.open(form_file) #opens actual file
    image_new_size = (150,150)
    i.thumbnail(image_new_size) #resizes the actual file down to 150

    i.save(new_file_path) #resized file is saved with the absolute filename

    return new_filename