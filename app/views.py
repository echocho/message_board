from flask import Flask
# from sqlalchemy import 
from app import app

@app.route('/')
def index():
    # print(db)
    return 'hello world'

