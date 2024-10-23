from app import db
from datetime import datetime

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    image_filename = db.Column(db.String(255), nullable=False)
    medium = db.Column(db.String(50))
    category = db.Column(db.String(50))

    def __repr__(self):
        return f'<Artwork {self.title}>'
