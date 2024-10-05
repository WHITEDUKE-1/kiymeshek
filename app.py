from flask import Flask
from flask_jwt_extended import JWTManager

from src.loader import init_app


app = Flask(__name__)
jwt = JWTManager(app)
init_app(app)


if __name__ == "__main__":
    app.run(port=8080)
