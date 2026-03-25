from . import db

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    location = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
