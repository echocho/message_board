from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from .config import Config

app = Flask(__name__)
print('0000', app.config)
app.config.from_pyfile('config.py')
print('0000', app.config)

# print('------')
# print(app.config)
print(type(app.config))
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# session_factory = sessionmaker(bind=engine)
# flask_scoped_session(session_factory, app)
db = SQLAlchemy(app)
print(db)

from app import views
