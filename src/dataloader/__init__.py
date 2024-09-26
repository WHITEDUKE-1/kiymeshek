from src.models.role_model import Role

def load_roles(db):
    default_roles = ['ADMIN', 'VALUNTEER', 'USER']

    for default_role in default_roles:
        role = Role.query.filter_by(role_name=default_role).first()

        if role is None:
            new_role = Role(default_role)
            db.session.add(new_role)

    db.session.commit()

def load_data(db):
    load_roles(db)