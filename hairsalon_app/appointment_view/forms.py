from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from hairsalon_app.qdb.database import Database

db = Database()

pros_list = db.get_list_pros()
choices = [(pro.username, pro.username) for pro in pros_list]
#form to add Owner
class AppointmentForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()], render_kw={'readonly' : True})
    venue =  SelectField('venue', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators = [DataRequired()]) #to change
    date = DateField('date', validators = [DataRequired()])
    slot = SelectField('time', choices=[('1', '10-11'), ('2', '11-12'), ('3', '12-13')], validators = [DataRequired()])
    professional = SelectField('professional', choices=choices, validators = [DataRequired()]) #to change
    service = SelectField('service', choices=[('Trimming','Trimming')], validators = [DataRequired()]) #to change
    submit = SubmitField("Reserve")
