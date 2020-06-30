from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    location = db.Column(db.String(64), index=True, unique=False)
    last_watered = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image_filename = db.Column(db.String)
    image_url = db.Column(db.String)
    waterings = db.relationship('Watering', backref='plant_name', lazy='dynamic')

    def __repr__(self):
        return '<Plant {}>'.format(self.name)

class Watering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))

    def __repr__(self):
        return '<Watering {}>'.format(self.timestamp)