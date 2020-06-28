from datetime import datetime

from app import db

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    location = db.Column(db.String(64), index=True, unique=False)
    waterings = db.relationship('Watering', backref='plant_name', lazy='dynamic')

    def __repr__(self):
        return '<Plant {}>'.format(self.name)

class Watering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))

    def __repr__(self):
        return '<Watering {}>'.format(self.timestamp)