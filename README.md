### MUSIC STREAMING APPLICATION DOCUMENTATION ###

# User Guide
    ## Starting the APP ##
        - Run the run_app.py script to initialize the Flask application (As of now the app must be run by running python3 app/routes.py)
        - Running the script will automatically print the the link to the local UI in the terminal output
        - Cmd. + Click on the link and you will be redirected to the Ui homepage

    ## Logging in ##
        - Before creating a playlist or using any of the website's functionality, you must be an authenticated User
        - To login, click on the login button in the top left corner of the homepage 
        - If it is your first time using the application, click the sign up buttona and create a new User profile
        - Once you hit submit, you will be directed back to the homepage, where you can login using your username and password credentials
        - If you have logged in and have been authenticated successfully, the login button will change to a red "Logout" button,
            you can press this at any time to logout of the application.

    ## Creating a Playlist ##
        - Once logged in, you can click either the "Create Playlist" button or "Find Song"
        - If you click on the create playlist, you will be redirected to a page that will list all of the current user's available playlists, as well as a text box
            that will allow the you to enter the desired title of your new playlist
        - After you click on the create playlist button underneath the text box, you will be directed to the add song page, in which you can add songs to your new playlist

    ## Add Songs to a Playlist ## 