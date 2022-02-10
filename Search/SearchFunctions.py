from Search.SidesSearchFunctions import *
from AuxiliaryFolder.AuxiliaryFunctions import AuxiliaryFunctions


class SearchFunctions:
    def get_all_artists(self, stock):
        for artist in stock.artists:
            print(" artist id : " + artist.id)
            print(" artist name : " + artist.name)

    def get_all_albums(self, stock):
        AuxiliaryFunctions.print_artists(AuxiliaryFunctions, stock)
        artist_id = input("Please insert artist id")
        for artist in stock.artists:
            if artist.id == artist_id:
                for album in artist.albums:
                    print(" album name : " + album.name)

    def get_top_10(self, stock):
        AuxiliaryFunctions.print_artists(AuxiliaryFunctions, stock)
        artist_id = input("Please insert artist id")
        songs = SideSearchFunctions.insert_artist_songs(stock, artist_id)

        songs.sort(key=lambda x: x.popularity, reverse=True)
        if (len(songs) < 10):
            for i in range(len(songs)):
                print(songs[i].id)
                print(songs[i].popularity)
                print(songs[i].name)
        else:
            for i in range(10):
                print("song number : " + i)
                print(songs[i].id)
                print(songs[i].popularity)
                print(songs[i].name)

    def get_songs_in_album(self, stock):
        AuxiliaryFunctions.print_albums(AuxiliaryFunctions, stock)
        album_id = input("Please insert id")
        for artist in stock.artists:
            for album in artist.albums:
                if album.id == album_id:
                    for song in album.songs:
                        print("Song name: " + song.name)
                        print("Song id: " + song.id)
