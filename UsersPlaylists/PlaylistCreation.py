from UsersPlaylists.PlaylistFunctions import PlaylistFunctions
from UsersPlaylists.Playlist import Playlist
from UsersPlaylists.Playlists import Playlists
from AuxiliaryFolder.AuxiliaryFunctions import AuxiliaryFunctions


class PlaylistCreation:
    def new_playlist(self, playlists, stock, author):
        name = PlaylistFunctions.get_name(PlaylistCreation)
        if PlaylistFunctions.is_name_valid(PlaylistCreation, name, playlists, author) == True:
            playlist = Playlist(name, author)
            AuxiliaryFunctions.print_songs(AuxiliaryFunctions, stock)
            id = input("Please enter a song ID to add it to this playlist. To finish adding the songs, enter Finish")
            while id != "Finish":
                song = AuxiliaryFunctions.get_song(AuxiliaryFunctions, stock, id)
                if song != None:
                    playlist.add_song(song)
                id = input(
                    "Please enter a song ID to add it to this playlist. To finish adding the songs, enter Finish")

            Playlists.add_new_paylist(playlists, playlist)

        else:
            print("The name is already in use")

        return playlists
