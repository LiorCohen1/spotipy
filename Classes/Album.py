class Album:
    def __init__(self, id_number):
        self.id = id_number
        self.songs = []

    def add_song(self, song):
        self.songs.insert(song)

    def get_songs(self):
        return self.songs
