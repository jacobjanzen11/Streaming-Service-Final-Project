

const accordion = document.getElementsByClassName('accordionContainer');

for (i=0; i<accordion.length; i++) {
  accordion[i].addEventListener('click', function () {
    this.classList.toggle('active')
  })
}

/*
add playlist
$('#playlistContainer').append("<div class="accordionContainer">
        <div class="label">" + PlaylistName + "</div>
        <div class="content">" + songList + "</div>
      <hr>");


add songs to song library

$(".songContainer").append("<div class="songShow">" + SongName + "by:" + Artist + "<div class="btnDiv"><button class="songBTN">+</button><button class="songBTN">-</button></div></div>");

to add songs to playlist



song object {
    title;
    artist;
    releaseDate;
    OtherInfo
}

Playlist Object {
    Title
    Songs array
}


addSongs(song, playlist); //adds songs to a users desired playlist

removeSongs(song);// Removes songs from playlist

setUp() // sets up the songs that you can search through and pulls the users playlist info

*/