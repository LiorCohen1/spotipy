from FilesHandling.UploadingFiles import UploadingFiles
from UsersPlaylists.PlaylistCreation import PlaylistCreation
from AuxiliaryFolder.Artists import Artists
from Classes.Playlists import Playlists
from Search.SearchingMethod import SearchingMethod

if __name__ == '__main__':

    stock = Artists()
    playlists = Playlists()
    folder_path = input("Please insert the folder path")
    if UploadingFiles.upload(UploadingFiles, folder_path, stock) != False:
        answer = input("Please enter a number: 1- Create a playlist, 2- Search the database, 3- Exit the system")
        while answer != '3':
            if answer == '1':
                author_name = input("Please enter your name")
                playlists = PlaylistCreation.new_playlist(PlaylistCreation, playlists, stock, author_name)
            elif answer == '2':
                SearchingMethod.searching(SearchingMethod, stock)
            else:
                print("Option dose not exist")
            answer = input("Please enter a number: 1- Create a playlist, 2- Search the database, 3- Exit the system")
