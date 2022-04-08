from Main_Assignment.modules.movieList import MovieList
from Main_Assignment.modules.movie import Movie


def getMins(s: str, foundHr: bool) -> int:
    s = s.split()
    hr, mins = 0, 0
    for i in s:
        if '0' <= i[0] <= '9':
            if not foundHr:
                hr, foundHr = int(i), True
            else:
                mins = int(i)
    return hr * 60 + mins


class Admin:
    def __init__(self):
        #init credentials for admin
        # with open("C:\\Users\\mayakaushik\\Python Track\\Main_Assignment\\data\\test.txt",'r') as file:
        #      for line in file.readlines():
        #          arr = line.split(',')
        #          print(arr)
        #          self.username = arr[0]
        #          self.username = arr[1]
        self.username = "admin"
        self.password = "123"

    def login(self, username, password) -> bool:
        #admin validation
        return self.username == username and self.password == password

    def get_movie(self) -> Movie:
        #take input for movie details
        title = input("Enter Title = ")
        genre = input("Enter Genre = ")
        length = getMins(input("Enter Length = "), False)
        cast = input("Enter Cast = ")
        director = input("Enter Director = ")
        rating = input("Enter Admin Rating = ")
        language = input("Enter Language = ")
        showCnt = int(input("Enter No of shows in a day = "))
        fs = getMins(input("Enter First Show = "), False)
        interval = getMins(input("Enter Interval timing = "), True)
        gap = getMins(input("Enter Gaps = "), True)
        cap = int(input("Enter Capacity = "))
        return Movie(title, genre, length, cast, director, rating, language, showCnt, fs, interval, gap, cap)

    def edit_movie(self, movies: MovieList):
        print("===================******Admin Edit Movie******====================")
        lst = list(movies.mlist.keys())
        mv = self.get_movie()
        for i in range(len(lst)):
            print(f"{i + 1}. {lst[i]}")
        if mv.movie_details['title'] in movies.mlist.keys():
            movies.mlist[mv.movie_details['title']] = mv
            print("---------------------------Update successful----------------------------------")
        else:
            print("No movie of this title")

    def add_movie(self, movies: MovieList):
        #add movie functionality
        print("=========================******Welcome Admin******========================")
        mv = self.get_movie()
        title = mv.movie_details['title']
        if title not in movies.mlist.keys():
            movies.add_movie(mv)
        else:
            print("XXXXXXXXXXXXXXXXXXXXXXX Movie already listed XXXXXXXXXXXXXXXXXX")

    def delete_movie(self, movies: MovieList):
        #delete movie functionality
        print("================***** Admin Delete Movie *****=================")
        lst = list(movies.mlist.keys())#get all the movies as a list
        for i in range(len(lst)):
            print(f"{i + 1}. {lst[i]}")
        inp = int(input("Enter which movie you want to delete = ")) - 1
        movies.mlist.pop(lst[inp])#remove that key movie

    def logout(self):
        print("************************Admin successfully logged out***********************")
