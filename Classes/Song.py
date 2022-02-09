class Song:
    def __init__(self, id_number):
        self.id = id_number
        self.popularity = 0

    def set_popularity(self):
        self.popularity = self.popularity + 1

    def get_popularity(self):
        return self.popularity
