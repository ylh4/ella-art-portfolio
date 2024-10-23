from flask import Blueprint, render_template, abort
from app.models.artwork import Artwork

bp = Blueprint('artwork', __name__)

@bp.route('/artwork/<int:artwork_id>')
def artwork_detail(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    return render_template('artwork_detail.html', artwork=artwork)
