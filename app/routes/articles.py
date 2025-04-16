from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_file
from flask_login import login_required, current_user
from app import db
from app.models import Article, EditHistory
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import pdfkit

bp = Blueprint('articles', __name__)

@bp.route('/')
def index():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('article_list.html', articles=articles)

@bp.route('/article/<int:id>')
def view_article(id):
    article = Article.query.get_or_404(id)
    return render_template('article_detail.html', article=article)

@bp.route('/article/new', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image_file = request.files['image']
        filename = None
        if image_file:
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        article = Article(title=title, content=content, image=filename, user_id=current_user.id)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('articles.index'))
    return render_template('article_edit.html', mode='new')

@bp.route('/article/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        image_file = request.files['image']
        if image_file:
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            article.image = filename

        edit = EditHistory(article_id=id, user_id=current_user.id)
        db.session.add(edit)
        db.session.commit()
        return redirect(url_for('articles.view_article', id=id))
    return render_template('article_edit.html', mode='edit', article=article)

@bp.route('/article/<int:id>/delete', methods=['POST'])
@login_required
def delete_article(id):
    article = Article.query.get_or_404(id)
    if current_user.id == article.user_id or current_user.is_admin:
        db.session.delete(article)
        db.session.commit()
        flash('مقاله حذف شد.')
    else:
        flash('شما مجوز حذف ندارید.')
    return redirect(url_for('articles.index'))

@bp.route('/article/<int:id>/pdf')
def article_pdf(id):
    article = Article.query.get_or_404(id)
    html = render_template('pdf_template.html', article=article)
    pdf_path = f'/tmp/article_{id}.pdf'
    pdfkit.from_string(html, pdf_path)
    return send_file(pdf_path, as_attachment=True)
