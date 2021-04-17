from flask import Flask,flash,request,redirect,send_file,render_template
from app import app
from werkzeug.utils import secure_filename
import os
import subprocess

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/script1')
def script1():
    subprocess.run(["/home/dennispike/fakie/scripts/test.sh"], shell=True)
    print(subprocess.check_output(["echo", "Fakie Rules!!!"]))
    return render_template('index.html', title='Home')

@app.route('/input', methods=['GET', 'POST'])
def input():
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
    return render_template('input.html')

@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')