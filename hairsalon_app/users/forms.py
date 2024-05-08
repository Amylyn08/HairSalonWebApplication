from flask_wtf import FlaskForm
from wtforms import DecimalField, EmailField, PasswordField, SelectField, StringField, SubmitField, IntegerField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed


class NewUserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4)])
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=4)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'webp'])])
    phone_number = TelField('phone_number', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0)])
    pay_rate = DecimalField('pay_rate')
    specialty = StringField('specialty')
    submit = SubmitField('Register')

class NewUserFormAdmin(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4)])
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=4)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'webp'])])
    phone_number = TelField('phone_number', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0)])
    pay_rate = DecimalField('pay_rate', default=0)
    specialty = StringField('specialty')
    user_type = SelectField('user_type', choices=[
    ('', '--Please select an option--'),
    ('admin_user', 'Admin User'),
    ('admin_appoint', 'Admin Appoint'),
    ('client', 'Client'),
    ('professional', 'Professional')
    ], default='')
    submit = SubmitField('Create User')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UpdateProfileForm(FlaskForm):
    full_name = StringField('full_name')
    old_password = PasswordField('password')
    new_password = PasswordField('confirm_password')
    email = EmailField('email', validators=[Email()])
    phone_number = TelField('phone_number')
    address = StringField('address')
    submit = SubmitField('Update info')
    
class UpdateProfileAdminForm(FlaskForm):
    user_type = StringField('user_type')
    username = StringField('username')
    full_name = StringField('full_name')
    new_password = PasswordField('confirm_password')
    email = EmailField('email', validators=[Email()])
    phone_number = TelField('phone_number')
    address = StringField('address')
    age = IntegerField('age')
    speciality = StringField('specialty')
    pay_rate = DecimalField('pay_rate')
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'webp'])])
    submit = SubmitField('Update info')

class UpdateImageForm(FlaskForm):
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'webp'])])
    submit = SubmitField('Update image')
    
