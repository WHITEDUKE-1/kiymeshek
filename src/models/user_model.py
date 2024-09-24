from flask_sqlalchemy import SQLAlchemy

from src.models import db

# Úlgi ushın model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def __repr__(self):
        return f'<User {self.username}>'
