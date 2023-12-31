-- This file is intended to set up and fill a music database structure in ----MySQL---- This might not work in another DBMS
-- 
-- created by Noah Frost
--
-- References:
-- https://www.w3schools.com/sql/sql_primarykey.asp
-- https://www.w3schools.com/sql/sql_foreignkey.asp
-- https://dev.mysql.com/doc/refman/8.0/en/comments.html


USE music;

DROP SCHEMA music;

CREATE SCHEMA music;

USE music;


-- create all tables first

create table `Song` (
    `ID` int,
    `name` varchar(255),
    `artist` int, -- foreign key to artist.ID
    `album` int, -- foreign key to album.ID
    `release` datetime,
    `genre` varchar(255),
    `listens` int,
    `length` int, -- in seconds
    `filepath` varchar(255),
    primary key (ID)
);

create table `Album` (
    `ID` int,
    `name` varchar(255),
    `artist` int, -- foreign key to artist.ID
    `release date` datetime,
    primary key (ID)
);

create table `Artist` (
    `ID` int,
    `name` varchar(255),
    `followerCount` int,
    `dateJoin` datetime, -- when the artist joined
    primary key (ID)
);

create table `User` (
    `ID` int AUTO_INCREMENT,
    `uname` varchar(255),
    `password` varchar(255),
    `name` varchar(255),
    `dateJoin` datetime,
    primary key (ID)
);

-- this table specifies what each user is listening to so friends can see what their friends are listening to -- This table is sepate from User and sorted by user.ID to make searching easier
create table `Listen Now` (
    `userID` int, -- foreign key to User.ID
    `songID` int, -- foreign key to Song.ID
    primary key (userID)
);

-- this holds the data of what artists each user follows
create table `Follow Artist` ( 
    `artist` int, -- foreign key to artist.ID
    `user` int, -- foreign key to user.ID
    primary key (artist, user)
);

create table `Follow Album` (
    `album` int, -- foreign key to Album.ID
    `user` int, -- foreign key to User.ID
    primary key (album, user)
);

create table `Friend` (
    `u1` int, -- USER 1 --- foreign key to user.ID
    `u2` int, -- USER 2 --- foreign key to user.ID
    primary key (u1, u2)
);

create table `Playlist` (
    `ID` int,
    `SongID` int, -- foreign key to Song.ID
    `Order` int, -- the order of the song in the playlist
    primary key (ID, SongID)
);

-- holds the data of which user owns which playlist
create table `Owned` (
    `userID` int, -- foreign key to User.ID
    `playlistID` int, 
    `name` varchar(255), -- the name of the playlist
    primary key (userID, playlistID)
);


-- adding all foreign keys -- foreign keys are set up seperately to ensure there are no ordering errors when creating tables

alter table song
add foreign key (artist) references Artist(ID);
alter table song
add foreign key (album) references Album(ID);

alter table album
add foreign key (artist) references artist(ID);

alter table `Listen Now`
add foreign key (userID) references User(ID);
alter table `Listen Now`
add foreign key (songID) references Song(ID);

alter table `Follow Artist`
add foreign key (artist) references Artist(ID);
alter table `Follow Artist`
add foreign key (user) references User(ID);

alter table `Follow Album`
add foreign key (album) references Album(ID);
alter table `Follow Album`
add foreign key (user) references User(ID);

alter table Friend
add foreign key (u1) references User(ID);
alter table Friend
add foreign key (u2) references User(ID);

alter table Playlist
add foreign key (songID) references Song(ID);

alter table Owned
add foreign key (userID) references User(ID);

-- adding all data to tables

insert into `Artist` values (
    1,
    "Example Artist",
    1000000,
    '2023-12-7 0:00:00'
);

insert into `Album` values (
    1,
    "Example Album",
    1,
    '2023-12-7 0:00:00'
);

insert into `Song` values (
    1,
    "Song number 1",
    1,
    1,
    '2023-12-7 0:00:00',
    "pop",
    1234,
    187,
    "https://open.spotify.com/embed/track/1hQFF33xi8ruavZNyovtUN?utm_source=generator"
);

insert into `User` values (
    1,
    "uname1",
    "pass1",
    "Person One",
    '2023-12-7 0:00:00'
);

insert into `User` values (
    2,
    "uname2",
    "pass2",
    "Person Two",
    '2023-12-7 0:00:00'
);

insert into `Listen Now` values (
    2,
    1
);

insert into `Follow Artist` values ( 
    1,
    1
);

insert into `Follow Album` values (
    1,
    1
);

insert into `Friend` values (
    1,
    2
);

insert into `Playlist` values (
    1,
    1,
    1
);

insert into `Owned` values (
    1,
    1,
    "Example Playlist"
);