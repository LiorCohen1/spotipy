from UsersPlaylists.PlaylistFunctions import PlaylistFunctions
from Classes.Playlist import Playlist
from Classes.Playlists import Playlists
from AuxiliaryFolder.AuxiliaryFunctions import AuxiliaryFunctions


class PlaylistCreation:
    def new_playlist(self, playlists, stock, author):
        name = PlaylistFunctions.get_name(PlaylistCreation)
        if PlaylistFunctions.is_name_valid(PlaylistCreation, name, playlists, author) == True:
            playlist = Playlist(name, author)
            AuxiliaryFunctions.print_songs(AuxiliaryFunctions, stock)
            PlaylistFunctions.add_song_into_playlist(PlaylistFunctions, playlist, stock)

            Playlists.add_new_playlist(playlists, playlist)

        else:
            print("The name is already in use")

        return playlists
