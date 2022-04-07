from Main_Assignment.modules.movieList import MovieList
from Main_Assignment.modules.userList import UserList
from Main_Assignment.modules.userPage import UserPage


def register_user(movies: MovieList, users: UserList):
    print("***** Welcome to registration page *****")
    name = input("Name = ")
    email = input("Email = ")
    phone = input("Phone = ")
    age = int(input("Age = "))
    password = input("Password = ")
    if email in users.ulist:
        print("User already present go to the login page")
    else:
        users.add_user(UserPage(name, email, phone, age, password))
        print("User successfully registered")
