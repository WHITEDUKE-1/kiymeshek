from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.db import db
from src.models import Category, User, Role
from src.utils import is_admin

category_bp = Blueprint("category", __name__)

@category_bp.post("/category")
@jwt_required()
def create_category():

    if not is_admin(get_jwt_identity()):
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

@category_bp.get("/category")
@jwt_required()
def get_all_categories():
    categories = Category.query.all()
    response_data = []
    for category in categories:
        response_data.append(category.to_dict())

    return jsonify(response_data)

@category_bp.get("/category/<id>")
@jwt_required()
def get_one_category(id: int):
    id = int(id)
    print(id)
    category = Category.query.filter_by(category_id=id).first_or_404()

    return jsonify(category.to_dict())

@category_bp.put("/category/<id>")
@jwt_required()
def update_category_by_id(id: int):
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    role = Role.query.filter_by(role_id=user.role_id).first()

    if role.role_name != "ADMIN":
        return jsonify({"msg": "You are not an admin"}), 403
    
    data = request.get_json()
    new_name = data.get('category', None)

    if new_name is None:
        return jsonify({'msg': 'category name is required'}), 400
    
    category = Category.query.filter_by(category_id=id).first_or_404()
    category.category = new_name
    
    db.session.add(category)
    db.session.commit()

    return jsonify({'msg': 'Category updated', 'data': category.to_dict()})

@category_bp.delete("/category/<id>")
@jwt_required()
def delete_by_id(id: int):
    if not is_admin(get_jwt_identity()):
        return jsonify({"msg": "You are not an admin"}), 403

    Category.query.filter_by(category_id=id).delete()
    db.session.commit()

    return jsonify({"msg": "Category is deleted"})