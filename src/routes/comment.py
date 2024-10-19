from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from src.db import db
from src.models import Comment
from src.utils import is_admin

from datetime import datetime

comment_bp = Blueprint("comment", __name__)

@comment_bp.post('/comment')
@jwt_required()
def create_comment():
    user_id = get_jwt_identity()

    data = request.get_json()
    comment = data.get('comment', None)
    article_id = data.get('article_id', None)

    if not comment or not article_id:
        return jsonify({'msg': 'comment and article_id are required'}), 400
    
    new_comment = Comment(comment, user_id, article_id)


    return jsonify({'msg': "New comment created", 'data': new_comment.to_dict()}), 201

@comment_bp.get('/comments/<int:article_id>')
def get_all_comments_by_article_id(article_id: int):
    comments = Comment.query.filter_by(article_id=article_id).all()
    response_data = []
    for comment in comments:
        response_data.append(comment.to_dict())

    if response_data:
        return jsonify({'data': response_data}), 200
    return jsonify({'msg': "not found"}), 404


@comment_bp.put('/comment/<int:comment_id>')
@jwt_required()
def updata_comment_by_id(comment_id: int):
    current_user_id = get_jwt_identity()
    comment = Comment.query.filter_by(comment_id=comment_id).first()

    if current_user_id != comment.user_id:
        return jsonify({'msg': 'Permission denied'}), 403
    
    data = request.get_json()
    new_comment = data.get('comment', None)

    if new_comment is None:
        return jsonify({'msg': 'comment is required'}), 400
    
    comment.comment = new_comment
    comment.updated_at = datetime.now()
    db.session.add(comment)
    db.session.commit()
    comment = Comment.query.filter_by(comment_id = comment_id).first()
    return jsonify({'msg': 'updated', 'data': comment.to_dict()}), 200