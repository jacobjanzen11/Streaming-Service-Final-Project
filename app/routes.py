##########################################################
#
# Program: Create web application framework 
#           using Flask and sqlalchemy libraries.
#           This file only defines the app routes, the
#           database classes are defined in db_classes.py
# Project: DB MGMT Final Project
# Author: Jacob Janzen
# Last Updated: 12/15/23
#
###########################################################

from flask import render_template, send_file, request, redirect, url_for, flash, current_app, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import func, or_
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from models import db, User, Playlist, Owned, Song, PlaylistForm
from __init__ import app, login_manager


def add_playlist(user_id, playlist_name):
    try:
        # Check if the user exists
        user = db.session.query(User).get(user_id)

        if user:
            # Create a new playlist entry
            playlist = Playlist(name=playlist_name)
            db.session.add(playlist)
            db.session.commit()

            # Associate the playlist with the user
            owned_playlist = Owned(user_id=user_id, playlist_id=playlist.ID, name=playlist_name)
            db.session.add(owned_playlist)
            db.session.commit()

            app.logger.info(f"Playlist '{playlist_name}' added successfully for user {user_id}")
            return True, "Playlist added successfully"
        else:
            app.logger.warning(f"User {user_id} does not exist")
            return False, "User does not exist"

    except Exception as e:
        app.logger.error(f"Error adding playlist: {str(e)}")
        return False, "An error occurred while adding the playlist"


def add_song(song_name, artist_name, playlist_id, song_order):
    try:
        # Check if the playlist exists
        playlist_exists = db.session.query(Playlist.query.filter_by(ID=playlist_id).exists()).scalar()

        if playlist_exists:
            # Create a new song entry
            song = Song(name=song_name, artist=artist_name, song_order=song_order)
            db.session.add(song)
            db.session.commit()

            # Associate the song with the playlist
            playlist = Playlist.query.get(playlist_id)
            playlist.songs.append(song)
            db.session.commit()

            return True, "Song added to playlist successfully"
        else:
            return False, "Playlist does not exist"

    except Exception as e:
        current_app.logger.error(str(e))
        return False, "An error occurred while adding the song to the playlist"

# Initialize Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # return Session(db.engine).query(User).get(int(user_id))
    return db.session.query(User).get(user_id)


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
            date_join = datetime.utcnow()  # Use current local time as the dateJoin value

            # Check if the username already exists
            existing_user = User.query.filter(or_(User.username.ilike(username), User.uname.ilike(username))).first()
            
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


@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            # Use case-insensitive comparison for username
            user = User.query.filter(or_(User.username.ilike(username), User.uname.ilike(username))).first()

            # Log the query and query result for debugging
            app.logger.info(f"Query: {str(db.session.query(User).filter(func.lower(User.uname) == func.lower(username)).statement)}")
            app.logger.info(f"Query Result: {user}")

            if user and check_password_hash(user.password, password):
                app.logger.info(f"User object: {user.__dict__}")
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('home'))
            else:
                app.logger.warning("Login credentials are invalid.")
                flash('Invalid username or password', 'danger')
                return redirect(url_for('home'))
        except Exception as e:
            app.logger.error(f"Error during login: {str(e)}")
            flash(f'An error occurred while logging in: {str(e)}', 'danger')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
    

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out', 'info')
    else:
        flash('You are not logged in', 'warning')

    return redirect(url_for('home'))


# Route for adding a playlist
@app.route('/add_playlist', methods=['POST'])
def add_playlist_route():
    try:
        data = request.get_json()

        user_id = data.get('user_id')
        playlist_name = data.get('playlist_name')

        success, message = add_playlist(user_id, playlist_name)

        return jsonify({"success": success, "message": message})
    
    except Exception as e:
        app.logger.error(f"Error adding playlist: {str(e)}")
        return jsonify({"success": False, "message": "An error occurred while adding the playlist"}), 500


@app.route('/create_playlist', methods=['GET', 'POST'])
def create_playlist():
    form = PlaylistForm()

    if form.validate_on_submit():
        playlist_name = form.name.data
        user_id = current_user.get_id() 

        success, message = add_playlist(user_id, playlist_name)

        if success:
            flash('Playlist created successfully!', 'success')
            return redirect(url_for('playlistMake'))  # Redirect to the home page after form submission
        else:
            flash(f'Error creating playlist: {message}', 'danger')

    # Debug print statement
    print("\nRendering create_playlist.html with form:", form)
    return render_template('playlistMake.html', form=form)


@app.route('/add_song', methods=['POST'])
def route_add_song():
    data = request.get_json()

    song_name = data.get('song_name')
    artist_name = data.get('artist_name')
    playlist_id = data.get('playlist_id')
    order = data.get('order')

    success, message = add_song(song_name, artist_name, playlist_id, order)

    return jsonify({"success": success, "message": message})


@app.route('/user_playlists/<int:user_id>')
def user_playlists(user_id):
    # Get the user's playlists from the database
    user_playlists = Owned.query.filter_by(userID=user_id).all()
    
    return render_template('user_playlists.html', user_playlists=user_playlists)


@app.route('/playlistMake')
def playlistMake():
    # Check if the user is logged in
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        user_playlists = Owned.query.filter_by(userID=user_id).all()
        return render_template('playlistMake.html', user_playlists=user_playlists)
    else:
        # Handle the case when the user is not logged in
        pass


# if main, run app with debug
# set debug to False before prod for security reasons
if __name__ == '__main__':
    app.run(debug=True)
    