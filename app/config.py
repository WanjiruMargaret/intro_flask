import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print("ENV DB URL")
print(os.getenv("DATABASE_URL"))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # <-- corrected
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")  # safer: load from env with fallback
