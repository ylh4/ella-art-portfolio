from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models.artwork import Artwork
from app import db
import os
from werkzeug.utils import secure_filename
from config import Config

bp = Blueprint('admin', __name__)

@bp.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')

@bp.route('/admin/upload', methods=['GET', 'POST'])
@login_required
def upload_artwork():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        medium = request.form['medium']
        category = request.form['category']
        file = request.files['image']
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            
            artwork = Artwork(title=title, description=description, medium=medium, category=category, image_filename=filename)
            db.session.add(artwork)
            db.session.commit()
            
            return redirect(url_for('admin.admin_dashboard'))
    
    return render_template('admin/upload.html')
