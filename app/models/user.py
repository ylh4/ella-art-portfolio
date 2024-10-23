# app/models/user.py
from app.extensions import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # Add other fields and methods as necessary

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
