from src.db import db

class Role(db.Model):
    __tablename__ = "roles"

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, nullable=False)

    def __init__(self, role_name: str): 
        self.role_name = role_name.upper()

    def __repr__(self) -> str:
        return f"Role <{self.role_name}>"
    
    def to_dict(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name
        }