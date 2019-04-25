from flask import (Flask, flash, redirect, render_template, 
                   request, url_for)

from app import app, db
from .forms import MessageForm
from .models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if request.method == 'GET':
        all_posts = Message.query.order_by(Message.created_at.desc()).all()
        return render_template('index.html', form=form, messages=all_posts)

    if form.validate_on_submit():
        author = request.values.get('name')
        msg = request.values.get('message')
        if author and msg:
            new_record = Message(author=author, content=msg)
            db.session.add(new_record)
            db.session.commit()
            flash('message posted!')
        return redirect(url_for('index'))

