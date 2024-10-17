from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from src.db import db
from src.models import Article
from src.utils import is_admin

from datetime import datetime

article_bp = Blueprint("article", __name__)

@article_bp.post('/article')
@jwt_required()
def create_aricle():
    user_id = get_jwt_identity()
    if not is_admin(user_id):
        return jsonify({"msg": "You are not admin"}), 403
    
    data = request.get_json()
    title = data.get('title', None)
    content = data.get('content', None)
    category_id = data.get('category_id', None)

    if title is None or content is None or category_id is None:
        return jsonify({"msg": "All atributes are required"}), 400
    
    new_article = Article(title=title, content=content, author_id=user_id, category_id=category_id, updated_at=datetime.now())
    db.session.add(new_article)
    db.session.commit()

    return new_article.to_dict()


@article_bp.get('/articles')
def get_all_articles():
    articles = Article.query.all()
    response_data = []
    for article in articles:
        response_data.append(article.to_dict())

    return jsonify({"articles": response_data})

@article_bp.get('/article/<id>')
def get_article_by_id(id: int):
    article = Article.query.filter_by(article_id=id).first_or_404()
    return jsonify(article.to_dict())