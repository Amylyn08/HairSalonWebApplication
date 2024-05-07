from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

from hairsalon_app.qdb.database import db

#form to add report to a specific appointment
class ReportForm(FlaskForm):
    title = StringField('title', validators = [DataRequired(), Length(max=20)])
    client_report =  StringField('client_report', validators = [Length(max=100)])
    professional_report = StringField('professional_report', validators = [Length(max=100)])
    submit = SubmitField("Send report")
    
class ReportEdit(FlaskForm):
    title = StringField('title', validators = [DataRequired(), Length(max=20)])
    client_report =  StringField('client_report', validators = [Length(max=100)])
    professional_report = StringField('professional_report', validators = [Length(max=100)])
    submit = SubmitField("Edit report")