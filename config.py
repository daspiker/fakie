import os

class Config(object):
    UPLOAD_FOLDER = 'uploads/'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'