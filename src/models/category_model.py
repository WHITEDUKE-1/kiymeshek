from src.db import db

class Category(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, nullable=True, unique=True)

    def __init__(self, category_name: str) -> None:
        self.category = category_name

    def __repr__(self) -> str:
        return f"Category<{self.category}>"
    
    def to_dict(self):
        return {
            "category_id": self.category_id,
            "category": self.category
        }