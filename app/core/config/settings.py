import os

from dotenv import load_dotenv

load_dotenv(override=True)

DEBUG = os.environ.get('DEBUG')

CLIENT_APP_URL = os.environ.get('CLIENT_APP_URL')

LOGS_DIR = os.environ.get('LOGS_DIR')

# Database
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_TYPE = os.environ.get("DB_TYPE")