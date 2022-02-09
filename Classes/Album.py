class Album:
    def __init__(self, id_code, album_name):
        self.id = id_code
        self.name = album_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs
