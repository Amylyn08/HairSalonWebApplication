from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed

class NewMemberForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=20)])
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])

class NewProfressionalForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=20)])
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])
    pay_rate = StringField('pay_rate', validators=[DataRequired()])

    
