from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, DecimalField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange, Optional

class jobForm(FlaskForm):
    serverIP = StringField('Syslog Server IP Address', validators=[DataRequired()])
    logFileName = StringField('Log Filename', validators=[DataRequired()])
    submit = SubmitField('Run Job')