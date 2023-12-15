$(document).ready(function () {

  // Define songNames array
  var songNames = ["Thunder", "Rawr", "Yup", "FSU Fight Song", "National Anthem"];

  // Define playlist array
  var playlists = [];

  // Load songs and playlists
  loadSongs();
  loadPlaylists();

  // Function to load songs into the songContainer
  function loadSongs() {
    for (var i = 0; i < songNames.length; i++) {
      var songName = songNames[i];
      var artist = "Sample Artist";

      var songDiv = "<div id='songLibrary" + i + "' class='songShow " + i + "'>" +
        "<p>" + i + " " + songName + " by: " + artist + "</p>" +
        "<div class='btnDiv'>" +
        "<button onclick='addSongToPlaylist(this)' id='" + i + "' class='songBTN'>+</button>" +
        "</div></div>";

      $(".songContainer").append(songDiv);
    }
  }

  // Function to load playlists into the playlistContainer
  function loadPlaylists() {
    for (var i = 0; i < 10; i++) {
      var label = "Playlist " + i;

      $('#playlistContainer').append("<div id='playlist" + i + "' class='accordionContainer'>" +
        "<div class='label'>" + label + "</div>" +
        "<div class='content'></div></div><hr>");

      playlists.push([]); // Initialize an empty array for each playlist
    }
  }

  // Function to add a song to a playlist
  window.addSongToPlaylist = function (button) {
    var element = $(button).attr("id"); //gets the divs index
    var songIndex = parseInt(element);

    // Find the active playlist
    var activePlaylistIndex = findActivePlaylistIndex();
    if (activePlaylistIndex !== -1) {
      // Add the song to the active playlist
      playlists[activePlaylistIndex].push(new SongObject(songNames[songIndex], "Sample Artist", songIndex));

      // Update the playlist content
      updatePlaylistContent(activePlaylistIndex);
    }
  };

  // Function to update the content of the active playlist
  function updatePlaylistContent(playlistIndex) {
    var playlistContent = playlists[playlistIndex].map(function (song) {
      return "<div class='songShow'>" +
        "<p>" + song.songName + " by: " + song.artist + "</p>" +
        "<div class='btnDiv'>" +
        "<button onclick='removeSongFromPlaylist(this)' id='" + song.indexNum + "' class='songBTN'>-</button>" +
        "</div></div>";
    }).join('');

    $(".accordionContainer#playlist" + playlistIndex + " .content").html(playlistContent);
  }

  // Function to find the index of the active playlist
  function findActivePlaylistIndex() {
    for (var i = 0; i < accordion.length; i++) {
      if (accordion[i].classList.contains('active')) {
        return i;
      }
    }
    return -1; // Return -1 if no active playlist is found
  }

  // Function to remove a song from a playlist
  window.removeSongFromPlaylist = function (button) {
    var element = $(button).attr("id"); //gets the song index
    var songIndex = parseInt(element);

    // Find the active playlist
    var activePlaylistIndex = findActivePlaylistIndex();
    if (activePlaylistIndex !== -1) {
      // Remove the song from the active playlist
      playlists[activePlaylistIndex] = playlists[activePlaylistIndex].filter(function (song) {
        return song.indexNum !== songIndex;
      });

      // Update the playlist content
      updatePlaylistContent(activePlaylistIndex);
    }
  };

  // Function to toggle the active state of the accordion container
  function toggleActiveState() {
    $(this).toggleClass('active');
  }

  // Add event listener to each accordion container
  $('.accordionContainer').click(toggleActiveState);

});


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