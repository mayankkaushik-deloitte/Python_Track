from Main_Assignment.modules.LoginPage import login
from Main_Assignment.modules.RegisterPage import register_user
from Main_Assignment.modules.movieList import MovieList
from Main_Assignment.modules.userList import UserList
#init objects
movieObj = MovieList()
userObj = UserList()

while True:
    print("==============================******Welcome to BookMyShow*******========================")
    print("1. Login")
    print("2. Register new Account")
    print("3. Exit")

    option = int(input("Enter the option you want to choose :: "))
    if option == 1:
        login(movieObj, userObj)
        #print all movies
        for i in movieObj.mlist.values():
            print(i)
    elif option == 2:
        register_user(movieObj, userObj)
        #print all users
        for i in userObj.ulist.values():
            print(i)
    else:
        exit(0)
