class SideSearchFunctions:
    def insert_artist_songs(stock, artist_id):
        songs = []
        for artist in stock.artists:
            if artist.id == artist_id:
                for album in artist.albums:
                    for song in album.songs:
                        songs.append(song)
        return songs
