from AuxiliaryFolder.AuxiliaryFunctions import AuxiliaryFunctions


class PlaylistFunctions:
    def get_name(self):
        return input("Please enter a name for your new playlist")

    def is_name_valid(self, name, playlists_stock, author):
        for playlist in playlists_stock.playlists:
            if playlist.name == name:
                if playlist.author == author:
                    return False
        return True

    def add_song_into_playlist(self, playlist, stock):
        id = input("Please enter a song ID to add it to this playlist. To finish adding the songs, enter Finish")
        while id != "Finish":
            song = AuxiliaryFunctions.get_song(AuxiliaryFunctions, stock, id)
            if song != None:
                playlist.add_song(song)
            id = input(
                "Please enter a song ID to add it to this playlist. To finish adding the songs, enter Finish")
