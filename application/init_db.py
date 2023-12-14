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


app = Flask(__name__)

def protect_db():
    username = input("\nEnter DB Username: ")
    password = getpass("\nEnter DB Password: ")
    host = input("\nEnter DB Host Name: ")
    db_path = input("\nEnter name of DB: ")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + username + ':' + password + '@' + host + '/' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            

# ask user for login credentials for db connection
protect_db()
db = SQLAlchemy(app)

db = SQLAlchemy(app)


def initialize_database():
    inspector = inspect(db.engine)

    # Check if tables exist
    if inspector.has_table("your_table_name"):
        print("Tables already exist. No need to create them again.")
        return

    # Execute the SQL script to create tables
    with open('application/createDB.sql', 'r') as script_file:
        script = script_file.read()

    # Explicitly declare the script as text
    text_script = db.text(script)

    try:
        # Execute the SQL script
        result = db.session.execute(text_script)

        # Consume the result to avoid "Commands out of sync" error
        result.fetchall()

        # Commit the changes
        db.session.commit()
        print("Tables successfully created.")
    except Exception as e:
        # Rollback changes in case of an exception
        db.session.rollback()
        print(f"Error creating tables: {e}")
    finally:
        # Close the database session
        db.session.close()


if __name__ == '__main__':
    initialize_database()
