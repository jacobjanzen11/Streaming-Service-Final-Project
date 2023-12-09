##########################################################
#
# Program: Defines Instances for DB tables so they can 
#           be accessed as objects in flask app script
# Project: DB MGMT Final Project
# Author: Jacob Janzen
# Last Updated: 12/7/23
#
###########################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from sqlalchemy.orm import synonym
from dotenv import load_dotenv
from getpass import getpass
import os


app = Flask(__name__)

load_dotenv('.env.dev')
app.config['SECRET_KEY'] = os.environ.get('PERSONAL_FLASK_SECRET_KEY'), os.urandom(24) 

login_manager = LoginManager(app)
login_manager.login_view = 'login'


def protect_db():
    # username = input("\nEnter DB Username: ")
    # password = getpass("\nEnter DB Password: ")
    # host = input("\nEnter DB Host Name: ")
    # db_path = input("\nEnter name of DB: ")
    
    username = "jacobjanzen11"#input("\nEnter DB Username: ")
    password = "!4WeLoveJesus!"#getpass("\nEnter DB Password: ")
    host = "localhost"#input("\nEnter DB Host Name: ")
    db_path = "music"#input("\nEnter name of DB: ")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + username + ':' + password + '@' + host + '/' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
            

# ask user for login credentials for db connection
protect_db()
db = SQLAlchemy(app)

# pushes application context, so tables are generated inside it
# generate all defined db tables: User
app.app_context().push()
db.create_all()


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
    

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    songs = db.relationship('Song', backref='playlist', lazy=True)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255))
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    

class PlaylistForm(FlaskForm):
    name = StringField('Playlist Name', render_kw={'placeholder': 'Enter playlist name'})
    submit = SubmitField('Create Playlist')


class SongForm(FlaskForm):
    name = StringField('Song Name', render_kw={'placeholder': 'Enter song name'})
    artist = StringField('Artist', render_kw={'placeholder': 'Enter artist name'})
    submit = SubmitField('Add Song')
    
    
class Owned(db.Model):
    __tablename__ = 'Owned'
    userID = db.Column(db.Integer, db.ForeignKey('User.ID'), primary_key=True)
    playlistID = db.Column(db.Integer, db.ForeignKey('Playlist.id'), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Owned(userID={self.userID}, playlistID={self.playlistID}, name={self.name})>"
