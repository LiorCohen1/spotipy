class AuxiliaryFunctions:
    def is_exists(self, check_item, items):
        for item in items:
            if item.id == check_item.id:
                return True
            else:
                return False

    def get_location(self, id, items):
        counter = 0
        for cell in items:
            if cell.id == id:
                return counter
            else:
                counter = counter + 1

    def add_song_into_album(self, album, artist, song):
        location = AuxiliaryFunctions.get_location(AuxiliaryFunctions, album.id, artist.albums)
        artist.albums[location].add_song(song)
        return artist

    def get_id(self, item):
        return item.id
