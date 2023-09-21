from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gitau'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Ken'},
            'body': 'The new avengers movie was lit!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)