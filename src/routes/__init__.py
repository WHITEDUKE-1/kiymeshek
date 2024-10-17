from flask import Flask, Blueprint

from src.routes.auth import auth_bp
from src.routes.category import category_bp
from src.routes.article import article_bp

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return "Hello, Flask Template!"

def init_routes(app: Flask):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(article_bp)