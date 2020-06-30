from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES, configure_uploads

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)
login = LoginManager(app)
login.login_view = 'login'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

from app import routes, models