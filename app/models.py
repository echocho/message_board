# from sqlalchemy import Base, Column, String
from app import db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(20), nullable=False)
