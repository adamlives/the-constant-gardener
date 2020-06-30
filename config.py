import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-dev-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOP_LEVEL_DIR = os.path.abspath(os.curdir)

    UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/app/static/img/'
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'

    UPLOADED_IMAGES_DEST = TOP_LEVEL_DIR + '/app/static/img/'
    UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/'