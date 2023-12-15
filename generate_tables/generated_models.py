# # Auto-generated models based on existing SQL schema

# from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
# from sqlalchemy.orm import relationship, Session
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


# class Album(Base):
#     __tablename__ = "album"
#     ID = Column(INTEGER, )
#     name = Column(VARCHAR(255), )
#     artist_id = Column(INTEGER, )
#     release_date = Column(DATETIME, )

# class Artist(Base):
#     __tablename__ = "Artist"
#     ID = Column(INTEGER, )
#     name = Column(VARCHAR(255), )
#     followerCount = Column(INTEGER, )
#     dateJoin = Column(DATETIME, )

# class Follow_album(Base):
#     __tablename__ = "follow_album"
#     album = Column(INTEGER, )
#     user = Column(INTEGER, )

# class User(Base):
#     __tablename__ = "User"
#     ID = Column(INTEGER, )
#     uname = Column(VARCHAR(255), )
#     password = Column(VARCHAR(255), )
#     name = Column(VARCHAR(255), )
#     dateJoin = Column(DATETIME, )

# class Follow_artist(Base):
#     __tablename__ = "follow_artist"
#     artist = Column(INTEGER, )
#     user = Column(INTEGER, )

# class Friend(Base):
#     __tablename__ = "Friend"
#     u1 = Column(INTEGER, )
#     u2 = Column(INTEGER, )

# class Listen_now(Base):
#     __tablename__ = "listen_now"
#     userID = Column(INTEGER, )
#     songID = Column(INTEGER, )

# class Owned(Base):
#     __tablename__ = "owned"
#     user_id = Column(INTEGER, )
#     playlist_id = Column(INTEGER, )
#     name = Column(VARCHAR(255), )

# class Playlist(Base):
#     __tablename__ = "Playlist"
#     ID = Column(INTEGER, )
#     name = Column(VARCHAR(255), )

# class Playlist_song(Base):
#     __tablename__ = "playlist_song"
#     playlist_id = Column(INTEGER, )
#     song_id = Column(INTEGER, )
#     song_order = Column(INTEGER, )

# class Song(Base):
#     __tablename__ = "Song"
#     ID = Column(INTEGER, )
#     name = Column(VARCHAR(255), )
#     artist_id = Column(INTEGER, )
#     album_id = Column(INTEGER, )
#     release = Column(DATETIME, )
#     genre = Column(VARCHAR(255), )
#     listens = Column(INTEGER, )
#     length = Column(INTEGER, )
#     filepath = Column(VARCHAR(255), )
