from src.models import User, Role

def is_admin(user_id):
    user = User.query.filter_by(id=user_id).first()
    role = Role.query.filter_by(role_id=user.role_id).first()

    return role.role_name == "ADMIN"