class Song:
    def __init__(self, id_code, song_popularity, song_name):
        self.id = id_code
        self.popularity = song_popularity
        self.name = song_name



    def get_popularity(self):
        return self.popularity
