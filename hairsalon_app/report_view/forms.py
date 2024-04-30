from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from hairsalon_app.qdb.database import Database

db = Database()

#form to add report to a specific appointment
class ReportForm(FlaskForm):
    appointment_id = IntegerField('appointment_id', validators=[DataRequired()])
    title = StringField('title', validators = [DataRequired()])
    client_report =  StringField('client_report', validators = [DataRequired()])
    professional_report = StringField('professional_report', validators = [DataRequired()])
    member_type = SelectField('member_type', choices=[('0', '0'), ('1', '1')], validators = [DataRequired()])
    submit = SubmitField("Send report")
