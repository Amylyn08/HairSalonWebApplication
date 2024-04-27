#Name : Iana Feniuc
#Section : 01
from flask import Blueprint, current_app, flash, url_for, redirect, render_template
from hairsalon_app.qdb.database import Database
import secrets
import os
from PIL import Image

from hairsalon_app.users.forms import NewUserForm
#Create an instance of Database
db = Database()

#Create a blueprint
users_bp = Blueprint("user",__name__,template_folder='templates')

#List of users
users_clients= []
users_professionals =[]

#Generates all the 
@users_bp.route("/profile/client")
def user_list_client():
    """Function for listing all the users."""
    users_clients = db.get_users_clients()
    return render_template('allUsers.html', clients =users_clients)

@users_bp.route("/profile/professional")
def user_list_professional():
    """Function for listing all the users."""
    users_professionals= db.get_users_professional()
    return render_template('allUsers.html', profesionnals = users_professionals)

@users_bp.route("/profile/<username>")
def client_name(username):
    """Function for finding a client by his username."""
    users_clients = db.get_users_clients()
    for client in users_clients:
        if client.username == username:
            return render_template('client.html', clients = client)
    flash("Sorry but this address doesn't exist !","errors_class")
    return redirect(url_for('user_list_client'))

@users_bp.route("/profile/<username>")
def professional_name(username):
    """Function for finding a client by his username."""
    users_professionals = db.get_users_professional()
    for professional in users_professionals:
        if professional.username == username:
            return render_template('professional.html', professionals= professional)
    flash("Sorry but this address doesn't exist !","errors_class")
    return redirect(url_for('user_list_professional'))

@users_bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = NewUserForm()
    if form.password.data != form.retype_password.data: 
        flash('Passwords do not match!', 'error')
    if form.validate_on_submit():
        #checks if this user already exists
        

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