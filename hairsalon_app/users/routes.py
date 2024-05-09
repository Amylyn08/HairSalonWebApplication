#Name : Iana Feniuc
#Section : 01
from flask import Blueprint, abort, current_app, flash, make_response, url_for, redirect, render_template,request
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from hairsalon_app.qdb.database import db
from flask_bcrypt import Bcrypt
import secrets
import os
from PIL import Image

from hairsalon_app.users.Member import Member
from hairsalon_app.users.User import User
from hairsalon_app.users.forms import LoginForm, NewUserForm, NewUserFormAdmin, UpdateProfileAdminForm, UpdateProfileForm, UpdateImageForm
#Create an instance of Database
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
                user = User(username=user_exists.username)
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
def edit_profile(username):
    form1 = UpdateImageForm()
    form = UpdateProfileForm()
    user = db.get_member(username=username)
    if request.method == 'POST':
        full_name = form.full_name.data if form.full_name.data else user.full_name
        email = form.email.data if form.email.data else user.email
        phone_number = form.phone_number.data if form.phone_number.data else user.phone_number
        address = form.address.data if form.address.data else user.address
        # Handle user_image file upload
        if form1.user_image.data:
            file_name = save_file(form1.user_image.data)  
        else:
            file_name = user.user_image
        if form.new_password.data and form.new_password.data :
            b = Bcrypt()
            if b.check_password_hash(user.password, form.old_password.data):
                b = Bcrypt()
                hashed_new_pass = b.generate_password_hash(form.new_password.data).decode('utf-8')
                password = hashed_new_pass
            else:
                flash('You inputed the wrong password for you account.Please input the information correctly!','error')
                password = user.password
        else:
            password = user.password
        db.update_profile(username=user.username,new_password= password, full_name=full_name, email=email,  phone_number=phone_number, address=address, user_image=file_name)
        flash('Successful update!','success')
        return redirect(url_for('users_bp.profile', username=user.username))
    return render_template('update_profile.html', form=form, form1=form1, users=user)

@users_bp.route('/profile/admin_edit/<username>/', methods=['GET', 'POST'])
def edit_profile_admin(username):
    form = UpdateProfileAdminForm()
    user = db.get_member(username=username)
    if form.validate_on_submit():
        if form.user_image.data:
            file_name = save_file(form.user_image.data)  
        else:
            file_name = user.user_image
        if form.new_password.data:
            b = Bcrypt()
            hashed_new_pass = b.generate_password_hash(form.new_password.data).decode('utf-8')
            password = hashed_new_pass
        else:
            password = user.password
        db.update_profile_admin(user_id=user.user_id, user_type=form.user_type.data, username=form.username.data, full_name=form.full_name.data,
                                new_password=password, email=form.email.data, phone_number=form.phone_number.data,
                                address=form.address.data, age=form.age.data, speciality=form.speciality.data,
                                pay_rate=form.pay_rate.data, user_image=file_name)
        flash('Successful update!', 'success')
        return redirect(url_for('users_bp.admin_pannel'))
    return render_template('edit_profile_admin.html', user=user, form=form)

@users_bp.route('/admin-pannel/', methods=['GET', 'POST'])
def admin_pannel():
    form = NewUserFormAdmin()
    if form.validate_on_submit():
        if form.user_image.data:
            file_name = save_file(form_file=form.user_image.data)
        else:
            file_name = 'default.png'
        member_exists = db.get_member(username=form.username.data)  
        if not member_exists:
            b = Bcrypt()
            hashed_pass = b.generate_password_hash(form.password.data).decode('utf-8')
            not_client_info = {'username': form.username.data,
                    'full_name': form.full_name.data,
                    'email': form.email.data,
                    'user_image': file_name,
                    'password': hashed_pass,
                    'phone': form.phone_number.data,
                    'address': form.address.data,
                    'age': form.age.data,
                    'speciality': form.specialty.data,
                    'payrate': form.pay_rate.data
                }
            if form.user_type.data == 'admin_user':
                db.add_new_admin_user(**not_client_info)
            elif form.user_type.data == 'admin_appoint':
                db.add_new_admin_appointment(**not_client_info)
            elif form.user_type.data == 'client':
                db.add_new_client(username=form.username.data, 
                            full_name=form.full_name.data,
                            email=form.email.data,
                            user_image=file_name,
                            password=hashed_pass, 
                            phone=form.phone_number.data,
                            address=form.address.data,
                            age=form.age.data)
            elif form.user_type.data == 'professional':
                db.add_new_pro(**not_client_info)
            else:
                flash('Please select a user type', 'error')
                if current_user.user_type == 'admin_super':
                    client_list = db.get_list_clients()
                    pro_list = db.get_all_users()
                    app_list = db.get_all_appointments()
                    return render_template('adminsuper_panel.html',
                                            clients=client_list, 
                                            employees=pro_list,
                                            appointments=app_list,
                                            form=form)
                else:
                    client_list = db.get_list_clients()
                    pro_list = db.get_list_pros()
                    return render_template('adminuser_panel.html', 
                                            clients=client_list,
                                            employees=pro_list,
                                            form=form)
            flash('User created successfully','success')
            if current_user.user_type == 'admin_super':
                client_list = db.get_list_clients()
                pro_list = db.get_all_users()
                app_list = db.get_all_appointments()
                return render_template('adminsuper_panel.html', 
                                       clients=client_list, 
                                       employees=pro_list, 
                                       appointments=app_list,
                                       form=form)
            else:
                client_list = db.get_list_clients()
                pro_list = db.get_list_pros()
                return render_template('adminuser_panel.html', 
                                       clients=client_list, 
                                       employees=pro_list,
                                       form=form)
        else:
            flash('This user already exists', 'error')
    if current_user.user_type == 'admin_super':
        client_list = db.get_list_clients()
        pro_list = db.get_all_users()
        app_list = db.get_all_appointments()
        return render_template('adminsuper_panel.html', 
                                clients=client_list, 
                                employees=pro_list, 
                                appointments=app_list,
                                form=form)
    else:
        client_list = db.get_list_clients()
        pro_list = db.get_list_pros()
        return render_template('adminuser_panel.html', 
                                clients=client_list, 
                                employees=pro_list,
                                form=form)

@users_bp.route('/adminsuper-pannel/delete-user/<string:username>/', methods=['GET', 'POST'])
def delete_user(username):
    user = db.get_member(username=username)
    if user is not None:
         db.delete_user(username=username)
         flash(f'User {username} has been deleted','success')
    else:
      flash('User does not exist', 'error')
    return redirect(url_for('users_bp.admin_pannel'))



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
    return redirect(url_for('users_bp.admin_pannel'))

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
    return redirect(url_for('users_bp.admin_pannel'))


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