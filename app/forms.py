from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, DecimalField, FileField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange, Optional, InputRequired
from app.models import SyslogSettings, ApiSettings

class syslogForm(FlaskForm):
    serverIP = StringField('Syslog Server Hostname or IP Address', validators=[DataRequired()])
    syslogLogFileName = SelectField('SyslogFilename', validate_choice=False)
    submit = SubmitField('Run Syslog Job')

class apiForm(FlaskForm):
    workspaceId = StringField('Sentinel Workspace ID', validators=[DataRequired()])
    workspaceKey = StringField('Sentinel Workspace Key', validators=[DataRequired()])
    tableName = StringField('Table Name', validators=[DataRequired()])
    apiLogFileName = SelectField('ApiFilename', validate_choice=False)
    submit = SubmitField('Run API Job')

class syslogSettingsForm(FlaskForm):
    serverIP = StringField('Syslog Server Hostname or IP Address', validators=[DataRequired()])
    submit = SubmitField('Save Syslog Settings')

class apiSettingsForm(FlaskForm):
    workspaceId = StringField('Sentinel Workspace ID', validators=[DataRequired()])
    workspaceKey = StringField('Sentinel Workspace Key', validators=[DataRequired()])
    submit = SubmitField('Save API Settings')