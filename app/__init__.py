# app/__init__.py
from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import and register blueprints
    from app.routes import main, gallery, artwork, blog, admin, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(gallery.bp)
    app.register_blueprint(artwork.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(auth.bp)

    # Import models
    from app.models import user, blog_post

    return app
