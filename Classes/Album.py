from AuxiliaryFolder.AuxiliaryFunctions import *


class Album:
    def __init__(self, id_code, album_name):
        self.id = id_code
        self.name = album_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs

    def add_song_into_album(self, album, artist, song):
        location = AuxiliaryFunctions.get_location(AuxiliaryFunctions, album.id, artist.albums)
        if location != -1:
            Album.add_song(artist.albums[location], song)
            return artist
