from src.db import db
from src.dataloader import load_data

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        load_data(db)

# Bárshe modeller
from .user_model import User
from .role_model import Role