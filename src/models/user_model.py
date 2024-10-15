from src.models import db

# Úlgi ushın model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=True)
    social_networks = db.Column(db.JSON)
    # role_id = db.Column(db.Integer, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def __init__(self, username: str, email: str, password: str, social_networks: dict, role_id: int):
        self.username = username
        self.email = email
        self.password = password
        self.social_networks = social_networks
        self.role_id = role_id

    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            "user_id": self.id,
            "username": self.username,
            "email": self.email,
            "social_networks": self.social_networks,
            "role_id": self.role_id,
            "created_at": self.created_at
        }