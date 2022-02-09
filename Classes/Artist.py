class Artist:
    def __init__(self, id_code, artist_name):
        self.id = id_code
        self.name = artist_name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def get_albums(self):
        return self.albums
