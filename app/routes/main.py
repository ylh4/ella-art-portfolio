from flask import Blueprint, render_template
from app.models.artwork import Artwork

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    recent_artworks = Artwork.query.order_by(Artwork.created_date.desc()).limit(5).all()
    return render_template('home.html', recent_artworks=recent_artworks)
