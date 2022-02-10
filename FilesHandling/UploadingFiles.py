import os
from FilesHandling.NewObjects import *


class UploadingFiles:
    def upload(self, folder_path, artists):
        try:
            for path in os.listdir(folder_path):
                full_path = os.path.join(folder_path, path)
                if os.path.isfile(full_path):
                    artists = NewObjects.add_new_objects(NewObjects, full_path, artists)
            return artists
        except FileNotFoundError:
            print("Wrong path")
            return False
