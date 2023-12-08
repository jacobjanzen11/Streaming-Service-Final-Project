
songNames = ["Thunder", "Rawr", "Yup", "FSU Fight Song", "National Anthem"]

//basic song object
function SongObject(songName, artist, indexNum) {
        this.songName = songName;
        this.artist = artist;
        this.indexNum = indexNum;
} 
//use a for loop to make song object array
//var song1 = new SongObject("Sams Song", "Jason", 1);


//when the + button is clicked add song to playlists by id = songLibrary#
function addSongToPlayList(button) {
    
    var element = $(button).attr("id"); //gets the divs index
    $(button).attr("onclick","removeSongFromPlaylist(this)");
    
    var songDiv = $("#songLibrary" + element).prop('outerHTML');//gets the whole song div
    
    $("#songLibrary" + element).remove();//deletes
    
    var newPlaylistSong = changeCharacter(songDiv, '+', '-'); //changes the btn from a + to -
    //todo add newSong to active playlists
    $(document).ready(function() {
        var accordionElement = $('.accordionContainer.active');
        accordionElement.find('.content').append(newPlaylistSong);  
        });

}

//when - is clicked in the playlist
function removeSongFromPlaylist(button) {
    $(button).attr("onclick","addSongToPlayList(this)");
    var element = $(button).attr("id"); //gets the divs index
    var songDiv = $("#songLibrary" + element).prop('outerHTML');//gets the whole song div
    $("#songLibrary" + element).remove();//deletes
    var newPlaylistSong = changeCharacter(songDiv, '-', '+'); //changes the btn from a + to -
    $(".songContainer").prepend(newPlaylistSong);

}

function changeCharacter(str, oldCharacter, newCharacter) {
    
    var strArray = str.split('');
    for (var i = 0; i < strArray.length; i++) {
        if (strArray[i] === oldCharacter) {
            strArray[i] = newCharacter;
           
            return strArray.join('');
        }
    }
    return str;
}

//loads in songs
for(var i = 0; i < 200; i++) {
    let SongName = "Sams Song";
    let Artist = "Sam";

    $(".songContainer").append("<div id='songLibrary" + i + "' class='songShow " + i + "'><p>" + i +" " + SongName + "by:" + Artist + "</p><div class='btnDiv'><button onclick='addSongToPlayList(this)' id='" + i + "' class='songBTN'>+</button></div></div>");

}

//loads playlists
for(var i = 0; i < 10;i++) {
    let content = "";
    let label = "Wtf"  + i;
    $('#playlistContainer').append("<div id='playlist" + i + "' class='accordionContainer'><div class='label'>" + label + "</div><div class='content'>Test</div></div><hr>");
}


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


MightNeed to add indexes to html tags

addSongs(song, playlist); //adds songs to a users desired playlist

removeSongs(song);// Removes songs from playlist

setUp() // sets up the songs that you can search through and pulls the users playlist info

*/