import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Superelnatan'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///einatan_art.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'app/static/uploads')
