class Artist:
    def __init__(self, id_number):
        self.id = id_number
        self.albums = []

    def add_album(self, album):
        self.albums.insert(album)

    def get_albums(self):
        return self.albums
