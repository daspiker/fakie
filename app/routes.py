from flask import render_template
from app import app
import subprocess

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/script1')
def script1():
    subprocess.run(["/home/dennispike/fakie/scripts/test.sh"], shell=True)
    print(subprocess.check_output(["echo", "Fakie Rules!!!"]))
    return render_template('index.html', title='Home')