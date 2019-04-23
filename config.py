import os 

def Config():
    DB_URI = os.getenv('DB_URI') or \
        'postgres://postgres:@localhost:5432/postgres'
    SECRET_KEY = os.getenv('SECRET_KEY') or 'cannot tell you'
    SQLALCHEMY_TRACK_MODIFICATIONS = False