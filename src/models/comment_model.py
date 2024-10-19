from src.db import db

from datetime import datetime

class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.article_id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    def __init__(self, comment, user_id, article_id) -> None:
        self.comment = comment
        self.user_id = user_id
        self.article_id = article_id
        self.updated_at = datetime.now()
    

    def __repr__(self) -> str:
        return f"Comment<{self.comment}>"
    
    def to_dict(self):
        return {
            "article_id": self.comment_id,
            "comment": self.comment,
            "user_id": self.user_id,
            "article_id": self.article_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
