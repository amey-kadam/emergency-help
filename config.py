import os
import sqlite3

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DATABASE = os.path.join(os.getcwd(), 'instance', 'app.sqlite')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}
