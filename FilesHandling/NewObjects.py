from ReadFromFile import *
from AuxiliaryFolder.AuxiliaryFunctions import AuxiliaryFunctions
from Classes.Artist import Artist


class NewObjects:
    def add_new_objects(self, path, artists):
        song = ReadFromFile.new_song(ReadFromFile, path)
        song_artists = (ReadFromFile.get_artist(ReadFromFile, path))

        album = (ReadFromFile.get_album(ReadFromFile, path))
        for artist in song_artists:
            if AuxiliaryFunctions.is_exists(AuxiliaryFunctions, artist, artists):
                if AuxiliaryFunctions.is_exists(AuxiliaryFunctions, album, artists.get_artist(Artist.get_id(artist))):
                    AuxiliaryFunctions.add_song_into_album(AuxiliaryFunctions, album, artist, song)


                else:
                    artist.add_album(artist, album)
                    AuxiliaryFunctions.add_song_into_album(AuxiliaryFunctions, album, artist, song)
            else:
                artists.append(artist)
                artist.add_album(album)
                AuxiliaryFunctions.add_song_into_album(AuxiliaryFunctions, album, artist, song)
        return artists, artist
