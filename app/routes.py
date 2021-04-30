from flask import Flask,flash,request,redirect,send_file,render_template
from app import app
from werkzeug.utils import secure_filename
import os
import subprocess
import json
from app.forms import syslogForm, apiForm
from app.sentinel import AzureSentinelConnector

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
    syslog_form = syslogForm()
    api_form = apiForm()
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
    return render_template('job.html', files=files, syslog_form=syslog_form, api_form=api_form)

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
        sentinel = AzureSentinelConnector(workspaceId, workspaceKey, tableName, queue_size=10000, bulks_number=10)
        with open(apiLogFileName, "r") as read_file:
            payload = {}
            data = json.load(read_file)
            print(data)
            for entry in data:
                for key, value in entry.items():
                    payload.update({key:value})
                with sentinel:
                    sentinel.send(payload)
        
    return render_template('job.html', files=files, syslog_form=syslog_form, api_form=api_form)

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
            print("saved file successfully")
            files = os.listdir(app.config['UPLOAD_FOLDER'])  
    return render_template('upload.html', files=files)

@app.route('/settings')
def settings():
    return render_template('settings.html')