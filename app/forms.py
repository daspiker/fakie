from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, DecimalField, FileField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange, Optional, InputRequired
from app.models import SyslogSettings, ApiSettings

class syslogForm(FlaskForm):
    syslogCollector = SelectField('Syslog Collector', validate_choice=False)
    syslogLogFileName = SelectField('Syslog Filename', validate_choice=False)
    submit = SubmitField('Run Syslog Job')

class apiForm(FlaskForm):
    apiWorkspace = SelectField('API Workspace', validate_choice=False)
    tableName = StringField('Table Name', validators=[DataRequired()])
    apiLogFileName = SelectField('API Filename', validate_choice=False)
    submit = SubmitField('Run API Job')

class syslogSettingsForm(FlaskForm):
    serverIP = StringField('Syslog Server Hostname or IP Address', validators=[DataRequired()])
    comment = StringField('Comment', validators=[Optional()])
    submit = SubmitField('Save Syslog Settings')

class apiSettingsForm(FlaskForm):
    workspaceId = StringField('Sentinel Workspace ID', validators=[DataRequired()])
    workspaceKey = StringField('Sentinel Workspace Key', validators=[DataRequired()])
    comment = StringField('Comment', validators=[Optional()])
    submit = SubmitField('Save API Settings')