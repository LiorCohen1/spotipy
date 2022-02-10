class Playlist:
    def __init__(self, name,author):
        self.author=author
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
