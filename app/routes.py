from flask import Flask,flash,request,redirect,send_file,render_template
from app import app
from werkzeug.utils import secure_filename
import os
import subprocess
from app.forms import jobForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/script1')
def script1():
    subprocess.run(["/home/dennispike/fakie/scripts/test.sh"], shell=True)
    print(subprocess.check_output(["echo", "Fakie Rules!!!"]))
    return render_template('index.html', title='Home')

@app.route('/job', methods=['GET', 'POST'])
def job():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    form = jobForm()
    if form.validate_on_submit():
        serverIP = str(form.serverIP.data)
        logFileName = app.config['UPLOAD_FOLDER'] + str(form.logFileName.data)
        subprocess.run(["logger -p auth.info -n " + serverIP + " -t CEF -f " + logFileName], shell=True)
        return render_template('job.html', serverIP=serverIP, logFileName=logFileName, files=files, form=form)
    elif request.method == 'GET':
        serverIP = request.args.get('serverIP', type=str)
        form.serverIP.data = serverIP
        logFileName = request.args.get('logFileName', type=str)
        form.logFileName.data = logFileName
    return render_template('job.html', files=files, form=form)

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