from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, DecimalField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange, Optional

class syslogForm(FlaskForm):
    serverIP = StringField('Syslog Server IP Address', validators=[DataRequired()])
    syslogLogFileName = StringField('Log Filename', validators=[DataRequired()])
    submit = SubmitField('Run Syslog Job')

class apiForm(FlaskForm):
    workspaceId = StringField('Sentinel Workspace ID', validators=[DataRequired()])
    workspaceKey = StringField('Sentinel Workspace Key', validators=[DataRequired()])
    tableName = StringField('Table Name', validators=[DataRequired()])
    apiLogFileName = StringField('Log Filename', validators=[DataRequired()])
    submit = SubmitField('Run API Job')