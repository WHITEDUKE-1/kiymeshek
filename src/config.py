import os
from dotenv import load_dotenv

# .env fayldan ózgeriwshilerdi júklep alıw
load_dotenv()

class Config:
    # Flask konfiguraciyaları
    DEBUG = os.getenv('DEBUG', False)

    # PostgreSQL maǵlıwmatlar bazası ushın konfiguraciya
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Basqa konfiguraciyalar
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
