##########################################################
#
# Program: Create web application framework 
#           using packages from py library
# Project: DB MGMT Final Project
# Author: Jacob Janzen
# Last Updated: 12/2/23
#
###########################################################

from flask import Flask, render_template, send_file, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from sqlalchemy import func
from sqlalchemy.orm import synonym
from werkzeug.security import check_password_hash, generate_password_hash
from getpass import getpass
from datetime import datetime
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv('.env.dev')
app.config['SECRET_KEY'] = os.environ.get('PERSONAL_FLASK_SECRET_KEY'), os.urandom(24) 

login_manager = LoginManager(app)
login_manager.login_view = 'login'


def protect_db():
    username = "jacobjanzen11"#input("\nEnter DB Username: ")
    password = "!4WeLoveJesus!"#getpass("\nEnter DB Password: ")
    host = "localhost"#input("\nEnter DB Host Name: ")
    db_path = "music"#input("\nEnter name of DB: ")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + username + ':' + password + '@' + host + '/' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
            

# ask user for login credentials for db connection
protect_db()
db = SQLAlchemy(app)

# User model for Flask-Login
class User(UserMixin, db.Model):
    __tablename__ = 'User'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(255), unique=True, nullable=False)
    username = synonym('uname')
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    dateJoin = db.Column(db.DateTime)
    
    def get_id(self):
        return str(self.ID)

# pushes application context, so tables are generated inside it
# generate all defined db tables: User
app.app_context().push()
db.create_all()

# Initialize Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# update this route to whatever link homepage should be
@app.route('/')
def home():
    return render_template('index.html')


# example of potential route to song for testing purposes
@app.route('/stream/<filename>')
def stream(filename):
    audio_file_path = f'path/to/audio/file/{filename}.mp3'
    return send_file(audio_file_path, as_attachment=True)


# added login functionality using Flask package
@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            name = request.form.get('name')  # Get the name from the form
            date_join = datetime.utcnow()  # Use current UTC time as the dateJoin value

            # Check if the username already exists
            existing_user = User.query.filter(func.lower(User.username) == func.lower(username)).first()
            if existing_user:
                flash('Username already exists. Please choose a different username.', 'danger')
                return redirect(url_for('signup'))

            # Hash the password before storing it
            hashed_password = generate_password_hash(password, method='scrypt', salt_length=8)

            # Create a new user object
            new_user = User(username=username, password=hashed_password, name=name, dateJoin=date_join)
            try:
                # Add the user to the database
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                print(f"Error during signup: {e}")
                # rollsback changes if error occurs
                db.session.rollback()
            

            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'An error occurred during signup: {str(e)}', 'danger')
            return redirect(url_for('signup'))
    else: 
        return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if request.method == 'POST':
        try:
            # Use case-insensitive comparison for username
            user = User.query.filter(func.lower(User.uname) == func.lower(username)).first()
            # Log the query for debugging
            app.logger.info(f"Query: {str(User.query.filter(func.lower(User.uname) == func.lower(username)))}")

            if user and check_password_hash(user.password, password):
                app.logger.info(f"User object: {user.__dict__}")
                login_user(user)
                return redirect(url_for('home'))
            else:
                app.logger.warning("Login credentials are invalid.")
                flash('Invalid username or password', 'danger')
                return redirect(url_for('login'))
        except Exception as e:
            app.logger.error(f"Error during login: {str(e)}")
            flash(f'An error occurred while logging in: {str(e)}', 'danger')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('home'))
    

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))


# if main, run app with debug
if __name__ == '__main__':
    app.run(debug=True)
    