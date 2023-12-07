##########################################################
#
# Program: Create web application framework 
#           using packages from py library
# Project: DB MGMT Final Project
# Author: Jacob Janzen
# Last Updated: 12/2/23
#
###########################################################

from flask import Flask, render_template, send_file, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import inspect
from werkzeug.security import check_password_hash
from getpass import getpass
import os


app = Flask(__name__)

# secret_key = input("\nEnter Your Secret Key: ")
# app.config['SECRET_KEY'] = secret_key 
login_manager = LoginManager(app)
login_manager.login_view = 'login'


def protect_db():
    username = "jacobjanzen11"#input("\nEnter DB Username: ")
    password = "!4WeLoveJesus!"#getpass("\nEnter DB Password: ")
    host = "localhost"#input("\nEnter DB Host Name: ")
    db_path = "music"#input("\nEnter name of DB: ")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + username + ':' + password + '@' + host + '/' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            

# ask user for login credentials for db connection
protect_db()
db = SQLAlchemy(app)

# User model for Flask-Login
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    dateJoin = db.Column(db.DateTime)


# Initialize Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# update this route to whatever link homepage should be
@app.route('/')
def home():
    print('hi there')
    return render_template('../UI/index.html')


# example of potential route to song for testing purposes
@app.route('/stream/<filename>')
def stream(filename):
    audio_file_path = f'path/to/audio/file/{filename}.mp3'
    return send_file(audio_file_path, as_attachment=True)


# added login functionality using Flask package, HTML can be updated,
# left actual categories and design with placeholders
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('home'))
    
    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# if main, run app with debug
if __name__ == '__main__':
    app.run(debug=True)
    