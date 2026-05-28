"""
Settings — carrega variáveis de ambiente.
"""

import os
from dotenv import load_dotenv

load_dotenv("config/development.env")

# App
APP_ENV: str = os.getenv("APP_ENV", "development")
DEBUG: bool = APP_ENV == "development"
SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")

# MongoDB
MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
MONGODB_DB: str = os.getenv("MONGODB_DB", f"demo_db_{APP_ENV}")

# Server
HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "8000"))
