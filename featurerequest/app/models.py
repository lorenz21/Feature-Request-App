from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    requests = db.relationship('Request', backref='requestor', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.Text(), index=True)
    target_date = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    product_area = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Request Title {}>'.format(self.title)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))