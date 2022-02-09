import json
from Classes.Song import Song
from Classes.Album import Album
from Classes.Artist import Artist


class ReadFromFile:
    def __init__(self):
        pass

    def readFromAFile(self, path):
        json_file = open(path)
        data = json.load(json_file)
        json_file.close()
        data = data["track"]
        return data

    def new_song(self, path):
        song_data = self.readFromAFile(self, path)
        song_popularity = song_data["popularity"]
        song_name = song_data["name"]
        song_id_code = song_data["id"]
        song = Song(str(song_id_code), int(song_popularity), str(song_name))
        return song

    def get_album(self, path):
        album_data = self.readFromAFile(self, path)["album"]
        album_id_code = album_data["id"]
        album_name = album_data["name"]
        album = Album(str(album_id_code), str(album_name))
        return album

    def get_artist(self, path):
        artists_data = self.readFromAFile(self, path)["artists"]
        artists = []
        for artist in artists_data:
            artist_id_code = artist["id"]
            artist_name = artist["name"]
            artist = Artist(str(artist_id_code), str(artist_name))
            artists.append(artist)
        return artists
