from AuxiliaryFolder.AuxiliaryFunctions import AuxiliaryFunctions


class Artists:
    def __init__(self):
        self.artists = []

    def add_artist(self, artist):
        self.artists.append(artist)

    def get_artist(self, id, artist):
        location = AuxiliaryFunctions.get_location(AuxiliaryFunctions, id, artist)
        return self.artists[location]
