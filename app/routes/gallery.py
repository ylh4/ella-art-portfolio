from flask import Blueprint, render_template, request
from app.models.artwork import Artwork

bp = Blueprint('gallery', __name__)

@bp.route('/gallery')
def gallery():
    page = request.args.get('page', 1, type=int)
    artworks = Artwork.query.order_by(Artwork.created_date.desc()).paginate(page=page, per_page=12)
    return render_template('gallery.html', artworks=artworks)

@bp.route('/gallery/category/<category>')
def gallery_category(category):
    page = request.args.get('page', 1, type=int)
    artworks = Artwork.query.filter_by(category=category).order_by(Artwork.created_date.desc()).paginate(page=page, per_page=12)
    return render_template('gallery.html', artworks=artworks, category=category)
