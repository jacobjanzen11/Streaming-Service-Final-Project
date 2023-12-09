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
from getpass import getpass

app = Flask(__name__)

def protect_db():
    username = input("\nEnter DB Username: ")
    password = getpass("\nEnter DB Password: ")
    host = input("\nEnter DB Host Name: ")
    db_path = input("\nEnter name of DB: ")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + username + ':' + password + '@' + host + '/' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Execute the SQL script to create tables
def initialize_database():
    with app.app_context():
        with open('createDB.sql', 'r') as script_file:
            script = script_file.read()

        # Explicitly declare the script as text
        text_script = db.text(script)

        try:
            # Use a context manager for result execution
            with db.session.begin():
                result = db.session.execute(text_script)
                # No need to explicitly commit; it will be done automatically when exiting the 'with' block
            print("Tables successfully created.")
        except Exception as e:
            # Rollback changes in case of an exception
            db.session.rollback()
            print(f"Error creating tables: {e}")
        finally:
            # Close the database session
            db.session.close()

if __name__ == '__main__':
    protect_db()
    db = SQLAlchemy(app)
    initialize_database()
