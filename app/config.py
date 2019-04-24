import os 

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or \
    'postgres://postgres:@localhost:5432/postgres'
SECRET_KEY = os.getenv('SECRET_KEY') or 'cannot tell you'
SQLALCHEMY_TRACK_MODIFICATIONS = False