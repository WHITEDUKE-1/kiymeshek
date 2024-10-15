from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.db import db
from src.models import Category, User, Role


category_bp = Blueprint("category", __name__)

@category_bp.post("/category")
@jwt_required()
def create_category():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    role = Role.query.filter_by(role_id=user.role_id).first()

    if role.role_name != "ADMIN":
        return jsonify({"msg": "You are not an admin"}), 403
    
    data = request.get_json()

    category_name = data.get('category', None)

    if category_name is None:
        return jsonify({"msg": "Category name is required"}), 400
    
    category = Category.query.filter_by(category=category_name).first()
    if category is not None:
        return jsonify({"msg": "Category is already taken"}), 400
    
    new_category = Category(category_name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({
        "msg": "Was created a new category",
        "data": new_category.to_dict()
    }), 201