from FilesHandling.ReadFromFile import *
from AuxiliaryFolder.AuxiliaryFunctions import *
from Classes.Artist import Artist


class NewObjects:
    def add_new_objects(self, path, artists):
        song = ReadFromFile.new_song(ReadFromFile, path)
        song = Song(song.id, song.popularity, song.name)
        song_artists = (ReadFromFile.create_artists(ReadFromFile, path))

        album = (ReadFromFile.get_album(ReadFromFile, path))
        for artist in song_artists:
            if AuxiliaryFunctions.is_exists(AuxiliaryFunctions, artist, artists.artists):
                if AuxiliaryFunctions.is_exists(AuxiliaryFunctions, album, artists.get_artist(Artist.get_id(artist),artists).get_albums()):
                    AuxiliaryFunctions.add_song_into_album(AuxiliaryFunctions, album, artist, song)


                else:
                    Artist.add_album(artist, album)
                    Album.add_song_into_album(Album, album, artist, song)
            else:
                artists.add_artist(artist)
                artist.add_album(album)
                Album.add_song_into_album(Album, album, artist, song)
        return artists


