##########################################################
#
# Program: Defines the classes and forms used in main
#          flask application (app.py)
# Project: DB MGMT Final Project
# Author: Jacob Janzen
# Last Updated: 12/15/23
#
###########################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import synonym
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# used for migrating current schema into mysql tables
# migrate = Migrate(app, db)
# engine = create_engine('mysql+mysqlconnector://jacobjanzen11:!4WeLoveJesus!@localhost/music')


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(255), unique=True, nullable=False)
    username = synonym('uname')
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    dateJoin = Column(DateTime, default=datetime.utcnow())
    
    def get_id(self):
        return str(self.ID)

class Album(db.Model):
    __tablename__ = "album"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey('Artist.ID'))
    release_date = Column(DateTime)

class Artist(db.Model):
    __tablename__ = "Artist"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    followerCount = Column(Integer)
    dateJoin = Column(DateTime)

class Follow_album(db.Model):
    __tablename__ = "follow_album"
    album = Column(Integer, ForeignKey('Album.ID'), primary_key=True)
    user = Column(Integer, ForeignKey('User.ID'), primary_key=True)

class Follow_artist(db.Model):
    __tablename__ = "follow_artist"
    artist = Column(Integer, ForeignKey('Artist.ID'), primary_key=True)
    user = Column(Integer, ForeignKey('User.ID'), primary_key=True)   

class Friend(db.Model):
    __tablename__ = "Friend"
    u1 = Column(Integer, ForeignKey('User.ID'), primary_key=True)
    u2 = Column(Integer, ForeignKey('User.ID'), primary_key=True)   

class Listen_now(db.Model):
    __tablename__ = "listen_now"
    userID = Column(Integer, ForeignKey('User.ID'), primary_key=True)
    songID = Column(Integer, ForeignKey('Song.ID'), primary_key=True)

class Owned(db.Model):
    __tablename__ = "owned"
    user_id = Column(Integer, ForeignKey('User.ID'), primary_key=True)
    playlist_id = Column(Integer, ForeignKey('Playlist.ID'))
    name = Column(String(255), nullable=False) 

class Playlist(db.Model):
    __tablename__ = "Playlist"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

class Playlist_song(db.Model):
    __tablename__ = "playlist_song"
    playlist_id = Column(Integer, primary_key=True, autoincrement=True)
    song_id = Column(Integer, ForeignKey('Song.ID'))
    song_order = Column(Integer)

class Song(db.Model):
    __tablename__ = "Song"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey('Artist.ID'))
    album_id = Column(Integer, ForeignKey('Album.ID'))
    release = Column(DateTime)
    genre = Column(String(255))
    listens = Column(Integer)
    length = Column(Integer)
    filepath = Column(String(255))
    
    
class PlaylistForm(FlaskForm):
    name = StringField('Playlist Name', render_kw={'placeholder': 'Enter playlist name'})
    submit = SubmitField('Create Playlist')


class SongForm(FlaskForm):
    name = StringField('Song Name', render_kw={'placeholder': 'Enter song name'})
    artist = StringField('Artist', render_kw={'placeholder': 'Enter artist name'})
    submit = SubmitField('Add Song')
    
    
### TESTING ###
# Only for creating the tables
# # Create the tables in the datadb.Model
# db.Model.metadata.create_all(engine)

# print("Tables created successfully.")