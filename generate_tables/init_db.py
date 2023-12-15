#######################################################
#
# Program: Initialize the database outlined
#           in createDB.sql
# Project: DB MGMT Final Project
# Author: Jacob Janzen
# Last Updated: 12/5/23
#
########################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from getpass import getpass
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)

def protect_db():
    username = input("\nEnter DB Username: ")
    password = getpass("\nEnter DB Password: ")
    host = input("\nEnter DB Host Name: ")
    db_path = input("\nEnter name of DB: ")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + username + ':' + password + '@' + host + '/' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            

# ask user for login credentials for db connection
# protect_db()
# db = SQLAlchemy(app)


# def initialize_database():
#     inspector = inspect(db.engine)

#     # Check if tables exist
#     if inspector.has_table("your_table_name"):
#         print("Tables already exist. No need to create them again.")
#         return

#     # Execute the SQL script to create tables
#     with open('application/createDB.sql', 'r') as script_file:
#         script = script_file.read()

#     # Explicitly declare the script as text
#     text_script = db.text(script)

#     try:
#         # Execute the SQL script
#         result = db.session.execute(text_script)

#         # Consume the result to avoid "Commands out of sync" error
#         result.fetchall()

#         # Commit the changes
#         db.session.commit()
#         print("Tables successfully created.")
#     except Exception as e:
#         # Rollback changes in case of an exception
#         db.session.rollback()
#         print(f"Error creating tables: {e}")
#     finally:
#         # Close the database session
#         db.session.close()
        
def get_sql_template():
    # Replace 'your_database_url' with the actual URL of your database
    engine = create_engine('mysql+mysqlconnector://jacobjanzen11:!4WeLoveJesus!@localhost/music')

    # Reflect the existing database schema
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Create an automap base
    Base = automap_base()

    # Reflect the tables
    Base.prepare(engine, reflect=True)

    # Output the generated models to a Python file
    with open('generated_models.py', 'w') as f:
        f.write("# Auto-generated models based on existing SQL schema\n\n")
        f.write("from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine\n")
        f.write("from sqlalchemy.orm import relationship, Session\n")
        f.write("from sqlalchemy.ext.declarative import declarative_base\n\n")
        f.write("Base = declarative_base()\n\n")

        for table_name in metadata.tables:
            f.write(f"\nclass {table_name.capitalize()}(Base):\n")
            f.write(f'    __tablename__ = "{table_name}"\n')

            for column in metadata.tables[table_name].columns:
                f.write(f'    {column.name} = Column({column.type}, {", ".join(repr(constraint) for constraint in column.constraints)})\n')

    # Output success message
    print("Generated models have been written to 'generated_models.py'")
    
    
def get_py_classes():
    engine = create_engine('mysql+mysqlconnector://jacobjanzen11:!4WeLoveJesus!@localhost/music')
    # Reflect the database tables
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    # Access the classes representing your tables
    Album = Base.classes.album
    Artist = Base.classes.Artist
    FollowAlbum = Base.classes.follow_album
    User = Base.classes.User
    FollowArtist = Base.classes.follow_artist
    Friend = Base.classes.Friend
    ListenNow = Base.classes.listen_now
    Owned = Base.classes.owned
    Playlist = Base.classes.Playlist
    PlaylistSong = Base.classes.playlist_song
    Song = Base.classes.Song



if __name__ == '__main__':
    # get_sql_template()
    get_py_classes()
