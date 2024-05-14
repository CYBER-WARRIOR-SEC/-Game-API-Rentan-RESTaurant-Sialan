import os
import random
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


# 6 digits random secrets are secure enough,
# I don't believe someone could brute-force them
import random
import string

def generate_random_secret(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


import os
import secrets

class Settings:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_hex(32))
    CHEF_USERNAME = os.getenv("CHEF_USERNAME", "chef")

    # Make sure to explicitly convert the environment variable to a boolean
    JWT_VERIFY_SIGNATURE = os.getenv("JWT_VERIFY_SIGNATURE", "").lower() in ["true", "1"]

    POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))  # Convert port to integer
    POSTGRES_DB = os.getenv("POSTGRES_DB", "restaurant")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
