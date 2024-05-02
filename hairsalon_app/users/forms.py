from flask_wtf import FlaskForm
from wtforms import DecimalField, EmailField, PasswordField, StringField, SubmitField, IntegerField, TelField
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
    pay_rate = IntegerField('pay_rate')
    specialty = StringField('specialty')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField('password', validators=[DataRequired()])
    new_password = PasswordField('confirm_password', validators=[DataRequired()])
    submit = SubmitField('Update Password')

class UpdateImageForm(FlaskForm):
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'webp'])])
    submit = SubmitField('Update Image')

    
