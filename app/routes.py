from flask import Flask,flash,request,redirect,send_file,render_template, url_for
from app import app
from werkzeug.utils import secure_filename
import os
import subprocess
import json
from app.forms import syslogForm, apiForm, syslogSettingsForm, apiSettingsForm
from app.sentinel import AzureSentinelConnector
from app import db
from app.models import SyslogSettings, ApiSettings

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/script1')
def script1():
    subprocess.run(["/home/dennispike/fakie/scripts/test.sh"], shell=True)
    print(subprocess.check_output(["echo", "Fakie Rules!!!"]))
    return render_template('index.html', title='Home')

@app.route('/job', methods=['GET'])
def job():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files_list=[(file) for file in files]

    syslog_form = syslogForm()
    api_form = apiForm()

    syslog_form.syslogLogFileName.choices = files_list
    api_form.apiLogFileName.choices = files_list

    syslogSettings = SyslogSettings.query.first()
    if syslogSettings:
        syslog_form.serverIP.data = syslogSettings.serverIP
    apiSettings = ApiSettings.query.first()
    if apiSettings:
        api_form.workspaceId.data = apiSettings.workspaceId
        api_form.workspaceKey.data = apiSettings.workspaceKey
    
    return render_template('job.html', files=files, syslog_form=syslog_form, api_form=api_form)

@app.route('/syslog', methods=['POST'])
def syslog():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    syslog_form = syslogForm()
    api_form = apiForm()
    if syslog_form.validate_on_submit():
        serverIP = str(syslog_form.serverIP.data)
        syslogLogFileName = app.config['UPLOAD_FOLDER'] + str(syslog_form.syslogLogFileName.data)
        subprocess.run(["logger -p auth.info -n " + serverIP + " -t CEF -f " + syslogLogFileName], shell=True)
        print("syslog data collected: " + serverIP + " " + syslogLogFileName)
        flash("Logs successfully sent to syslog server")
    return redirect(url_for('job'))

@app.route('/api', methods=['POST'])
def api():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    syslog_form = syslogForm()
    api_form = apiForm()
    if api_form.validate_on_submit():
        workspaceId = str(api_form.workspaceId.data)
        workspaceKey = str(api_form.workspaceKey.data)
        tableName = str(api_form.tableName.data)
        apiLogFileName = app.config['UPLOAD_FOLDER'] + str(api_form.apiLogFileName.data)
        print(workspaceId + " " + workspaceKey + " " + tableName + " " + apiLogFileName)
        sentinel = AzureSentinelConnector(workspaceId, workspaceKey, tableName, queue_size=10000, bulks_number=10)
        with open(apiLogFileName, "r") as read_file:
            data = json.load(read_file)
            for entry in data:
                with sentinel:
                    sentinel.send(entry)
            flash("Logs successfully sent to API")
    return redirect(url_for('job'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("File uploaded successfully")
            files = os.listdir(app.config['UPLOAD_FOLDER'])  
    return render_template('upload.html', files=files)

@app.route('/deletefile/<id>', methods=['GET'])
def deletefile(id):
    file = id
    os.remove(app.config['UPLOAD_FOLDER'] + file)
    flash('File successfully deleted')
    return redirect(url_for('upload'))
    return render_template(title="Delete File")

@app.route('/viewfile/<id>', methods=['GET'])
def viewfile(id):
    filename = id
    file = open(app.config['UPLOAD_FOLDER'] + filename, "r")
    fileoutput = file.read()
    return render_template('viewfile.html', filename=filename, fileoutput=fileoutput)

@app.route('/settings', methods=['GET'])
def settings():
    syslogSettings_form = syslogSettingsForm()
    apiSettings_form = apiSettingsForm()
    syslogSettingsAll = SyslogSettings.query.all()
    apiSettingsAll = ApiSettings.query.all()
    return render_template('settings.html', syslogSettings_form=syslogSettings_form, apiSettings_form=apiSettings_form, syslogSettingsAll=syslogSettingsAll, apiSettingsAll=apiSettingsAll)

@app.route('/syslogSettings', methods=['POST'])
def syslogSettings():
    syslogSettings_form = syslogSettingsForm()
    apiSettings_form = apiSettingsForm()
    if syslogSettings_form.validate_on_submit():
        syslogsettings = SyslogSettings(serverIP=syslogSettings_form.serverIP.data, comment=syslogSettings_form.comment.data)
        db.session.add(syslogsettings)
        db.session.commit()
        flash('Syslog Settings Successfully Saved')
    syslogSettingsAll = SyslogSettings.query.all()
    apiSettingsAll = ApiSettings.query.all()
    return render_template('settings.html',syslogSettings_form=syslogSettings_form, apiSettings_form=apiSettings_form, syslogSettingsAll=syslogSettingsAll, apiSettingsAll=apiSettingsAll)

@app.route('/deletesyslogsetting/<id>', methods=['GET'])
def deletesyslogsetting(id):
    syslogsetting = SyslogSettings.query.get_or_404(id)
    db.session.delete(syslogsetting)
    db.session.commit()
    flash('You have successfully deleted the syslog setting.')
    return redirect(url_for('settings'))

@app.route('/apiSettings', methods=['POST'])
def apiSettings():
    syslogSettings_form = syslogSettingsForm()
    apiSettings_form = apiSettingsForm()
    if apiSettings_form.validate_on_submit():
        apisettings = ApiSettings(workspaceId=apiSettings_form.workspaceId.data, workspaceKey=apiSettings_form.workspaceKey.data, comment=apiSettings_form.comment.data)
        db.session.add(apisettings)
        db.session.commit()
        flash('API Settings Successfully Saved')
    syslogSettingsAll = SyslogSettings.query.all()
    apiSettingsAll = ApiSettings.query.all()
    return render_template('settings.html', syslogSettings_form=syslogSettings_form, apiSettings_form=apiSettings_form, syslogSettingsAll=syslogSettingsAll, apiSettingsAll=apiSettingsAll)

@app.route('/deleteapisetting/<id>', methods=['GET'])
def deleteapisetting(id):
    apisetting = ApiSettings.query.get_or_404(id)
    db.session.delete(apisetting)
    db.session.commit()
    flash('You have successfully deleted the api setting.')
    return redirect(url_for('settings'))