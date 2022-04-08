from Main_Assignment.modules.movie import Movie


class MovieList:
    def __init__(self):
        self.mlist = dict()

    def __str__(self):
        return str(list(self.mlist.keys()))

    def get_movie_list(self) -> list:
        # convert the dict->keys to list
        return list(self.mlist.keys())

    def add_movie(self, movie: Movie):
        # add a movie to the dict
        self.mlist[movie.movie_details['title']] = movie

    def del_movie(self, movie_name: str):
        # exception handled if trying to delete movie which is not even there
        try:
            self.mlist.pop(movie_name)
        except:
            print("Movie was not found")
