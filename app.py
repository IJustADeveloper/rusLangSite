from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, LoginManager, login_required, current_user
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_class import Base, Users
import db_comms
from werkzeug.security import generate_password_hash, check_password_hash
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(24)
login_manager = LoginManager(app)

engine = create_engine('sqlite:///homeworkDB.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

login_manager = LoginManager(app)


@login_manager.user_loader
def user_loader(user_id):
    return session.query(Users).get(int(user_id))


@app.route('/')
def main_page():
    return redirect(url_for('homework_page', num="1"))


@app.route('/homework/page/<num>')
def homework_page(num):
    results, show_button = db_comms.get_data(int(num))
    return render_template('main.html', res=results, number=int(num), sb=show_button)


@app.route('/addHW', methods=["GET", "POST"])
def add_homework():
    if request.method == "POST":
        title = request.form['t']
        mainText = request.form['mt']
        db_comms.add_data(title, mainText)
    if not current_user.is_anonymous:
        return render_template('add_new.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            user = session.query(Users).filter_by(email=email).one()
        except:
            return render_template('login.html', message='Неверная почта')
        if not check_password_hash(generate_password_hash(user.password), password):
            return render_template('login.html', message='Неверный пароль')
        else:
            login_user(user, remember=True)
            return redirect(url_for('add_homework'))

    return render_template('login.html', message='')


if __name__ == '__main__':
    app.run()
