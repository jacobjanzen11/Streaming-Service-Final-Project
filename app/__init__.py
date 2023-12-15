from flask import Flask
from flask_login import LoginManager
from getpass import getpass
from dotenv import load_dotenv
import os
from models import db


app = Flask(__name__)

load_dotenv('.env.dev')
app.config['SECRET_KEY'] = os.environ.get('PERSONAL_FLASK_SECRET_KEY') or os.urandom(24)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

def protect_db(app):
    username = "jacobjanzen11"  # input("\nEnter DB Username: ")
    password = "!4WeLoveJesus!"  # getpass("\nEnter DB Password: ")
    host = "localhost"  # input("\nEnter DB Host Name: ")
    db_path = "music"  # input("\nEnter name of DB: ")

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{host}/{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
        
# ask user for login credentials for db connection
protect_db(app)
db.init_app(app)
    