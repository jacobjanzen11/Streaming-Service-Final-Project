Get the user’s information. 
This will allow our application to display the users name and their playlists and albums they follow. This should happen on login. It will get the user’s ID, then it will find all playlists they own and what albums they follow

        SELECT ID
        FROM User
        WHERE uname = username;

        SELECT A.ID
        FROM `Follow Album` A
        WHERE A.user = userID;

        SELECT P.ID
        FROM Owned P
        WHERE P.user = userID;

Get the user’s playlists. 
The user table will have a playlist because the playlists will be stored in another table. The user can have multiple playlists, but a playlist can only have one user.  
This query will allow the application to display the songs in the user's playlist. 
	
Get the songs in the user's playlists. 
The song information will be stored in a table separate from playlists. The playlist data will store a list of song IDs. Songs can have multiple playlists and playlists can have multiple songs.  
This will allow us to list the songs in the user's playlist.
 
Get the songs information. 
Getting the song names, genre, and other information will allow the application to display the songs and all their information. 
Get albums information

Add playlist to user
