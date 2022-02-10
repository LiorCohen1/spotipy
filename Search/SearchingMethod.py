from Search.SearchFunctions import SearchFunctions


class SearchingMethod:
    def searching(self, stock):
        answer = input(
            "Please enter number:1-Get all the artists that appear in the system, 2-By artist's ID get his album names, 3-By artist's ID get his 10 popular songs, 4-By album ID get all his songs, 5- Exit options The search")
        while answer != '5':
            if answer == '1':
                SearchFunctions.get_all_artists(SearchFunctions, stock)
            elif answer == '2':

                SearchFunctions.get_all_albums(SearchFunctions, stock)
            elif answer == '3':
                SearchFunctions.get_top_10(SearchFunctions, stock)
            elif answer == '4':
                SearchFunctions.get_songs_in_album(SearchFunctions, stock)
            else:
                print("Option dose not exist")
            answer = input(
                "Please enter number:1-Get all the artists that appear in the system, 2-By artist's ID get his album names, 3-By artist's ID get his 10 popular songs, 4-By album ID get all his songs, 5- Exit options The search")
