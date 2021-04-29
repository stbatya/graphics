from . import db


class Insurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(120), nullable=False)
    bmi = db.Column(db.Float)
    children = db.Column(db.String(120))
    smoker = db.Column(db.String(120))
    region = db.Column(db.String(120))
    charges = db.Column(db.Float)
