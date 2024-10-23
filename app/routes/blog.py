from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models.blog_post import BlogPost
from app import db

bp = Blueprint('blog', __name__)

@bp.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.order_by(BlogPost.created_date.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)

@bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = BlogPost(title=title, content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.blog'))
    return render_template('blog_new.html')
