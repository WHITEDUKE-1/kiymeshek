from src.db import db

from datetime import datetime

class Article(db.Model):
    __tablename__ = "articles"

    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, content, category_id,author_id, updated_at) -> None:
        self.title = title
        self.content = content
        self.category_id = category_id
        self.author_id = author_id
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"Article<{self.category}>"
    
    def to_dict(self):
        return {
            "article_id": self.article_id,
            "title": self.title,
            "content": self.content,
            "category_id": self.category_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    

