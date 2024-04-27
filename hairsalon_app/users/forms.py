from flask_wtf import FlaskForm
from wtforms import DecimalField, EmailField, PasswordField, StringField, SubmitField, IntegerField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed

class NewUserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=20)])
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=4, max=20)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    phone_number = TelField('phone_number', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0)])
    pay_rate = DecimalField('pay_rate',places=2)
    specialty = StringField('specialty')
    submit = SubmitField('Register')


# class NewProfressionalForm(FlaskForm):
#     username = StringField('username', validators=[DataRequired(), Length(min=4, max=20)])
#     full_name = StringField('full_name', validators=[DataRequired(), Length(min=4, max=20)])
#     email = EmailField('email', validators=[DataRequired(), Email()])
#     password = PasswordField('password', validators=[DataRequired()])
#     confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
#     user_image = FileField('user_image', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
#     phone_number = TelField('phone_number', validators=[DataRequired()])
#     address = StringField('address', validators=[DataRequired()])
#     age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0)])

#     submit = SubmitField('Register')

    
