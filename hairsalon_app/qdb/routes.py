from flask import Blueprint, flash, redirect, render_template, url_for
from flask_bcrypt import Bcrypt
from hairsalon_app.qdb.database import Database

owner = Blueprint('owner',__name__, template_folder='templates')
db = Database()

# #route and function for listing all owners.
# @owner.route('/owners/', methods=['GET', 'POST'])
# def list_owners():
#     owners_list  = db.get_owners()
#     return render_template('owners.html', context_data=owners_list)

# #route and function for registering 
# @owner.route('/register/', methods=['GET', 'POST'])
# def register():
#     form = NewOwnerForm()
#     if form.password.data != form.retype_password.data:
#         flash('Passwords do not match!', 'error')
#     if form.validate_on_submit():
#         #checking if password match
#         #checking if the owner exists from the database.
#         owner_exists = db.get_owner(form.username.data)
#         #if the owner does not exist, then creating the new owner and putting in db.
#         if not owner_exists:
#             b = Bcrypt()
#             hashed_pass = b.generate_password_hash(form.password.data).decode('utf-8')
#             db.add_new_owner(username=form.username.data, owner_name=form.owner_name.data,
#                                 email=form.email.data, password=hashed_pass, occupation=form.occupation.data)
#             flash('Successful registration! Login to continue', 'success')
#             return redirect(url_for('main.login'))
#         else:
#             flash('You cannot register an owner that already exists', 'error')
#     return render_template('register.html', form=form)





            


