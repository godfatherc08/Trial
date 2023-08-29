from . import db
from sqlalchemy.sql import func

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    def __init__(self, first_name, email, password):
        self.first_name = first_name
        self.email = email
        self.password = password
    def __repr__(self):
        return '<User %r>' % self.first_name



