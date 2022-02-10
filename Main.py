from FilesHandling.UploadingFiles import UploadingFiles
from UsersPlaylists.PlaylistCreation import PlaylistCreation
from AuxiliaryFolder.Artists import Artists
from Classes.Playlists import Playlists

if __name__ == '__main__':
    artists = Artists()
    playlists = Playlists()
    folder_path = input("Please insert the folder path")
    if UploadingFiles.upload(UploadingFiles, folder_path, artists) !=False:
        artists=UploadingFiles.upload(UploadingFiles, folder_path, artists)
        author_name=input("Please enter your name")
        playlists = PlaylistCreation.new_playlist(PlaylistCreation,playlists,artists,author_name)
