class PlaylistFunctions:
    def get_name(self):
        return input("Please enter a name for your new playlist")

    def is_name_valid(self, name, playlists_stock, author):
        for playlist in playlists_stock.playlists:
            if playlist.name == name:
                if playlist.author == author:
                    return False
        return True
