from flask import Flask

from src.routes import init_routes  # hámme routelardı dizimnen ótkeriw
from src.models import init_db      # maǵlıwmatlar bazasın qáliplestiriw

def init_app(app: Flask):
    app.config.from_object('src.config.Config')     # konfiguraciyalardı júklew
    init_routes(app)
    init_db(app)
