from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from hairsalon_app.qdb.database import db

pros_list = db.get_list_pros()
choices = [(pro.username, pro.username) for pro in pros_list]
# form to add Owner
class AppointmentForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()], render_kw={'readonly' : True})
    venue =  SelectField('venue', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators = [DataRequired()]) #to change
    date = DateField('date', validators = [DataRequired()])
    slot = SelectField('time', choices=[('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], validators = [DataRequired()])
    professional = SelectField('professional', choices=choices, validators = [DataRequired()]) #to change
    service = SelectField('service', choices=[('Trimming','Trimming')], validators = [DataRequired()]) #to change
    submit = SubmitField("Reserve")

class AppointmentEditForm(FlaskForm):
    date = DateField('date', validators = [DataRequired()])
    slot = SelectField('time', choices=[('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], validators = [DataRequired()])
    service = SelectField('service', choices=[('Trimming','Trimming')], validators = [DataRequired()]) #to change
    status = SelectField('status', choices=[('pending','pending'), ('cancelled', 'cancelled')], validators = [DataRequired()])
    submit = SubmitField("Edit")
